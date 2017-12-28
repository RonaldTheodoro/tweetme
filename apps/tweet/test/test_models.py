from django.contrib.auth import get_user_model
from django.test import TestCase

from .. import models


User = get_user_model()


class TweetModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='ronaldtheodoro')
        self.tweet = models.Tweet.objects.create(
            content='My first tweet',
            user=user
        )

    def test_exists(self):
        self.assertTrue(models.Tweet.objects.exists())
