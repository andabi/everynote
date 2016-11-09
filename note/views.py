from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core import serializers

from .models import Note

# TODO pagination
def index(request):
    max_count = 100
    notes = Note.objects.order_by('date')[:max_count]
    notes_as_json = serializers.serialize('json', notes, fields=('lang1','lang2','date'))
    return HttpResponse(notes_as_json, content_type='json')