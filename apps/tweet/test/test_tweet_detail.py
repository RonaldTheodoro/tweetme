from django.urls import resolve, reverse
from django.test import TestCase

from rest_framework import status

from .. import views

class TweetDetailViewTest(TestCase):
    url = reverse('tweet:detail', kwargs={'id': 1})

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'tweet/detail.html')

    def test_function(self):
        index = resolve(self.url)
        self.assertEqual(views.tweet_detail, index.func)
