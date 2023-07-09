from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.apps import apps


@shared_task
def set_visits_to_zero(ad_id):
    ad = apps.get_model('ads.AdsLocation').objects.with_expiration_data() \
                                .filter(id=ad_id, date_expired=False) \
                                .first()
    ad.visits = 0
    ad.save()


@shared_task
def schedule_task_after_24_hours(ad_id):
    set_visits_to_zero.apply_async(args=[ad_id], eta=timezone.now() + timedelta(days=1))

