import json

from django.views import View
from django.http import JsonResponse

from .models import Movie

class MovieListView(View):
    def get(self, request):
        movie_list = Movie.objects.all()

        movies = [{
            'name'       : movie.name,
            'main_image' : movie.main_image
       }for movie in movie_list]

        if not movies:
            return JsonResponse({'message':'NOT_EXIST_MOVIE'}, status=404)
        return JsonResponse({"movies": movies}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        try :
           movie = Movie.objects.create(
                name        = data['name'],
                country     = data['country'],
                main_image  = data['main_image'],
                description = data['description'],
                show_time   = data['show_time'],
                genre       = data['genre'],
                director    = data['director'],
                actor       = data['actor']
            )
           return JsonResponse({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=404)

class MovieDetailView(View):
    def get(self, request, movie_id):
        try :
            movie = Movie.objects.get(id=movie_id)
            movie_detail = {
                'name'        : movie.name,
                'country'     : movie.country,
                'main_image'  : movie.main_image,
                'description' : movie.description,
                'show_time'   : movie.show_time,
                'genre'       : movie.genre,
                'director'    : movie.director,
                'actor'       : movie.actor,
                }
            return JsonResponse({'movie_detail':movie_detail}, status=200)
        except Movie.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_MOVIE'}, status=404)

    def delete(self, request, movie_id):
        try :
            movie    = Movie.objects.get(id=movie_id)
            movie.delete()

            return JsonResponse({'message':'SUCCESS'}, status=200)
        except Movie.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_MOVIE'}, status=404)

    def put(self, request, movie_id):
        try:
            data = json.loads(request.body)
            movie = Movie.objects.get(id=movie_id)

            if 'name' in data:
                movie.name        = data['name']
            if 'country' in data:
                movie.country     = data['country']
            if 'main_image' in data:
                movie.main_image  = data['main_image']
            if 'description' in data:
                movie.description = data['description']
            if 'show_time' in data:
                movie.show_time   = data['show_time']
            if 'genre' in data:
                movie.genre       = data['genre']
            if 'director' in data:
                movie.director    = data['director']
            if 'actor' in data:
                movie.actor       = data['actor']
            movie.save()

            return JsonResponse({'message':'SUCCESS'}, status=200)
        except Movie.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_MOVIE'}, status=404)
