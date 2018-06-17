from django import forms
from .models import Note
from django.contrib.auth.models import User

from bootstrap_datepicker_plus import DateTimePickerInput

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['owner']
        widgets = {'dateDue': DateTimePickerInput(options={
            "showClose": False,
            "showClear": False,
            "showTodayButton": True,
            "format": "MM/DD/YYYY HH:mm",
        })}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
