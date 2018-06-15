from django.shortcuts import render, get_object_or_404
from django.http import Http404
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

def editNote(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notesApp/editNote.html', {'note': note})
