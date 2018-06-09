from django.shortcuts import render
from .models import Note


def index(request):
    return render(request, 'notesApp/index.html', {})

def notes(request):
    notes = Note.objects.all()
    return render(request, 'notesApp/notes.html', {'notes': notes})

def noteInfo(request):
    return render(request, 'notesApp/noteInfo.html')
