from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Event(models.Model):
    Event_Name = models.TextField(default="no-name")

    Event_Start_Date = models.DateField(default="0000-00-00")
    Event_Start_Time = models.TimeField(default="00:00:00")
    #
    Event_End_Date = models.DateField(default="0000-00-00")
    Event_End_Time = models.TimeField(default="00:00:00")

    Even_Owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='1')

    # Tickets

    # Event_IconFile = models.FileField(default=None, null=True)
    # Event_MapFile = models.FileField(default=None, null=True)

    Event_Description = models.TextField(default="Opis")
    Event_Program = models.TextField(default="Program")

    def __str__(self):
        return self.Event_Name
