from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django import apps


@shared_task
def your_celery_task(ad_id):
    try:
        ad = apps.get_model('ads.AdsLocation').objects.with_expiration_data() \
                                    .filter(id=ad_id, date_expired=False) \
                                    .first()
    except ad.DoesNotExist:
        return
   
    ad.max_visits = 0
    ad.save()


@shared_task
def schedule_task_after_24_hours(ad_id):
    your_celery_task.apply_async(args=[ad_id], eta=timezone.now() + timedelta(minutes=1))


@shared_task
def calculate():
    print("----------------------==================================")
    return "Someting"
