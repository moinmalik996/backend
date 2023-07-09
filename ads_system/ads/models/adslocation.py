from django.db import models
from django.db.models import Case, When, Value, F
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from .ad import Ad
from .location import Location

from ..tasks import schedule_task_after_24_hours, calculate


class AdsLocationManager(models.Manager):

    def with_expiration_data(self):
        return self.get_queryset().annotate(
            date_expired=Case(
                When(end_date__lt=timezone.now(), then=Value(True)),
                When(end_date__gte=timezone.now(), then=Value(False)),
            ),
            max_reached=Case(
                When(visits__gte=F('max_visits'), then=Value(True)),
                default=False
            ),
        )

class AdsLocation(models.Model):
    max_visits = models.IntegerField(default=1)
    visits = models.IntegerField(default=0)
    ad = models.ForeignKey(Ad, on_delete=models.PROTECT, related_name='ads')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='ads')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f"{self.location.name}-{self.ad.name}"
    
    objects = AdsLocationManager()


@receiver(post_save, sender=AdsLocation)
def my_sceduale_task(sender, instance, created, **kwargs):
    calculate.delay(10, 20)
    