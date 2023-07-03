from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
#Libreria que permite mostrar respuestas en formato http
from rest_framework import viewsets
from .serializers import CategoriaSerializer

def index(request):
    return HttpResponse("Hola Escuela de Futbol...")

def categorias(request):
    post_nombre=request.POST.get("nombre")
    if post_nombre:
        categoria=Categoria(nombre_categoria=post_nombre)
        categoria.save()
    categorias=Categoria.objects.all()
    return render(request,"form_categorias.html",{"categorias": categorias})

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer
