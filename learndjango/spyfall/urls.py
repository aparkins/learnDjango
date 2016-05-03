from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^random', views.random_card, name='Random Card'),
]
