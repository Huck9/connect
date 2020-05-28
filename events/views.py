from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import CreateNew
from .models import Event


def nr(response):
    return HttpResponse("panel wydarzenia")


def register(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = CreateNew(response.POST)
            if form.is_valid():
                ev_nam = form.cleaned_data["ev_Nam"]
                ev_st_d = form.cleaned_data["ev_Start_Date"]
                ev_st_t = form.cleaned_data["ev_Start_Time"]
                own = response.user.id
                t = Event(Event_Name=ev_nam, Event_Start_Date=ev_st_d, Event_Start_Time=ev_st_t, Even_Owner=own)
                t.save()
            return HttpResponseRedirect("succes")
        else:
            form = CreateNew()

        return render(response, "events/register.html", {"form": form})
    else:
        return HttpResponseRedirect("/../LoginError")


def suc(response):
    return HttpResponse("Działa")
