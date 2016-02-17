# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .views import Validar

urlpatterns = [
	
	url(r'^validar/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<id>\d+)/', Validar.as_view(), name='validar'),


]
