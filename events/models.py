from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class EventRegister(models.Model):
    User_Add = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='1')
    Main_Event_ID = models.ForeignKey('MainEvent', on_delete=models.CASCADE, default=1)
    User_name = models.TextField(default="Imie")
    User_surname = models.TextField(default="Nazwisko")


class EventSmallRegister(models.Model):
    EventRegister = models.ForeignKey('EventRegister', on_delete=models.CASCADE,default=0)
    SmallEvent = models.ForeignKey('SmallEvent', on_delete=models.CASCADE, default=1)


class SmallEvent(models.Model):
    Show_Name = models.TextField(default="Small event")

    Show_Start_Date = models.DateField(default="2020-01-01")
    Show_Start_Time = models.TimeField(default="00:00:00")
    #
    Show_End_Date = models.DateField(default="2020-01-01")
    Show_End_Time = models.TimeField(default="00:00:00")

    Show_Description = models.TextField(default="Opis")

    Main_Event_ID = models.ForeignKey('MainEvent', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Show_Name


class MainEvent(models.Model):
    Event_Name = models.TextField(default="no-name")

    Event_Start_Date = models.DateField(default="2020-01-01")
    Event_Start_Time = models.TimeField(default="00:00:00")
    #
    Event_End_Date = models.DateField(default="2020-01-01")
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


