from django.shortcuts import render
from datetime import datetime

from django.http import JsonResponse

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from Racks.models import  *

from .forms import ProductosForm

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from django.contrib import messages
# Create your views here.





def index(request):
    suplementos = Suplemento.objects.all()
    penetrables = Penetrable.objects.all()
    psicotropicos = Psicotropico.objects.all()
    estanterias = Estanteria.objects.all()

    ubicacionesSuplementos = {}
    ubicacionesPenetrables = {}
    ubicacionesPsicotropicos = {}
    ubicacionesEstanterias = {}
    
    for suplemento in suplementos:
        ubicacionesSuplementos[suplemento.ubicacion] = suplemento.ocupacion

    for penetrable in penetrables:
        ubicacionesPenetrables[penetrable.ubicacion] = penetrable.ocupacion

    for psicotropico in psicotropicos:
        ubicacionesPsicotropicos[psicotropico.ubicacion] = psicotropico.ocupacion

    for estanteria in estanterias:
        ubicacionesEstanterias[estanteria.ubicacion] = estanteria.ocupacion

    ubicaciones = {'ubicacionesSuplementos':ubicacionesSuplementos, 
                   'ubicacionesPenetrables':ubicacionesPenetrables, 
                   'ubicacionesPsicotropicos':ubicacionesPsicotropicos, 
                   'ubicacionesEstanterias':ubicacionesEstanterias}


    return render(request, 'planoP2.html', ubicaciones)


def buscar(request):

    opcion = request.GET.get("opcion")
    query = request.GET.get("query")

    try:
        if opcion and query:
            if opcion == "Producto":
                articulo = Productos.objects.filter(articulo__icontains=query).distinct().order_by("articulo")
                return render(request, 'busqueda.html', {"articulos":articulo})
            
            elif opcion == "Cantidad":
                articulo = Productos.objects.filter(cantidad__icontains=query).distinct().order_by("-cantidad")
                return render(request, 'busqueda.html', {"articulos":articulo})
            
            elif opcion == "Lote":
                articulo = Productos.objects.filter(lote__icontains=query).distinct().order_by("articulo")
                return render(request, 'busqueda.html', {"articulos":articulo})
            
            elif opcion == "Mueble":
                articulo = Productos.objects.filter(mueble__icontains=query).distinct().order_by("articulo")
                return render(request, 'busqueda.html', {"articulos":articulo})
            
        else:
            messages.warning(request, "Sin Resultados")
            return render(request, 'busqueda.html')


    
    except Exception as e:
        logFecha = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
        logErrorFile = 'Racks/log_error/keyslog_{}.txt'.format(logFecha)
        with open (logErrorFile, 'a') as log_file:
            log_file.write("Ha ocurrido un error con la búsqueda index: " + str(e))
        





