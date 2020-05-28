from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CreateNew(forms.Form):
    ev_Nam = forms.CharField(label="Nazwa Wydarzenia", max_length=30)

    ev_Start_Date = forms.DateField(label="Data rozpoczecia wydarzenia", widget=DateInput, required=False)
    ev_Start_Time = forms.TimeField(label="Czas rozpoczęcia wydarzenia", widget=TimeInput, required=False)

    ev_End_Date = forms.DateField(label="Data zakonczenia wydarzenia (1)", widget=DateInput, required=False)
    ev_End_Time = forms.TimeField(label="Czas zakonczenia wydarzenia (1)", widget=TimeInput, required=False)


