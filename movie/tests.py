from django.test import TestCase, Client
from .models            import Movie


class MovieListTestCase(TestCase):
    def setUp(self):
        self.URL = '/movie'
        self.client = Client()

        self.DUMMY_NAME        = 'name'
        self.DUMMY_COUNTRY     = 'korea'
        self.DUMMY_MAIN_IMAGE  = 'image'
        self.DUMMY_DESCRIPTION = 'description'
        self.DUMMY_SHOW_TIME   = 100
        self.DUMMY_GENRE       = '코미디'
        self.DUMMY_DIRECTOR    = 'director'
        self.DUMMY_ACTOR       = 'actor'

        self.movie = Movie.objects.create(
            id          = 1,
            name        = self.DUMMY_NAME,
            country     = self.DUMMY_COUNTRY,
            main_image  = self.DUMMY_MAIN_IMAGE,
            description = self.DUMMY_DESCRIPTION,
            show_time   = self.DUMMY_SHOW_TIME,
            genre       = self.DUMMY_GENRE,
            director    = self.DUMMY_DIRECTOR,
            actor       = self.DUMMY_ACTOR
        )

    def tearsDown(self):
        pass

    def test_movie_get_success(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            'movies': [{
                'name'       : self.movie.name,
                'main_image' : self.movie.main_image,
            }]})

    def test_movie_get_fail(self):
        self.movie.delete()
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{'message':'NOT_EXIST_MOVIE'})

    def test_movie_post_success(self):
        request = {
            'name'        : self.movie.name,
            'main_image'  : self.movie.main_image,
            'country'     : self.movie.country,
            'description' : self.movie.description,
            'show_time'   : self.movie.show_time,
            'genre'       : self.movie.genre,
            'director'    : self.movie.director,
            'actor'       : self.movie.actor

        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'SUCCESS'})
        self.assertEqual(response.status_code, 200)


class MovieDetailTestCase(TestCase):
    def setUp(self):
        self.URL = '/movie/1'
        self.client = Client()

        self.DUMMY_NAME        = 'name'
        self.DUMMY_COUNTRY     = 'korea'
        self.DUMMY_MAIN_IMAGE  = 'image'
        self.DUMMY_DESCRIPTION = 'description'
        self.DUMMY_SHOW_TIME   = 100
        self.DUMMY_GENRE       = '코미디'
        self.DUMMY_DIRECTOR    = 'director'
        self.DUMMY_ACTOR       = 'actor'

        self.movie = Movie.objects.create(
            id          = 1,
            name        = self.DUMMY_NAME,
            country     = self.DUMMY_COUNTRY,
            main_image  = self.DUMMY_MAIN_IMAGE,
            description = self.DUMMY_DESCRIPTION,
            show_time   = self.DUMMY_SHOW_TIME,
            genre       = self.DUMMY_GENRE,
            director    = self.DUMMY_DIRECTOR,
            actor       = self.DUMMY_ACTOR
        )

    def tearsDown(self):
        pass

    def test_moviedetail_get_success(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            'movie_detail': {
                'name'        : self.movie.name,
                'main_image'  : self.movie.main_image,
                'country'     : self.movie.country,
                'description' : self.movie.description,
                'show_time'   : self.movie.show_time,
                'genre'       : self.movie.genre,
                'director'    : self.movie.director,
                'actor'       : self.movie.actor
                }})

    def test_moviedetail_get_fail(self):
        response = self.client.get('/movie/2000')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{'message':'NOT_EXIST_MOVIE'})

    def test_moviedetail_delete_success(self):

        response = self.client.delete(self.URL)
        self.assertEqual(response.json(),{'message':'SUCCESS'})
        self.assertEqual(response.status_code, 200)

    def test_moviedetail_delete_fail(self):

        response = self.client.delete('/movie/1000')
        self.assertEqual(response.json(),{'message':'NOT_EXIST_MOVIE'})
        self.assertEqual(response.status_code, 400)

    def test_moviedetail_put_success(self):
        request = {
            'name'        : '무비',
            'main_image'  : '이미지',
            'country'     : '한국',
            'description' : '설명',
            'show_time'   : 66,
            'genre'       : '장르',
            'director'    : '감독',
            'actor'       : '배우'
        }

        response = self.client.put(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'SUCCESS'})
        self.assertEqual(response.status_code, 200)

    def test_moviedetail_put_fail(self):
        request = {
            'name'        : '무비',
            'main_image'  : '이미지',
            'country'     : '한국',
            'description' : '설명',
            'show_time'   : 66,
            'genre'       : '장르',
            'director'    : '감독',
            'actor'       : '배우'
        }

        response = self.client.put('/movie/2', request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'NOT_EXIST_MOVIE'})
        self.assertEqual(response.status_code, 400)

