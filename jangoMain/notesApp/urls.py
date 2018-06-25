from django.urls import path

from . import views

urlpatterns = [     #define urls used in the note app accross the site
    path('', views.Index, name='index'),
    path('notes', views.Notes, name='notes'),
    path('note/<int:pk>', views.EditNote, name='editNote'),
    path('note/<int:pk>/delete', views.DeleteNote, name='deleteNote'),
    path('notes/add', views.CreateNote, name='noteCreate'),
    path('register', views.CreateUser, name='register'),
]
