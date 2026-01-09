from django.shortcuts import render


# import facut de mine
from django.http import HttpResponse

# Create your views here.
def hello_viewer(request):
    return HttpResponse("Hello from server!")

def produse_viewer(request, categorie):
    return HttpResponse(f"Categoria este: {categorie}")

lista_laptop = ["home", "office", "gaming"]

def laptop_viewer(request, categorie):
    if categorie in lista_laptop:
        return HttpResponse(f"Categoria de laptop-uri: {categorie}, a fost gasita!")
    return HttpResponse(f"Categoria de laptop-uri: {categorie}, nu exista!")