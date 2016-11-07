from __future__ import unicode_literals
from django.db import models

class Note(models.Model):
    lang1 = models.CharField(max_length=200)
    lang2 = models.CharField(max_length=200)
    date = models.DateTimeField('date')

    def __str__(self):
        return '%s, %s' % (self.lang1, self.lang2)