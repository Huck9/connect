from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from events import models


def home(request):
	event = models.MainEvent.objects.all()
	return render(request, "main/index.html", {'event': event})

