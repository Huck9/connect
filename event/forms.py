from django import forms
from .models import MainEvent


class MainEventCreate(forms.ModelForm):

    class Meta:
        model = MainEvent
        fields = ['event_name','event_place', 'event_date','event_time','event_dec']
