from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


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
    colours = models.CharField(max_length=4, choices=colourChoices)
    subject = models.CharField(max_length=20)
    dateCreated = models.DateTimeField('date created')
    dateDue = models.DateTimeField('date due')

    def __str__(self):
        return self.title
