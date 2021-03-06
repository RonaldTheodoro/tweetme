from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from rest_framework import status

from .. import models, views


User = get_user_model()


class TweetDetailViewTest(TestCase):
    url = reverse('tweet:detail', kwargs={'id': 1})

    def setUp(self):
        user_data = {'username': 'ronaldtheodoro', 'password': 'asdf1234'}
        user = User.objects.create_user(**user_data)
        self.client.login(**user_data)
        self.tweet = models.Tweet.objects.create(
            content='My First Tweet',
            user=user
        )
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'tweet/tweet_detail.html')

    def test_context(self):
        self.assertIn('tweet', self.response.context)

    def test_is_instance_of(self):
        self.assertIsInstance(self.response.context['tweet'], models.Tweet)
    
    def test_equal(self):
        self.assertEqual(self.response.context['tweet'], self.tweet)

    def test_absolute_url(self):
        self.assertEqual(self.url, self.tweet.get_absolute_url())

    def test_template_has_detail_link(self):
        self.assertContains(self.response, self.tweet.get_absolute_url())

    def test_template_has_edit_link(self):
        self.assertContains(
            self.response,
            reverse('tweet:update', kwargs={'id': self.tweet.id})
        )
    
    def test_template_has_delete_link(self):
        self.assertContains(
            self.response,
            reverse('tweet:delete', kwargs={'pk': self.tweet.id})
        )


class TweetDetailFailViewTest(TestCase):
    url = reverse('tweet:detail', kwargs={'id': 1})

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(status.HTTP_404_NOT_FOUND, self.response.status_code)
