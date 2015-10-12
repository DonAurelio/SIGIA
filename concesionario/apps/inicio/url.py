# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from .views import Login, Logout, OlvidoLogin


urlpatterns = [
	url(r'^$', Login.as_view(), name='login'),
    url(r'^inicio/login/$', Login.as_view(), name='login'),
    url(r'^inicio/logout/$', Logout.as_view(), name='logout'),
    url(r'^inicio/olvido_login/$', OlvidoLogin.as_view(), name='olvido_login'),
]
