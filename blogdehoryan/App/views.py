from django.http import HttpResponse
from django.shortcuts import render

from App.forms import *
from App.models import *


# Create your views here.
#vamos acambiar inicio
def inicio(request):
    return render(request,"App/inicio.html")

# Creamos paginas para cada clase que utilizamos:  
def juegos(request):
    return render(request,"App/juegos.html")

def integrantes(request):
    return render(request, "App/integrantes.html")

def donadores(request):
    return render(request,"App/donadores.html")

def sugerencias(request):
    return render(request, "App/sugerencias.html")

#-----------------------------------------------------------------------------------------------------------------------------------

# CREACION CLASES FORMULARIOS:

def juegosformulario(request):
    if request.method == 'POST':
        miFormulario = JuegoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            juego = Juego(nombre=informacion['nombre'], categoria=informacion['categoria'], calificacion=informacion['calificacion'], resena=informacion['resena'])
            juego.save()
            return render(request, "App/inicio.html")

        #Si no viene por post lo configuramos para cuando llega por GET:
    else:
        miFormulario=JuegoFormulario()
    return render(request, "App/juegosFormulario.html", {"miFormulario":miFormulario})


def integrantesformulario(request):
    if request.method == 'POST':
        miFormulario = IntegranteFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data

            integrantes=Integrante(nombre=informacion['nombre'], apellido=informacion['apellido'], cargo=informacion['cargo'], email=informacion['email'])

            integrantes.save()
            return render(request, "App/inicio.html")

        #Si no viene por post lo configuramos para cuando llega por GET:
    else:
        miFormulario=IntegranteFormulario()
    return render(request, "App/integrantesFormulario.html", {"formulario":miFormulario})


def donadoresformulario(request):
    if request.method == 'POST':
        miFormulario = DonadorFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data

            donador=Donador(nombre=informacion['nombre'], nickname=informacion['nickname'], email=informacion['email'])
            donador.save()
            return render(request, "App/inicio.html")

        #Si no viene por post lo configuramos para cuando llega por GET:
    else:
        miFormulario=DonadorFormulario()
    return render(request, "App/donadoresFormulario.html", {"formulario":miFormulario})


def sugerenciasformulario(request):
    if request.method == 'POST':
        miFormulario = SugerenciaFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data

            sugerencia=Sugerencia(nombre=informacion['nombre'], categoria=informacion['categoria'])
            sugerencia.save()
            return render(request, "App/inicio.html")

        #Si no viene por post lo configuramos para cuando llega por GET:
    else:
        miFormulario=SugerenciaFormulario()
    return render(request, "App/sugerenciasFormulario.html", {"miFormulario":miFormulario})

# ----------------------------------------------------------------------------------------------------------------------------------
# BUSQUEDA CON FORM

def busquedaReview(request):
    return render(request, "App/busquedaReview.html")

def buscar(request):
    if request.GET['categoria']:
        categoria=request.GET['categoria']
        #Del modelo juego, filtrame los datos que tengan cierta categoria
        juegos=Juego.objects.filter(categoria__icontains=categoria)
        return render(request, 'App/resultadosBusqueda.html', {'juegos':juegos, 'categoria': categoria })

    else:
        respuesta="No se ingreso ninguna categoría analizada por el momento"
        return render(request, 'App/resultadosBusqueda.html', {'respuesta':respuesta})