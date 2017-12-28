from django.views import generic
from django.shortcuts import get_list_or_404, get_object_or_404, render

from . import models


def index(request):
    return render(request, 'tweet/index.html', {})


class TweetDetail(generic.DetailView):
    template_name = 'tweet/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(models.Tweet, id=1)

def tweet_detail(request, id):
    tweet = get_object_or_404(models.Tweet, id=id)
    return render(request, 'tweet/detail.html', {'tweet': tweet})


class TweetList(generic.ListView):
    queryset = get_list_or_404(models.Tweet)
    template_name = 'tweet/list.html'

def tweet_list(request):
    tweets = get_list_or_404(models.Tweet)
    return render(request, 'tweet/list.html', {'tweets': tweets})
