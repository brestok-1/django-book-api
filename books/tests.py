from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from books.models import Book


# Create your tests here.
class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='maks', password='Maksim135799')
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author=user
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'A good title')
        self.assertEqual(self.book.subtitle, 'An excellent subtitle')

    def test_book_listview(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'excellent subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')
