from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello', views.index, name='index'),
    url(r'^foobar', views.foobar, name='foobar'),
]
