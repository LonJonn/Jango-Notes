from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q

from .models import Note
from django.contrib.auth.models import User


def Index(request):
    notesCount = Note.objects.all().count()
    usersCount = User.objects.all().count()

    return render(request, 'notesApp/index.html', {'usersCount': usersCount, 'notesCount': notesCount})


from django.contrib.auth.decorators import login_required

@login_required
def Notes(request):
    search = request.GET.get('search', '')
    sort = request.GET.get('sort', 'dateCreated')
    noteList = Note.objects.filter(owner=request.user).filter(
        Q(title__contains=search) | 
     Q(description__contains=search) | 
     Q(group__contains=search) | 
     Q(colour__contains=search)
     ).order_by(sort)

    return render(request, 'notesApp/notes.html', {'noteList': noteList})


from .forms import NoteForm

@login_required
def CreateNote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.cleaned_data['owner'] = request.user
            Note.objects.create(**form.cleaned_data)
            return redirect('notes')
    else:
        form = NoteForm()
    return render(request, 'notesApp/noteForm.html', {'form': form })

@login_required
def EditNote(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.owner != request.user:
        raise Http404("You can only edit your own notes.")
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notesApp/noteForm.html', {'form': form })

@login_required
def DeleteNote(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.owner != request.user:
        raise Http404("You can only delete your own notes.")
    note.delete()

    return redirect('notes')

from .forms import UserForm
from django.contrib.auth import login

def CreateUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('notes')
    else:
        form = UserForm()

    return render(request, 'notesApp/register.html', {'form': form})