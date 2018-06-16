from django import forms
from .models import Note

class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['owner']