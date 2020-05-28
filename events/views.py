from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import CreateNew
from .models import Event



def nr(response):
    return HttpResponse("panel wydarzenia")


def Register(response):
    if response.method == "POST":
        form = CreateNew(response.POST)
        if form.is_valid():
            ev_nam = form.cleaned_data["ev_Nam"]

            t = Event(Event_Name=ev_nam)
            t.save()
        return HttpResponseRedirect("succes")
    else:
        form = CreateNew()

    return render(response, "events/register.html", {"form": form})


def suc(response):
    return HttpResponse("Działa")



