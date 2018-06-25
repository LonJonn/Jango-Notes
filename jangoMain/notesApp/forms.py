from django import forms
from .models import Note
from django.contrib.auth.models import User

from bootstrap_datepicker_plus import DateTimePickerInput

class NoteForm(forms.ModelForm):    #note form structure for adding and editing notes, inherited from note model
    class Meta:
        model = Note    #where to inherit
        exclude = ['owner']     #dont include option to change user
        widgets = {'dateDue': DateTimePickerInput(options={     #options for the bootstrap date picker
            "showClose": False,
            "showClear": False,
            "showTodayButton": True,
            "format": "MM/DD/YYYY HH:mm",
        })}

    def __init__(self, *args, **kwargs):    #on creation, add form-control class to inputs
        super(NoteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

from django.contrib.auth.forms import UserCreationForm  #get user create form from django
from django.utils.safestring import mark_safe

class SignUpForm(UserCreationForm):     #create custom sign up form from UserCreationForm
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')   #required email addition entry

    class Meta:
        model = User    #model to structure from
        fields = ('username', 'email', 'password1', 'password2', )  #field to include in form

    def __init__(self, *args, **kwargs):    #on create
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():   #for every field, add form-control class
            field.widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = mark_safe(self.fields['password1'].help_text)  #change help text to proper html