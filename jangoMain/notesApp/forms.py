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

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = mark_safe(self.fields['password1'].help_text)