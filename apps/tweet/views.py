from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import exceptions
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from . import forms, models


def index(request):
    return render(request, 'tweet/index.html', {})


class TweetDetail(generic.DetailView):

    def get_object(self):
        return get_object_or_404(models.Tweet, id=self.kwargs.get('id'))


class TweetUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    form_class = forms.TweetForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise exceptions.PermissionDenied()
        return super(TweetUpdate, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(models.Tweet, id=self.kwargs.get('id'))


class TweetList(generic.ListView):
    queryset = models.Tweet.objects.all()
    template_name = 'tweet/tweet_list.html'


class TweetCreate(LoginRequiredMixin, generic.CreateView):
    form_class = forms.TweetForm
    template_name = 'tweet/tweet_form.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreate, self).form_valid(form)


class TweetDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Tweet
    success_url = reverse_lazy('tweet:list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise exceptions.PermissionDenied()
        return super(TweetDelete, self).dispatch(request, *args, **kwargs)