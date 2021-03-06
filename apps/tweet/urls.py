from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'tweet'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.TweetDetail.as_view(), name='detail'),
    path('list/', views.TweetList.as_view(), name='list'),
    path('new/', views.TweetCreate.as_view(), name='create'),
    url(r'^(?P<id>\d+)/edit/$', views.TweetUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TweetDelete.as_view(), name='delete'),
]
