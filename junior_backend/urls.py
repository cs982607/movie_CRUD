from django.urls import path, include

urlpatterns = [
    path('movies', include('movie.urls')),
]
