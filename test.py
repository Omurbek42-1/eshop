from rest_framework.test import APITestCase
from rest_framework import status
from .models import Director, Movie, Review

class DirectorTests(APITestCase):
    def test_list_directors(self):
        response = self.client.get('/api/v1/directors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_director(self):
        response = self.client.post('/api/v1/directors/', {'name': 'New Director'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class MovieTests(APITestCase):
    def test_list_movies(self):
        response = self.client.get('/api/v1/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        response = self.client.post('/api/v1/movies/', {'title': 'New Movie'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReviewTests(APITestCase):
    def test_list_reviews(self):
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_review(self):
        response = self.client.post('/api/v1/reviews/', {'content': 'Great movie!'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
