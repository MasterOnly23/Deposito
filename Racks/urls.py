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
from Racks.views import index, Estantes, Penetrables, Suplementos, Psicotropicos,buscar, vencimientos, pallet,guardar_producto, nuevo_producto, vencimientosTodos

urlpatterns = [
    path('', index, name='index'),
    path('busqueda/', buscar, name='buscar'),
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
    path('estantes/E7/', Estantes.E7, name='E7'),
    path('estantes/E8/', Estantes.E8, name='E8'),
    path('estantes/E9/', Estantes.E9, name='E9'),
    path('estantes/E10/', Estantes.E10, name='E10'),

    #Penetrables
    path('penetrable/F1/', Penetrables.F1, name='F1'), 
    path('penetrable/F2/', Penetrables.F2, name='F2'),
    path('penetrable/F3/', Penetrables.F3, name='F3'),
    path('penetrable/F4/', Penetrables.F4, name='F4'),
    path('penetrable/F5/', Penetrables.F5, name='F5'),
    path('penetrable/F6/', Penetrables.F6, name='F6'),
    path('penetrable/F7/', Penetrables.F7, name='F7'),
    path('penetrable/F8/', Penetrables.F8, name='F8'),
    path('penetrable/F9/', Penetrables.F9, name='F9'),
    path('penetrable/F10/', Penetrables.F10, name='F10'),
    path('penetrable/F11/', Penetrables.F11, name='F11'),
    path('penetrable/F12/', Penetrables.F12, name='F12'),
    

    #pallets
    path('pallet/<str:ubicacion>/', pallet, name='pallet'),


    path('agregar/<str:ubicacion>/', nuevo_producto, name='nuevo_producto'),
    path('guardar/<str:ubicacion>/', guardar_producto, name='guardar_producto'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

