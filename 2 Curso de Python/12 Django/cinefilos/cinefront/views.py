from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from cinefront.models import Pelicula, Director

# Create your views here.

# Sobre el contexto en las vistas: https://stackoverflow.com/questions/20957388/what-is-a-context-in-django

def index(request, inputPagination=None):
    """
    En esta vista se visualiza un listado de películas con los directores
    clicables.

    Se muestran 5 ítems paginados.
    """
    # Especificamos el template que vamos a devolver
    template = loader.get_template('cinefront/index.html')
    
    # Obtenemos un listado de las 5 primeras pelis en la BD

    if inputPagination != None and inputPagination >= 5:
        endRange        = inputPagination
        initialRange    = inputPagination - 5
        nextPage        = inputPagination + 5
        previousPage    = inputPagination - 5
    else:
        endRange        = 5
        initialRange    = 0
        nextPage        = 10
        previousPage    = '#'

    listaPelis = Pelicula.objects.filter(id__range=(initialRange + 1, endRange))

    # Generamos el diccionario (contexto en argot Django donde el template buscará las variables)
    contexto = {
        "listaPelis":    listaPelis,
        "initialRange":  initialRange,
        "nextPage":      nextPage,
        "previousPage":  previousPage,
    }

    return HttpResponse(template.render(contexto, request))

def pelicula(request, peliculaId):
    """
    Vista muestra el detalle de una película concreta.
    """

    # Plantilla
    template = loader.get_template('cinefront/pelicula.html')

    # Consulta a la BD
    listaPeli = Pelicula.objects.filter(id=peliculaId)

    # Contexto (Diccionario)
    contexto = {
        "listaPeli": listaPeli,
    }

    return HttpResponse(template.render(contexto, request))

def director(request, directorId):
    """
    En esta vista se muestra un detalle de un director concreto
    listando todas las películas en las que ha participado.
    """

    # Plantilla
    template = loader.get_template('cinefront/director.html')

    # Consulta a la BD
    listaDirector = Director.objects.filter(id=directorId)
    listaPelis = Pelicula.objects.filter(director_id=directorId)

    # Contexto

    contexto = {
        "listadirector": listaDirector,
        "listaPelis": listaPelis,
    }

    return HttpResponse(template.render(contexto, request))



def busqueda(request):
    """
    Busqueda simple

    Usando: https://learndjango.com/tutorials/django-search-tutorial
    """

    # Plantilla

    template = loader.get_template('cinefront/busqueda.html')

    # Obtenemos los parámetros del GET

    tabla   = request.GET.get("tabla")
    nombre  = request.GET.get("nombre")

    # Consulta a la BD
    if tabla == "pelicula":
        listaBusqueda = Pelicula.objects.filter(nombre__icontains=nombre)
    else:
        listaBusqueda = Director.objects.filter(nombre__icontains=nombre)

    # Contexto

    contexto = {
        "listaBusqueda": listaBusqueda,
    }

    return HttpResponse(template.render(contexto, request))