class Estantes:

    def estantes(request):
        estanterias = Estanteria.objects.all()
        ubicacionesEstanterias = {}

        for estanteria in estanterias:
            ubicacionesEstanterias[estanteria.ubicacion] = estanteria.ocupacion
        ubicaciones = {'ubicacionesEstanterias':ubicacionesEstanterias}

        return render(request, 'Estantes/estantes.html', ubicaciones)

    def E1(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E1')
        ubicacionesE1 = {}
        for pallet in pallets:
            ubicacionesE1[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE1': ubicacionesE1}

        return render(request, 'Estantes/E1.html', contexto)
    

    def E2(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E2')
        ubicacionesE2 = {}
        for pallet in pallets:
            ubicacionesE2[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE2': ubicacionesE2}

        return render(request, 'Estantes/E2.html', contexto)
    
    def E3(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E3')
        ubicacionesE3 = {}
        for pallet in pallets:
            ubicacionesE3[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE3': ubicacionesE3}

        return render(request, 'Estantes/E3.html', contexto)
    
    def E4(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E4')
        ubicacionesE4 = {}
        for pallet in pallets:
            ubicacionesE4[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE4': ubicacionesE4}

        return render(request, 'Estantes/E4.html', contexto)
    
    def E5(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E5')
        ubicacionesE5 = {}
        for pallet in pallets:
            ubicacionesE5[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE5': ubicacionesE5}

        return render(request, 'Estantes/E5.html', contexto)
    
    def E6(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E6')
        ubicacionesE6 = {}
        for pallet in pallets:
            ubicacionesE6[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE6': ubicacionesE6}

        return render(request, 'Estantes/E6.html', contexto)
    
    def E7(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E7')
        ubicacionesE7 = {}
        for pallet in pallets:
            ubicacionesE7[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE7': ubicacionesE7}

        return render(request, 'Estantes/E7.html', contexto)
    
    def E8(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E8')
        ubicacionesE8 = {}
        for pallet in pallets:
            ubicacionesE8[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE8': ubicacionesE8}

        return render(request, 'Estantes/E8.html', contexto)
    
    def E9(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E9')
        ubicacionesE9 = {}
        for pallet in pallets:
            ubicacionesE9[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE9': ubicacionesE9}

        return render(request, 'Estantes/E9.html', contexto)
    
    def E10(request):
        pallets = Estanteria.objects.filter(ubicacion__startswith='E10')
        ubicacionesE10 = {}
        for pallet in pallets:
            ubicacionesE10[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesE10': ubicacionesE10}

        return render(request, 'Estantes/E10.html', contexto)
    

class Penetrables:

    def penetrables(request):
        penetrables = Penetrable.objects.all()
        ubicacionesPenetrables = {}

        for penetrable in penetrables:
            ubicacionesPenetrables[penetrable.ubicacion] = penetrable.ocupacion
        ubicaciones = {'ubicacionesPenetrables':ubicacionesPenetrables}

        return render(request, 'Penetrables/penetrables.html', ubicaciones)

    def F1(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F1')
        ubicacionesF1 = {}
        for pallet in pallets:
            ubicacionesF1[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF1': ubicacionesF1}

        return render(request, 'Penetrables/F1.html', contexto)
    
    def F2(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F2')
        ubicacionesF2 = {}
        for pallet in pallets:
            ubicacionesF2[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF2': ubicacionesF2}

        return render(request, 'Penetrables/F2.html', contexto)
    
    def F3(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F3')
        ubicacionesF3 = {}
        for pallet in pallets:
            ubicacionesF3[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF1': ubicacionesF3}

        return render(request, 'Penetrables/F3.html', contexto)
    
    def F4(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F4')
        ubicacionesF4 = {}
        for pallet in pallets:
            ubicacionesF4[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF4': ubicacionesF4}

        return render(request, 'Penetrables/F4.html', contexto)
    
    def F5(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F5')
        ubicacionesF5 = {}
        for pallet in pallets:
            ubicacionesF5[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF5': ubicacionesF5}

        return render(request, 'Penetrables/F5.html', contexto)
    
    def F6(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F6')
        ubicacionesF6 = {}
        for pallet in pallets:
            ubicacionesF6[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF6': ubicacionesF6}

        return render(request, 'Penetrables/F6.html', contexto)
    
    def F7(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F7')
        ubicacionesF7 = {}
        for pallet in pallets:
            ubicacionesF7[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF7': ubicacionesF7}

        return render(request, 'Penetrables/F7.html', contexto)
    
    def F8(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F8')
        ubicacionesF8 = {}
        for pallet in pallets:
            ubicacionesF8[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF8': ubicacionesF8}

        return render(request, 'Penetrables/F8.html', contexto)
    
    def F9(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F9')
        ubicacionesF9 = {}
        for pallet in pallets:
            ubicacionesF9[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF9': ubicacionesF9}

        return render(request, 'Penetrables/F9.html', contexto)
    
    def F10(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F10')
        ubicacionesF10 = {}
        for pallet in pallets:
            ubicacionesF10[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF10': ubicacionesF10}

        return render(request, 'Penetrables/F10.html', contexto)
    
    def F11(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F11')
        ubicacionesF11 = {}
        for pallet in pallets:
            ubicacionesF11[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF11': ubicacionesF11}

        return render(request, 'Penetrables/F11.html', contexto)
    
    def F12(request):
        pallets = Penetrable.objects.filter(ubicacion__startswith='F12')
        ubicacionesF12 = {}
        for pallet in pallets:
            ubicacionesF12[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesF12': ubicacionesF12}

        return render(request, 'Penetrables/F12.html', contexto)


class Suplementos:

    def suplementos(request):
        suplementos = Suplemento.objects.all()
        ubicacionesSuplementos = {}

        for suplemento in suplementos:
            ubicacionesSuplementos[suplemento.ubicacion] = suplemento.ocupacion
        ubicaciones = {'ubicacionesSuplementos':ubicacionesSuplementos}

        return render(request, 'Suplementos/suplementos.html', ubicaciones)
    
    
    def S1(request):
        pallets = Suplemento.objects.filter(ubicacion__startswith='S1')
        ubicacionesS1 = {}
        for pallet in pallets:
            ubicacionesS1[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesS1': ubicacionesS1}

        return render(request, 'Suplementos/S1.html', contexto)
    
    def S2(request):
        pallets = Suplemento.objects.filter(ubicacion__startswith='S2')
        ubicacionesS2 = {}
        for pallet in pallets:
            ubicacionesS2[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesS2': ubicacionesS2}

        return render(request, 'Suplementos/S2.html', contexto)
    

class Psicotropicos:

    def psicotropicos(request):
        psicotropicos = Psicotropico.objects.all()
        ubicacionesPsicotropicos = {}

        for psicotropico in psicotropicos:
            ubicacionesPsicotropicos[psicotropico.ubicacion] = psicotropico.ocupacion
        ubicaciones = {'ubicacionesPsicotropicos':ubicacionesPsicotropicos}

        return render(request, 'Psicotropicos/psicotropicos.html', ubicaciones)
    
    
    def P1(request):
        pallets = Psicotropico.objects.filter(ubicacion__startswith='P1')
        ubicacionesP1 = {}
        for pallet in pallets:
            ubicacionesP1[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesP1': ubicacionesP1}

        return render(request, 'Estantes/P1.html', contexto)
    
    def P2(request):
        pallets = Psicotropico.objects.filter(ubicacion__startswith='P2')
        ubicacionesP2 = {}
        for pallet in pallets:
            ubicacionesP2[pallet.ubicacion] = pallet.ocupacion
        contexto ={'ubicacionesP2': ubicacionesP2}

        return render(request, 'Estantes/P2.html', contexto)

def pallet(request, ubicacion):
    print(ubicacion)
    productos = Productos.objects.filter(Q(ubicacionF=ubicacion) | Q(ubicacionE=ubicacion) | Q(ubicacionP=ubicacion) | Q(ubicacionS=ubicacion)) 
    contexto = {'productos':productos,'ubicacion':ubicacion}
    return render(request, 'Pallets/pallet.html', contexto)


#FORMULARIOS

def nuevo_producto(request,ubicacion):
    form = ProductosForm(initial={'ubicacion':ubicacion})
    # form.fields['ubicacion'].widget.attrs['disabled']= True
    
    return render(request, 'Formularios/agregar.html', {'form': form, 'ubicacion':ubicacion})

def guardar_producto(request, ubicacion):
    if request.method == 'POST':
        form = ProductosForm(request.POST, request.FILES,initial={'ubicacion':ubicacion})
        if form.is_valid():
            form.save()
            return redirect(f'/pallet/{ubicacion}')
    else:
        form = ProductosForm(initial={'ubicacion':ubicacion})
    return render(request, 'Formularios/agregar.html', {'form': form})


#FORMULARIOS

def vencimientos(request):

    productos = Productos.objects.all().order_by('-fecha_vencimiento')[:6]

    return render(request, 'vencimientos2.html', {'productos':productos})

def vencimientosTodos(request):

    productos = Productos.objects.all().order_by('-fecha_vencimiento')

    return render(request, 'vencimientos2.html', {'productos':productos})



