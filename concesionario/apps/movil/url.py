# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .views import Validar
from .views import OrdenDeTrabajoJSONList

urlpatterns = [
	
	url(r'^validar/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<id>\d+)/', Validar.as_view(), name='validar'),
	url(r'^ordenesdetrabajo/(?P<pk>\d+)/json/$',OrdenDeTrabajoJSONList.as_view(),name='ordenes'),

]
