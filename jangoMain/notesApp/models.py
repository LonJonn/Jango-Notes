import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class Note(models.Model):
    colourChoices = (
        ('blue' ,'Blue'),
        ('red' ,'Red'),
        ('green' ,'Green'),
        ('yellow' ,'Yellow'),
    )
    owner = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    colour = models.CharField(blank=True, null=True, max_length=30, choices=colourChoices)
    subject = models.CharField(blank=True, null=True, max_length=30)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDue = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def isNew(self):
        return self.dateCreated >= timezone.now() - datetime.timedelta(days=2)

    def clean(self):
        if self.dateDue is not None:
            if self.dateDue < timezone.now():
                raise ValidationError({"dateDue":"The due date cannot be in the past!"})