from django.shortcuts import render, redirect
from django.http import HttpResponse 

from .models import Squirrel
from .forms import SightingsForm


def main(request):
    return render(request, 'sighting/main.html')

def squirrel_add_new(request):
    if request.method == "POST":
        form = SightingsForm(request.POST)
        return render(request, 'sighting/main.html')
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
    return render(request,'sighting/edit.html',context)

def squirrel_update_existing(request,unique_id):
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
    return render(request, 'sighting/edit.html', context)


# Create your views here.
