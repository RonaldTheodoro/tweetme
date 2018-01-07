from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse
from django.views import generic

from . import forms, models


def index(request):
    return render(request, 'tweet/index.html', {})


class TweetDetail(generic.DetailView):

    def get_object(self):
        return get_object_or_404(models.Tweet, id=self.kwargs.get('id'))


class TweetUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    form_class = forms.TweetForm
    
    def get_object(self):
        return get_object_or_404(models.Tweet, id=self.kwargs.get('id'))


class TweetList(generic.ListView):
    queryset = models.Tweet.objects.all()
    template_name = 'tweet/tweet_list.html'


class TweetCreate(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    form_class = forms.TweetForm
    template_name = 'tweet/tweet_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreate, self).form_valid(form)
