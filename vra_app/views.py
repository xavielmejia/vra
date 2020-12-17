from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Seguros, Coberturas, CoberturaSeguros
from django.template import loader
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
import sys

# Create your views here.

# Home template
def index(request):
    lista_seguro = Seguros.objects.all()
    context = {
        'lista_seguro': lista_seguro,
    }
    return render(request, 'index.html', context)


def detail(request, seguro_id):
    try:
        seguro = Seguros.objects.get(pk=seguro_id)
    except Seguros.DoesNotExist:
        raise Http404('Seguro no existe')
    # ALTERNATIVA al try
    # seguros = get_object_or_404(Seguros, pk=seguro_id)
    return render(request, 'detail.html', {'seguro': seguro})


### seguros

# table where you see 
def see_seguros(request):
    seguros = Seguros.objects.all()
    return render(request, 'see_seguros.html', {'seguros':seguros})


# Insert seguro in Seguros Model
def create_seguro(request):
    
    if request.method == 'POST':
        # crear nuevo seguro
        if request.POST.get('nombre') and request.POST.get('estado'):
            seguros=Seguros()
            seguros.nombre = request.POST.get('nombre').upper()
            seguros.estado = request.POST.get('estado')
            seguros.color = request.POST.get('color')

            seguros.prima_minima = set_prima_minima(request)

            # Catch error associated with constraint, the constraint for nombre is UNIQUE
            try:
                seguros.save()
            except IntegrityError as e:
                # Mensaje de error en caso de que ocurra un error de integridad
                messages.error(request, 'Seguro ya existe')
                return render(request, 'new_seguro.html')

            # Mensaje de exito cuando el seguro es ingresado
            messages.success(request, 'Seguro insertado')

            return HttpResponseRedirect(reverse('vra:see_seguros'))
        messages.error(request, 'Algo salió mal, Seguro no ha sido ingresado')
        return render(request, 'new_seguro.html')
    else:
        messages.error(request, 'Algo salió mal, Seguro no ha sido ingresado')
        return render(request, 'new_seguro.html')


def new_seguro(request):
    # Ir a la vista para agregar nuevos seguros
    return render(request, 'new_seguro.html')

def delete_seguro(request, seguro_id):
    # Ir a la vista de eliminacion del seguro
    seguro = get_object_or_404(Seguros, pk=seguro_id)
    return render(request, 'delete_seguro.html', {'seguro':seguro})


def confirm_delete_seguro(request, seguro_id):
    # Eliminar seguro
    seguro = get_object_or_404(Seguros, pk=seguro_id)
    seguro.delete()
    return HttpResponseRedirect(reverse('vra:see_seguros'))


def update_seguro(request, seguro_id):
    # Ir a la vista de actualizacion
    seguro = get_object_or_404(Seguros, pk=seguro_id)
    return render(request, 'update_seguro.html', {'seguro':seguro})

def confirm_update_seguro(request, seguro_id):
    # Actualizar los datos de los seguros
    seguro = get_object_or_404(Seguros, pk=seguro_id)
    if request.method == 'POST':

        # Actualizar los valores de los seguros
        seguro.estado = request.POST.get('estado')
        seguro.color = request.POST.get('color')
        seguro.prima_minima = set_prima_minima(request)

        seguro.save()

        # Mensaje de actualizacio exitosa
        messages.success(request, 'Seguro actualizado')
        return HttpResponseRedirect(reverse('vra:see_seguros'))
    
    return render(request, 'update_seguro.html')


def set_prima_minima(request):
    # validate that prima_minima field is not in black if it is the case insert zero
    if not request.POST.get('prima_minima'):
        return 0
    else:
        return request.POST.get('prima_minima')



### Coberturas

def new_cobertura(request):
    # Ir a la vista donde se crean los seguros
    seguros = Seguros.objects.all()
    return render(request, 'coberturas/new_cobertura.html', {'seguros':seguros})


def create_cobertura(request):
    if request.method == 'POST':
        # crear nuevo seguro
        if request.POST.get('descripcion') and request.POST.get('estado'):
            coberturas=Coberturas()
            coberturas.descripcion = request.POST.get('descripcion').upper()
            coberturas.estado = request.POST.get('estado')

            # Catch error associated with constraint, the constraint for nombre is UNIQUE
            try:
                coberturas.save()
            except IntegrityError as e:
                # Mensaje de error en caso de que ocurra un error de integridad
                messages.error(request, 'Cobertura ya existe')
                return render(request, 'coberturas/new_cobertura.html')
            except:
                error = sys.exc_info()
                messages.error(request, 'Ha ocurrido el error {}: {}'.format(str(error[0]), str(error[1])))
                return render(request, 'coberturas/new_cobertura.html')


            # Mensaje de exito cuando el seguro es ingresado
            messages.success(request, 'Cobertura insertada')

            return HttpResponseRedirect(reverse('vra:see_seguros'))
        messages.error(request, 'La descripción es obligatoria, no puede estar en blanco')
        return render(request, 'coberturas/new_cobertura.html')
    else:
        messages.error(request, 'Algo salió mal, Seguro no ha sido ingresado')
        return render(request, 'coberturas/new_cobertura.html')
