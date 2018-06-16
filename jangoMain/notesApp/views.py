from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import NewNoteForm


# class notes(LoginRequiredMixin, generic.ListView):
#     model = Note
#     template_name = 'notesApp/notes.html'

#     def get_queryset(self):
#         return Note.objects.filter(owner = self.request.user)

# class editNote(LoginRequiredMixin, generic.DetailView):
#     model = Note
#     template_name = 'notesApp/editNote.html'


def index(request):
    notesCount = Note.objects.all().count()
    numUsers = User.objects.all().count()

    return render(request, 'notesApp/index.html', {'numUsers': numUsers, 'notesCount': notesCount})

@login_required
def notes(request):
    noteList = Note.objects.filter(owner = request.user)
    notesCount = noteList.count()

    return render(request, 'notesApp/notes.html', {'noteList': noteList, 'notesCount': notesCount})

@login_required
def editNote(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.owner.username != request.user.username:
        raise Http404("You can only edit your own notes.")
    
    return render(request, 'notesApp/editNote.html', {'note': note})


# class noteCreate(CreateView):
#     model = Note
#     fields = ['owner', 'title', 'description', 'colour', 'group', 'dateDue']
#     success_url = reverse_lazy('notes')


def noteCreate(request):
    if request.method == 'POST':
        form = NewNoteForm(request.POST or None)
        if form.is_valid():
            newNote = form.save(commit=False)
            newNote.owner = request.user
            newNote.save()
            return redirect('notes')
    else:
        form = NewNoteForm()
    return render(request, 'notesApp/newNote.html', {'form': form })
