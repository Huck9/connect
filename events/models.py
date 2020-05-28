from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Event(models.Model):
    Event_Name = models.TextField()
    Event_Start_Date = models.DateField()
    Event_Start_Time = models.TimeField()
    Even_Owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='1')

    def __str__(self):
        return self.Event_Name
