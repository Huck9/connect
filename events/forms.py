from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CreateNew(forms.Form):
    Nazwa_Wyd = forms.CharField(label="Nazwa Wydarzenia", max_length=30)

    Data_rozp = forms.DateField(label="Data rozpoczecia wydarzenia", widget=DateInput)
    Czas_rozp = forms.TimeField(label="Czas rozpoczęcia wydarzenia", widget=TimeInput)

    Data_zak = forms.DateField(label="Data zakonczenia wydarzenia (1)", widget=DateInput)
    Czas_zak = forms.TimeField(label="Czas zakonczenia wydarzenia (1)", widget=TimeInput)

    Czas_trw = forms.TimeField(label="Czas  trwania wydarzenia (2)", widget=TimeInput)
