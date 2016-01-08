# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import SucursalCreateView
from .forms import SucursalUpdateView
from .views import SucursalesListView

urlpatterns = [

    url(r'^sucursal/crear$', SucursalCreateView.as_view(), name='crear'),
    url(r'^sucursal/(?P<pk>\d+)/$', SucursalUpdateView.as_view(), name='actualizar'), 
    url(r'^sucursales/$', SucursalesListView.as_view(), name='listar'),
    
]
