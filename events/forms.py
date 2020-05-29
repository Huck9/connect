from django import forms
from django.views.generic.edit import UpdateView
from .models import MainEvent, SmallEvent


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CreateNewEvent(forms.Form):
    ev_Nam = forms.CharField(label="Nazwa Wydarzenia", max_length=30)

    ev_Start_Date = forms.DateField(label="Data rozpoczecia wydarzenia", widget=DateInput, required=True)
    ev_Start_Time = forms.TimeField(label="Czas rozpoczęcia wydarzenia", widget=TimeInput, required=True)

    ev_End_Date = forms.DateField(label="Data zakonczenia wydarzenia", widget=DateInput, required=True)
    ev_End_Time = forms.TimeField(label="Czas zakonczenia wydarzenia", widget=TimeInput, required=True)

    ev_Description = forms.CharField(label="Opis wydarzenia")
    ev_Program = forms.CharField(label="Program wydarzenia")


class ModifyEvent(forms.ModelForm):
    class Meta:
        model = MainEvent
        fields = ['Event_Name', 'Event_Start_Date', 'Event_Start_Time', 'Event_End_Time', 'Event_Description',
                  'Event_Program']


class CreateNewShow(forms.ModelForm):
    class Meta:
        model = SmallEvent
        fields = "__all__"