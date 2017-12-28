from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from django.test import TestCase

from rest_framework import status

from .. import views, models


User = get_user_model()


class TweetDetailViewTest(TestCase):
    url = reverse('tweet:detail', kwargs={'id': 1})

    def setUp(self):
        user = User.objects.create_user(username='ronaldtheodoro')
        self.tweet = models.Tweet.objects.create(
            content='My First Tweet',
            user=user
        )
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'tweet/detail.html')

    def test_function(self):
        index = resolve(self.url)
        self.assertEqual(views.tweet_detail, index.func)

    def test_context(self):
        self.assertIn('tweet', self.response.context)
        self.assertIsInstance(self.response.context['tweet'], models.Tweet)
        self.assertEqual(self.response.context['tweet'], self.tweet)
