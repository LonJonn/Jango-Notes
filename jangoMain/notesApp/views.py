from django.shortcuts import render
from .models import Note


def index(request):
    return render(request, 'notesApp/index.html', {})

def info(request):
    notes = Note.objects.all()
    return render(request, 'notesApp/info.html', {'notes': notes})