from django.test import TestCase

from .. import models

class TweetModelTest(TestCase):

    def setUp(self):
        self.tweet = models.Tweet.objects.create(content='My first tweet')

    def test_exists(self):
        self.assertTrue(models.Tweet.objects.exists())
