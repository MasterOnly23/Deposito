"""ProyectoDeposito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Racks.views import index, Estantes, Penetrables, Suplementos, Psicotropicos, vencimientos, pallet,guardar_producto, nuevo_producto, vencimientosTodos

urlpatterns = [
    path('', index, name='index'),
    path('vencimientos/', vencimientos, name='vencimientos'),
    path('vencimientos/todos/', vencimientosTodos, name='vencimientos_todos'),
    path('estantes/', Estantes.estantes, name='estantes'),
    path('penetrables/', Penetrables.penetrables, name='penetrables'),
    path('suplementos/', Suplementos.suplementos, name='suplementos'),
    path('psicotropicos/', Psicotropicos.psicotropicos, name='psicotropicos'),

    #Estantes
    path('estantes/E1/', Estantes.E1, name='E1'),
    path('estantes/E2/', Estantes.E2, name='E2'),
    path('estantes/E3/', Estantes.E3, name='E3'),
    path('estantes/E4/', Estantes.E4, name='E4'),
    path('estantes/E5/', Estantes.E5, name='E5'),
    path('estantes/E6/', Estantes.E6, name='E6'),

    #pallets
    path('pallet/<str:ubicacion>/', pallet, name='pallet'),


    path('agregar/<str:ubicacion>/', nuevo_producto, name='nuevo_producto'),
    path('guardar/<str:ubicacion>/', guardar_producto, name='guardar_producto'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

