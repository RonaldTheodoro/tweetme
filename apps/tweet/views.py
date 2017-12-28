from django.views import generic
from django.shortcuts import get_list_or_404, get_object_or_404, render

from . import models


def index(request):
    return render(request, 'tweet/index.html', {})


class TweetDetail(generic.DetailView):
    
    def get_object(self, queryset=None):
        return get_object_or_404(models.Tweet, id=1)


class TweetList(generic.ListView):
    queryset = get_list_or_404(models.Tweet)
