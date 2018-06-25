from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q

from .models import Note
from django.contrib.auth.models import User


def Index(request):     #on index visit
    notesCount = Note.objects.all().count() #get count of main info
    usersCount = User.objects.all().count()
    try:
        latestNote = Note.objects.order_by('-pk')[0]
    except:
        latestNote = None
        #get most recent note
    return render(request, 'notesApp/index.html', {'usersCount': usersCount, 'notesCount': notesCount, 'latestNote': latestNote})


from django.contrib.auth.decorators import login_required

@login_required #require user to login
def Notes(request): #on notes page visit
    search = request.GET.get('search', '')  #if user searched for a note, get all notes that contain the search
    sort = request.GET.get('sort', 'dateCreated')   #if user is sorting, return notes in the order of the sort
    noteList = Note.objects.filter(owner=request.user).filter(
        Q(title__contains=search) | 
     Q(description__contains=search) | 
     Q(group__contains=search) | 
     Q(colour__contains=search)
     ).order_by(sort)   #order the notes

    return render(request, 'notesApp/notes.html', {'noteList': noteList})   #return the note info to the user


from .forms import NoteForm #import note from from forms.py

@login_required
def CreateNote(request):    #on new note page
    if request.method == 'POST':    #if they are making a post request
        form = NoteForm(request.POST)
        if form.is_valid(): #check it
            newNote = form.save(commit=False)
            newNote.owner = request.user    #set owner of note to current user
            newNote.save()  #save it
            return redirect('notes')    #redirec to notes page
    else:
        form = NoteForm()   #if not a post request, display the form
    return render(request, 'notesApp/noteForm.html', {'form': form })   #return form to user

@login_required
def EditNote(request, pk):  #on edit page
    note = get_object_or_404(Note, pk=pk)   #get the note otherwise raise a 404
    if note.owner != request.user:  #check if current user is note owner
        raise Http404("You can only edit your own notes.")
    
    if request.method == 'POST':    #if post request
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notesApp/noteForm.html', {'form': form })

@login_required
def DeleteNote(request, pk):    #on delete note page
    note = get_object_or_404(Note, pk=pk)   #get note otherwise return 404
    if note.owner != request.user:  #check if current user is owner
        raise Http404("You can only delete your own notes.")
    note.delete()   #delete the note

    return redirect('notes')    #return to notes page

from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def CreateUser(request):    #create user page
    if request.method == "POST":    #if post request
        form = SignUpForm(request.POST) #make post to server
        if form.is_valid(): #check if data is valid
            form.save() #save the new user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)   #create new user from inputs
            login(request, user)    #login as the user
            return redirect('notes')    #redirect to notes
    else:
        form = SignUpForm() #if not post, show form

    return render(request, 'notesApp/register.html', {'form': form})    #return form to user

from django.shortcuts import render_to_response
from django.template import RequestContext