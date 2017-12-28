from django.shortcuts import render


def index(request):
    return render(request, 'tweet/index.html', {})


def tweet_detail(request, id):
    return render(request, 'tweet/detail.html', {})
