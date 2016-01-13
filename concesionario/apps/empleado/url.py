# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from . import views
from . import forms


urlpatterns = [
    url(r'^empleado/sucursal/crear/(?P<spk>\d+)/$', forms.EmpleadoCreateView.as_view(), name='crear'),
    url(r'^empleado/sucursal/actualizar/(?P<epk>\d+)/$', forms.EmpleadoUpdateView.as_view(), name='actualizar'),
    url(r'^empleado/sucursal/listado/(?P<spk>\d+)/$', views.EmpleadoListView.as_view(), name='listar-empleados-sucursal'),
]
