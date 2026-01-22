from django.contrib import admin
from viewer.models import Movie, Actors, WatchMovie, Profile

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actors)
admin.site.register(WatchMovie)
admin.site.register(Profile)
