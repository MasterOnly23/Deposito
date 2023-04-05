from django.shortcuts import render


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from Racks.models import RacksFrente, Productos 
# Create your views here.


def index(request):

    return render(request, 'plano.html')


def penetrables(request):

    return render(request, 'penetrables.html')



def suplementos(request):

    return render(request, 'suplementos.html')