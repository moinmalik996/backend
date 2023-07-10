from django.db import models

class Ad(models.Model):
    name = models.CharField(max_length=250, unique=True)
    locations = models.ManyToManyField('Location', through='AdsLocation')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name