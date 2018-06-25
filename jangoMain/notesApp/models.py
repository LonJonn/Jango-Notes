import datetime

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Note(models.Model):   #define note model for database and api access
    colourChoices = (   #choice of colours
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   #owner primary key to assign notes too
    title = models.CharField(   #title of note
        max_length=50, help_text="Main description of your task")
    description = models.TextField(     #optional description
        blank=True, null=True, help_text="Any additional information")
    colour = models.CharField(blank=True, null=True,    #option colours from colourChoice
                              max_length=50, choices=colourChoices, help_text="Colour code the note")
    group = models.CharField(   #option group
        blank=True, null=True, max_length=50, help_text="Assign the note to a group")
    dateCreated = models.DateTimeField(     #date created set from servers current date
        auto_now_add=True, verbose_name='date created')
    dateDue = models.DateTimeField(     #option date due set by user
        blank=True, null=True, help_text="Set a reminder date", verbose_name='date due')

    class Meta: #custom ordering of notes
        ordering = ["dateCreated"]

    def __str__(self):  #return title of note for clarity
        return self.title

    def clean(self):    #check for valid due date before submitting
        if self.dateDue is not None:
            if self.dateDue < timezone.now():
                raise ValidationError(
                    {"dateDue": "The due date cannot be in the past!"})
