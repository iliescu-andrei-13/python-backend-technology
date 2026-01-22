from django.shortcuts import render, redirect, get_object_or_404
# import facut de mine
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from viewer.models import Movie, WatchMovie
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from viewer.forms import RegisterProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


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


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    is_watched = False
    if request.user.is_authenticated:
        is_watched = WatchMovie.objects.filter(
            user = request.user,
            movie = movie
        ).exists()
    
    return render(request, 'movie.html', {'movie': movie,
                                          'is_watched': is_watched,
                                          })


@login_required
def toggle_wathed_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    watched_movie, created = WatchMovie.objects.get_or_create(
        user = request.user,
        movie = movie
    )
    
    # Exista in tabela, vrem sa-l stergem
    if not created:
        watched_movie.delete()
    
    # A fast adaugat/sters in/din tabela, facem refresh
    return redirect('spre_film', movie_id=movie.id)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie'
    

class MovieCreateView(CreateView):
    model = Movie
    template_name = "create_movie.html"
    fields = ["title", "year", "description"]
    success_url = reverse_lazy("home")


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "create_movie.html"
    fields = ["title", "year", "description"]
    success_url = reverse_lazy("home")


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "delete_movie.html"
    success_url = reverse_lazy("home")


def register_user(request):
    if request.method == "POST": # daca am trimis formularul completat
        form = RegisterProfileForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user) # NU este obligatoriu
            return redirect("home")
        
    else: # cand am intrat prima data pe register
        form = RegisterProfileForm()
        
    return render(request, "register.html", {"form_html": form})


class CustomLogInView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    
    
def logoout_view(request):
    logout(request)
    return redirect("home")
