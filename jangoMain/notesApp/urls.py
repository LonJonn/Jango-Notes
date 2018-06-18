from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('notes', views.Notes, name='notes'),
    path('note/<int:pk>', views.EditNote, name='editNote'),
    path('note/<int:pk>/delete', views.DeleteNote, name='deleteNote'),
    path('notes/add', views.CreateNote, name='noteCreate'),
    path('register', views.CreateUser, name='register'),
]