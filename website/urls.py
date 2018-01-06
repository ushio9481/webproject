from django.conf.urls import url
from . import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/$', views.BlogView.as_view(), name='blog'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^category/1$', views.CategoryView.as_view(), name='category'),
    url(r'^search/$', views.search, name='search'),
    url(r'^photo/$', views.photo, name='photo'),
]