from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class MainEvent(models.Model):

    event_name = models.TextField(max_length=250)
    event_place = models.TextField(max_length=250)
    event_date = models.DateField()
    event_time = models.DateTimeField()
    event_dec = models.TextField(max_length=250)

    def __str__(self):
        return self.event_name
