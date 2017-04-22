from django.conf.urls import url
from .views import detail, index, category, archives


app_name = 'blog'
urlpatterns = [
    url(r'^index', index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', category, name='category'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', archives, name='archives'),

]