import datetime

from django.db import models
from django.utils import timezone

class Note(models.Model):
    colourChoices = (
        ('blue' ,'Blue'),
        ('red' ,'Red'),
        ('green' ,'Green'),
        ('yellow' ,'Yellow'),
    )
    owner = models.IntegerField()
    title = models.CharField(max_length=20)
    description = models.TextField()
    colour = models.CharField(max_length=20, choices=colourChoices)
    subject = models.CharField(max_length=20)
    dateCreated = models.DateTimeField('date created')
    dateDue = models.DateTimeField('date due')

    def __str__(self):
        return self.title

    def isNew(self):
        return self.dateCreated >= timezone.now() - datetime.timedelta(days=2)

