from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .form import RegisterForm
from events.models import MainEvent, SmallEvent
from events.models import EventRegister, EventSmallRegister


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


def login_error(request):  # usun _
    return render(request, "register/loginerror.html")


def showuserpanel(request):
    if request.user.is_authenticated:
        instance = EventRegister.objects.all().filter(User_Add=request.user)
        events = MainEvent.objects.all().filter(Even_Owner=request.user)
        print(events)
        field = {
            "instance": instance,
            "events": events,
        }
        return render(request, "register/userpanel.html", field)
    else:
        return HttpResponseRedirect("/../LoginError")


def userpanelid(request, i=None,j=None):
    if request.user.is_authenticated:
        instance = get_object_or_404(MainEvent, id=i)
        order = EventRegister.objects.all().filter(Main_Event_ID=instance)
        order = order.filter(pk=j)

        miniorder = EventSmallRegister.objects.all().filter(EventRegister=order[0])
        field = {
            "instance": instance,
            'order': order,
            'miniorder': miniorder,
        }
        return render(request, "register/userpanelid.html", field)
    else:
        return HttpResponseRedirect("/../LoginError")
