from django.shortcuts import render, redirect
from .models import MainEvent
from .forms import MainEventCreate
from django.http import HttpResponse


# Create your views here.


def events(request):
    if request.user.is_authenticated:
        event = MainEvent.objects.all()
        return render(request, 'event/showEvents.html', {'event': event})
    else:
        return redirect('/LoginError')


def add_event(request):
    if request.user.is_authenticated:

        event = MainEventCreate()
        if request.method == 'POST':
            event = MainEventCreate(request.POST, request.FILES)

            if event.is_valid():
                event.save()
                return redirect('/../event')
            else:
                return redirect('/../event/addEvent/')
        else:
            return render(request, 'event/upoladform.html', {'form': event})
    else:
        return redirect('/LoginError')
