from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'tweet'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.tweet_detail, name='detail'),
    path('list/', views.tweet_list, name='list'),
]
