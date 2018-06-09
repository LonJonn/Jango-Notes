import datetime

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Note(models.Model):
    colourChoices = (
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=50, help_text="Main description of your task")
    description = models.TextField(
        blank=True, null=True, help_text="Any additional information")
    colour = models.CharField(blank=True, null=True,
                              max_length=50, choices=colourChoices, help_text="Colour code the note")
    group = models.CharField(
        blank=True, null=True, max_length=50, help_text="Assign the note to a group")
    dateCreated = models.DateTimeField(
        auto_now_add=True, verbose_name='date created')
    dateDue = models.DateTimeField(
        blank=True, null=True, help_text="Set a reminder date", verbose_name='date due')

    class Meta:
        ordering = ["dateCreated"]

    def __str__(self):
        return self.title

    def clean(self):
        if self.dateDue is not None:
            if self.dateDue < timezone.now():
                raise ValidationError(
                    {"dateDue": "The due date cannot be in the past!"})
