from django.db import models

from model_utils.models import TimeStampedModel

class Tweet(TimeStampedModel):
    content = models.CharField('content', max_length=140)

    def __str__(self):
        return str(self.content)
