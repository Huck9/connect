from django.shortcuts import render, redirect
from .models import MainEvent
from .forms import MainEventCreate
from django.http import HttpResponse
# Create your views here.


def showevent(request):
    if request.user.is_authenticated:
        event = MainEvent.objects.all()
        return render(request, 'event/showEvents.html', {'event': event})
    else:
        return redirect('main/index.html')


def addevent(request):
    event = MainEventCreate()
    if request.method == 'POST':
        event = MainEventCreate(request.POST, request.FILES)
        if event.is_valid():
            event.save()

            return redirect('event/showEvents.html', {'event': event})
        else:
            return redirect('main/index.html')
    else:
        return render(request, 'event/upoladform.html', {'form': event})