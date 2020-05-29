from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import CreateMainEvent, ModifyMainEvent, CreateSmallEvent, ModifySmallEvent
from .forms import RegisterToEvent, AddOpinion
from .models import EventRegister, EventSmallRegister, eventOpinion
from .models import MainEvent, SmallEvent


def add_main_event(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateMainEvent(request.POST)
            if form.is_valid():
                # ev_map = form.changed_data["ev_Map"]
                # ev_icon = form.changed_data["ev_Icon"]
                # Event_MapFile = ev_map,
                # Event_IconFile = ev_icon

                t = MainEvent(Event_Name=form.cleaned_data["ev_Nam"],
                              Event_Start_Date=form.cleaned_data["ev_Start_Date"],
                              Event_Start_Time=form.cleaned_data["ev_Start_Time"],
                              Event_End_Date=form.cleaned_data["ev_End_Date"],
                              Event_End_Time=form.cleaned_data["ev_End_Time"],
                              Even_Owner=request.user,
                              Event_Description=form.cleaned_data["ev_Description"],
                              Event_Program=form.cleaned_data["ev_Program"])
                t.save()

            return HttpResponseRedirect("../events/details/" + str(t.id))
        else:
            form = CreateMainEvent()

        return render(request, "events/createEvent.html", {"form": form})
    else:
        return HttpResponseRedirect("/../LoginError")


def deleteOpinion(request,i=None):
    if request.user.is_authenticated:
        instance = get_object_or_404(eventOpinion, id=i)
        if request.user == instance.Main_Event_ID.Even_Owner:
            instance.delete()
            return render(request, 'events/deleteinfo.html', {'delete_info': "Usunieto Opinie"})
        else:
            return HttpResponseRedirect("/../LoginError")


def details_main_event(request, i=None):
    instance = get_object_or_404(MainEvent, id=i)
    small_events = SmallEvent.objects.filter(Main_Event_ID=instance.id)
    eventOpinion2 = eventOpinion.objects.filter(Main_Event_ID=instance.id)
    context = {
        "instance": instance,
        "small_events": small_events,
        "eventOpinion": eventOpinion2,
    }
    return render(request, "events/show.html", context)


def edit_main_event(request, i=None):
    instance = get_object_or_404(MainEvent, id=i)

    if request.user == instance.Even_Owner:
        instance_form = ModifyMainEvent(request.POST or None, instance=instance)
        if instance_form.is_valid():
            instance_form.save()

        return render(request, 'events/upload.html', {'upload_form': instance_form})
    else:
        return HttpResponseRedirect("/../LoginError")


def delete_main_event(request, i=None):
    instance = get_object_or_404(MainEvent, id=i)
    if request.user == instance.Even_Owner:
        instance.delete()
        return render(request, 'events/deleteinfo.html', {'delete_info': "Usunieto Wydarzenie"})
    else:
        return HttpResponseRedirect("/../LoginError")


def add_small_event(request, i=None):
    if request.user.is_authenticated:
        event = get_object_or_404(MainEvent, id=i)

        if request.user == event.Even_Owner:
            if request.method == "POST":
                form = CreateSmallEvent(request.POST)

                if form.is_valid():
                    t = SmallEvent(SmallEvent_Name=form.cleaned_data["ev_Nam"],
                                   SmallEvent_Start_Date=form.cleaned_data["ev_Start_Date"],
                                   SmallEvent_Start_Time=form.cleaned_data["ev_Start_Time"],
                                   SmallEvent_End_Date=form.cleaned_data["ev_End_Date"],
                                   SmallEvent_End_Time=form.cleaned_data["ev_End_Time"],
                                   SmallEvent_Description=form.cleaned_data["ev_Description"],
                                   SmallEvent_Prelegent=form.cleaned_data["ev_Prelegent"],
                                   Main_Event_ID=event)
                    t.save()

                return HttpResponseRedirect("/../events/details/" + str(i))
            else:
                form = CreateSmallEvent()

            return render(request, "events/createEvent.html", {"form": form})
        else:
            return HttpResponseRedirect("/../LoginError")

    else:
        return HttpResponseRedirect("/../LoginError")


def delete_small_event(request, i=None):
    small_eve = get_object_or_404(SmallEvent, id=i)
    main_eve = get_object_or_404(MainEvent, id=small_eve.Main_Event_ID.id)
    if request.user == main_eve.Even_Owner:
        small_eve.delete()
        return render(request, 'events/deleteinfo.html', {'delete_info': "Usunieto PodWydarzenie"})
    else:
        return HttpResponseRedirect("/../LoginError")


def edit_small_event(request, i=None):
    small_eve = get_object_or_404(SmallEvent, id=i)
    main_eve = get_object_or_404(MainEvent, id=small_eve.Main_Event_ID.id)

    if request.user == main_eve.Even_Owner:
        small_eve_form = ModifySmallEvent(request.POST or None, instance=small_eve)
        if small_eve_form.is_valid():
            small_eve_form.save()

        return render(request, 'events/upload.html', {'upload_form': small_eve_form})
    else:
        return HttpResponseRedirect("/../LoginError")


def register_to_event(request, i=None):
    if request.user.is_authenticated:
        instance = get_object_or_404(MainEvent, id=i)
        small_events = SmallEvent.objects.filter(Main_Event_ID=instance.id)
        form = RegisterToEvent()
        context = {
            "instance": instance,
            "small_events": small_events,
            "form": form,
        }
        if request.method == "POST":
            instance_form = CreateMainEvent(request.POST)
            if instance_form.is_valid:
                user_name = request.POST['User_name']
                user_surname = request.POST['User_surname']
                model = EventRegister()
                model.User_Add = request.user
                model.User_name = request.POST['User_name']
                model.User_surname = request.POST['User_surname']
                model.Main_Event_ID = instance
                model.save()
                listEvent = request.POST.getlist('events')
                for i in listEvent:
                    model2 = EventSmallRegister()
                    model2.EventRegister = model
                    model2.SmallEvent = SmallEvent.objects.get(pk=i)
                    model2.save()
            return render(request, "events/show.html", context)

        return render(request, "events/registerForm.html", context)
    else:
        return HttpResponseRedirect("/../LoginError")


def add_opinion(request,i=None):
    instance = get_object_or_404(MainEvent, id=i)
    if request.method == 'POST':
        model = eventOpinion()
        model.Opinion = request.POST['Opinion']
        model.Name = request.POST['Name']
        model.Main_Event_ID = instance
        model.save()
        return HttpResponseRedirect("/")
    form = AddOpinion()
    return render(request, "events/addOpinion.html", {'form': form})