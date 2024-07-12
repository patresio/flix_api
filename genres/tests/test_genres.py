import json

from django.test import Client, TestCase

from genres.models import Genre  # Assuming your Genre model is in 'genres' app


class GenreAPITests(TestCase):

    def test_get_genres(self):
        client = Client()
        response = client.get("/genres/")
        self.assertEqual(response.status_code, 200)  # Check for successful response

    def test_create_genre(self):
        client = Client()
        data = {"name": "Comedy"}
        response = client.post(
            "/genres/", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)  # Check for successful creation
        self.assertEqual(response.json()["name"], "Comedy")  # Verify the created genre

    def test_get_genre_by_id(self):
        genre = Genre.objects.create(name="Action")
        client = Client()
        response = client.get(f"/genres/{genre.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Action")

    def test_update_genre(self):
        genre = Genre.objects.create(name="Thriller")
        client = Client()
        data = {"name": "Thriller Updated"}
        response = client.put(
            f"/genres/{genre.id}/",
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Thriller Updated")

    def test_delete_genre(self):
        genre = Genre.objects.create(name="Horror")
        client = Client()
        response = client.delete(f"/genres/{genre.id}/")
        self.assertEqual(response.status_code, 204)  # Check for successful deletion
        self.assertFalse(
            Genre.objects.filter(id=genre.id).exists()
        )  # Verify genre is deleted
