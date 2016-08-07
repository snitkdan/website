from django.conf.urls import url
from . import views

urlpatterns = [
    #/music/
    url(r'^$', views.index, name = 'index'),
    #/music/id e.g. /music/180
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')

]
