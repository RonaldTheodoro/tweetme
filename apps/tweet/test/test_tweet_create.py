from django.test import TestCase
from django.urls import resolve, reverse

from rest_framework import status

from .. import models, views, forms


class TweetCreateViewTest(TestCase):
    url = reverse('tweet:create')

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'tweet/tweet_form.html')

    def test_context(self):
        self.assertIn('form', self.response.context)
