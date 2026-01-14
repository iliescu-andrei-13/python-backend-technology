from django.shortcuts import render
# import facut de mine
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from viewer.models import Movie


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


def filme_viewer(request):
    nume_filme = request.GET.get('nume', '')
    return HttpResponse(f'Numele filmelor sunt {nume_filme}')


def not_found_404_view(request):
    return HttpResponseNotFound("Pagina nu a fost gasita")


handler404 = not_found_404_view

def show_homepage(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies_html': movies})


# 1. Un nou view cu un link dinamic (? -> filtrare)
# 2. Sa filtreze informatiile afisate in tabel
def filter_movies(request):
    year = request.GET.get('year', '')

    movies = Movie.objects.all()

    if year:
        movies = movies.filter(year=year)

    return render(request, 'home.html', {'movies_html': movies})
