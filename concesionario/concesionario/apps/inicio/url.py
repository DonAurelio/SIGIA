from django.conf.urls import include, url
from django.contrib import admin
from .views import Login, Logout

urlpatterns = [
	url(r'^$', Login.as_view(), name='login'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
]
