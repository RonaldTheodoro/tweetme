from django.conf import settings
from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel


class Tweet(TimeStampedModel):
    content = models.CharField('content', max_length=140)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tweet',
        verbose_name='user'
    )

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse('tweet:detail', kwargs={'id': self.id})
