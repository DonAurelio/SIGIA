from django.conf.urls import include, url
from django.contrib import admin
from .views import Login

urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
]
