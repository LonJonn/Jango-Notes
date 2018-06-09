from django.shortcuts import render
from .models import Note
from django.contrib.auth.models import User


def index(request):
    numNotes = Note.objects.all().count()
    numUsers = User.objects.all().count()
    return render(request, 'notesApp/index.html', {'numUsers': numUsers, 'numNotes': numNotes})

def notes(request):
    notes = Note.objects.all()
    numNotes = notes.count()
    return render(request, 'notesApp/notes.html', {'notes': notes, 'numNotes': numNotes})

def noteInfo(request):
    return render(request, 'notesApp/noteInfo.html')
