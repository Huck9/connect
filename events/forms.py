from django import forms
from django.views.generic.edit import UpdateView
from .models import Event


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CreateNew(forms.Form):
    ev_Nam = forms.CharField(label="Nazwa Wydarzenia", max_length=30)

    ev_Start_Date = forms.DateField(label="Data rozpoczecia wydarzenia", widget=DateInput, required=True)
    ev_Start_Time = forms.TimeField(label="Czas rozpoczęcia wydarzenia", widget=TimeInput, required=True)

    ev_End_Date = forms.DateField(label="Data zakonczenia wydarzenia", widget=DateInput, required=True)
    ev_End_Time = forms.TimeField(label="Czas zakonczenia wydarzenia", widget=TimeInput, required=True)

    # tickets

    # ev_Icon = forms.FileField(label="Ikona Eventu", required=False)
    # ev_Map = forms.FileField(label="Mapa Eventu", required=False)


class ModifyEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['Event_Name', 'Event_Start_Date', 'Event_Start_Time', 'Event_End_Time', 'Event_Description',
                  'Event_Program']
