
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.http.response import JsonResponse
from django.db.models import Avg, Max, Min, Count
from .models import Squirrel
from .forms import SightingsForm


def main(request):
    return render(request, 'sighting/main.html')

def squirrel_add_new(request):
    if request.method == "POST":
        form = SightingsForm(request.POST)
        #return render(request, 'sighting/main.html')
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
        else:
            return JsonResponse({'errors': form.errors}, status= 400)
        
    else:
        form = SightingsForm()
        context ={
                'form':form,
                }
    return render(request,'sightings/add.html',context)

def squirrel_update_existing(request, unique_id):
    squirrel= Squirrel.objects.get(unique_id=unique_id)
    if request.method =='POST': 
        form = SightingsForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
        else: 
            return JsonResponse({'errors': form.errors}, status= 400)
    else:
        form = SightingsForm(instance=squirrel)
        context ={
            'form':form,
                }
    return render(request, 'sightings/edit.html', context)


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
            'sightings': listing,
        }
    return render(request, 'sightings/sightings.html',context)

def squirrel_stats(request): 
    AM = 0 
    PM = 0
    ADULT = 0
    JUVENILE = 0 
    GREY = 0 
    CINNAMON = 0 
    BLACK = 0 
    GROUND_PLANE = 0 
    ABOVE_GROUND = 0 
    TOTAL=0

    for s in Squirrel.objects.all():
        TOTAL += 1
        if s.shift == 'AM':
            AM += 1
        if s.shift == 'PM':
            PM += 1 
        if s.age == 'Adult':
            ADULT += 1 
        if s.age == 'Juvenile':
            JUVENILE += 1 
        if s.fur_color == 'Grey':
            GREY += 1 
        if s.fur_color == 'Cinnamon':
            CINNAMON += 1 
        if s.fur_color == 'Black':
            BLACK += 1 
        if s.location == 'Ground Plane':
            GROUND_PLANE +=1 
        if s.location == 'Above Ground':
            ABOVE_GROUND += 1
    LATITUDE = Squirrel.objects.all().aggregate(minimum=Min('lat'),maximum=Max('lat'))
    LONGITUDE = Squirrel.objects.all().aggregate(minimum=Min('lon'),maximum=Max('lon'))
    ADULT=round(ADULT*100/ (ADULT+JUVENILE), 2)
    JUVENILE=round(100-ADULT, 2)
    context = {
            'TOTAL':TOTAL, 
            'AM':AM,
            'PM':PM, 
            'LATITUDE':LATITUDE,
            'LONGITUDE':LONGITUDE,
            'ADULT':ADULT,
            'JUVENILE':JUVENILE, 
            'GREY':GREY ,
            'CINNAMON':CINNAMON,
            'BLACK':BLACK ,
            'GROUND_PLANE':GROUND_PLANE,
            'ABOVE_GROUND':ABOVE_GROUND,
            }

    return render(request, 'sightings/stats.html', context) 




