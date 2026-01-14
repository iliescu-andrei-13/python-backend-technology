"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
# import facut de mine
# from viewer.views import hello_viewer, produse_viewer, laptop_viewer
from viewer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_homepage, name='home'),
    path('filter/', views.filter_movies),
    
    path('hello/', views.hello_viewer),
    path('produse/<categorie>/', views.produse_viewer),
    path('laptop/<categorie>/', views.laptop_viewer),
    path('filme/', views.filme_viewer),
]

# Exercitiu:
# 1. Creare de url nou cu pattern
# 2. Functia de view, sa verifice daca valoarea trimisa se afla intr-o  lista
# 3. Fuctia returneaza "DA", daca elementul este in lista, altfel "NU"
