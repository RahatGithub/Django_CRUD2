from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerEntry

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PlayerEntry(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            runs = form.cleaned_data['runs']
            wickets = form.cleaned_data['wickets']
            country = form.cleaned_data['country']
            franchise = form.cleaned_data['franchise']
            record = Player(first_name=f_name, last_name=l_name, runs=runs, wickets=wickets, country=country, franchise=franchise)
            record.save()
            form = PlayerEntry()
    else:
        form = PlayerEntry()

    players = Player.objects.all()  # Taking all objects/instaces of the Player model
    return render(request, 'main/index.html', {'form':form, 'players':players})


def deleteData(request, id):
    if request.method == 'POST':
        record = Player.objects.get(pk=id)
        record.delete()
        return redirect('/main')



def updateData(request, id):
    record = Player.objects.get(pk=id)
    if request.method == 'POST':
        form = PlayerEntry(request.POST, instance=record)  
        if form.is_valid():
            form.save() 
    else:
        form = PlayerEntry(instance=record)
    
    return render(request, 'main/update_data.html', {'form':form}) 