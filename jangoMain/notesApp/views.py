from django.shortcuts import render
from .models import User, Note


def index(request):
    return render(request, 'notesApp/index.html', {})


def login(request):
    return render(request, 'notesApp/login.html', {})

def info(request):
    noteInfo = Note.objects.all()
    context = {'noteInfo': noteInfo}
    return render(request, 'notesApp/info.html', {'notes': 'i'})