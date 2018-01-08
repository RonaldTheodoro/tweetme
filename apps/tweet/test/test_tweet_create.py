from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from rest_framework import status

from .. import forms, models, views


User = get_user_model()


class TweetCreateGETViewTest(TestCase):
    url = reverse('tweet:create')

    def setUp(self):
        data = {'username':'ronaldtheodoro', 'password': 'asdf1234'}
        user = User.objects.create_user(**data)
        self.client.login(**data)
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'tweet/tweet_form.html')

    def test_context(self):
        self.assertIn('form', self.response.context)
