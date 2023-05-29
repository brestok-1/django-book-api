from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


class APITests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='user', password='Somepassword135799')
        cls.book = Book.objects.create(
            title='API',
            subtitle='Subtitle',
            author=user
        )

    def test_api_listview(self):
        response = self.client.get(reverse('book_list_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
