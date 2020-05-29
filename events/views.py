from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from .forms import CreateNewEvent, ModifyEvent
from .models import MainEvent, SmallEvent


def nr(response):
    return HttpResponse("panel wydarzenia")


def register(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateNewEvent(request.POST)
            if form.is_valid():
                ev_nam = form.cleaned_data["ev_Nam"]

                ev_st_d = form.cleaned_data["ev_Start_Date"]
                ev_st_t = form.cleaned_data["ev_Start_Time"]

                ev_end_d = form.cleaned_data["ev_End_Date"]
                ev_end_t = form.cleaned_data["ev_End_Time"]

                own = request.user

                ev_des = form.cleaned_data["ev_Description"]
                ev_pro = form.cleaned_data["ev_Program"]

                # ev_map = form.changed_data["ev_Map"]
                # ev_icon = form.changed_data["ev_Icon"]
                # Event_MapFile = ev_map, # czemu to krwa nie dziala
                # Event_IconFile = ev_icon

                t = MainEvent(Event_Name=ev_nam, Event_Start_Date=ev_st_d, Event_Start_Time=ev_st_t,
                              Event_End_Date=ev_end_d, Event_End_Time=ev_end_t, Even_Owner=own,
                              Event_Description=ev_des,
                              Event_Program=ev_pro)
                t.save()

            return HttpResponseRedirect("../details/" + str(t.id))
        else:
            form = CreateNewEvent()

        return render(request, "events/register.html", {"form": form})
    else:
        return HttpResponseRedirect("/../LoginError")


def details(request, i=None):
    instance = get_object_or_404(MainEvent, id=i)
    # small_events = get_list_or_404(SmallEvent, Main_Event_ID=instance.id)
    small_events = SmallEvent.objects.filter(Main_Event_ID=instance.id)
    print(small_events)
    context = {
        "instance": instance,
        "test": small_events,
    }
    return render(request, "events/show.html", context)


def edit(request, i=None):
    instance = get_object_or_404(MainEvent, id=i)

    if request.user == instance.Even_Owner:
        instance_form = ModifyEvent(request.POST or None, instance=instance)
        if instance_form.is_valid():
            instance_form.save()

        return render(request, 'events/upload.html', {'upload_form': instance_form})
    else:
        return HttpResponseRedirect("/../LoginError")


def delete(request, i=None):
    instance = get_object_or_404(MainEvent, id=i)
    if request.user == instance.Even_Owner:
        instance.delete()
        return HttpResponse("Usunieto")
    else:
        return HttpResponseRedirect("/../LoginError")


def suc(request):
    return HttpResponse("Działa")
