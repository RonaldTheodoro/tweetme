from django.test import TestCase
from django.urls import reverse, resolve

from rest_framework import status

from .. import views

class IndexViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('tweet:index'))

    def test_get(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'tweet/index.html')

    def test_function(self):
        index = resolve('/')
        self.assertEqual(views.index, index.func)