from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from rest_framework import status

from .. import forms, models, views


User = get_user_model()


class TweetCreateViewTest(TestCase):
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


class TweetCreatePOSTViewTest(TestCase):
    url = reverse('tweet:create')

    def setUp(self):
        user_data = {'username':'ronaldtheodoro', 'password': 'asdf1234'}
        user = User.objects.create_user(**user_data)
        self.client.login(**user_data)
        self.response = self.client.post(
            self.url,
            data={'content': 'My Tweet'}
        )

    def test_redirect_to_detail_page(self):
        self.assertRedirects(
            self.response,
            reverse('tweet:detail', kwargs={'id': 1})
        )


class TweetCreateFailViewTest(TestCase):
    url = reverse('tweet:create')

    def setUp(self):
        self.response = self.client.get(self.url, follow=True)

    def test_redirect_to_login_page(self):
        """Unauthenticate user must be redirect to login view"""
        login_url = reverse('login')
        self.assertRedirects(self.response, f'{login_url}?next={self.url}')