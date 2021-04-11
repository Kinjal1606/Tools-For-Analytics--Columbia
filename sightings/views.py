from django.shortcuts import render
from django.http import HttpResponse 
from sightings.models import Squirrel


# Create your views here.
def map(request):
    sightings= Squirrel.objects.all()[:100]
    context ={
            'sightings':sightings,
            }
    return render(request, 'sightings/map.html', context)
def list_sighting(request):
    listing = Squirrel.objects.all()
    context = {
            'sighting': listing,
        }
    return render(request, 'sightings/sightings.html',context)