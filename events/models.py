from django.db import models


# Create your models here.
class Ticket(models.Model):
    Ticket_Name = models.TextField()
    Ticket_Amount = models.SmallIntegerField()
    Ticket_Price = models.FloatField()


class TicketList(models.Model):
    dupa = models.TextField()


class Event(models.Model):
    Event_Name = models.TextField()
