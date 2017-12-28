from django.shortcuts import render, get_object_or_404

from . import models

def index(request):
    return render(request, 'tweet/index.html', {})


def tweet_detail(request, id):
    tweet = get_object_or_404(models.Tweet, id=id)
    return render(request, 'tweet/detail.html', {'tweet': tweet})


def tweet_list(request):
    return render(request, 'tweet/list.html', {})
