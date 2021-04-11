from django.shortcuts import render
from django.http import HttpResponse 
from sightings.models import Squirrel


# Create your views here.
def map(request):
    sightings= Sighting.objects.all()[:100]
    context ={
            'sightings':sightings,
            }
    return render(request, 'tracker/map.html', context)