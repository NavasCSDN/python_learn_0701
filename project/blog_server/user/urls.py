from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'/(?P<username>[\w]{6,11})$', views.users, name='users')
]