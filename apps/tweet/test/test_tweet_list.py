from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from rest_framework import status

from .. import models, views


User = get_user_model()


class TweetListViewTest(TestCase):
    url = reverse('tweet:list')

    def setUp(self):
        user = User.objects.create_user(username='ronaldtheodoro')
        self.tweets = [
            models.Tweet.objects.create(content='My First Tweet', user=user),
            models.Tweet.objects.create(content='My Second Tweet', user=user),
            models.Tweet.objects.create(content='My Third Tweet', user=user),
        ]
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'tweet/tweet_list.html')

    def test_context(self):
        self.assertIn('object_list', self.response.context)

    def test_is_instance_of(self):
        with self.subTest():
            for tweet in self.response.context['object_list']:
                self.assertIsInstance(tweet, models.Tweet)
    
    def test_equal(self):
        self.assertEqual(self.response.context['object_list'], self.tweets)

    def test_count(self):
        self.assertEqual(len(self.response.context['object_list']), 3)

    def test_absolute_url(self):
        with self.subTest():
            for tweet in self.tweets:
                self.assertEqual(
                    reverse('tweet:detail', kwargs={'id': tweet.id}),
                    tweet.get_absolute_url()
                )

    def test_template_has_detail_link(self):
        with self.subTest():
            for tweet in self.tweets:
                self.assertContains(self.response, tweet.get_absolute_url())
