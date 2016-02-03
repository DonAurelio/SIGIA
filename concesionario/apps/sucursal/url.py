# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import SucursalAjaxCreateView
from .forms import SucursalAjaxUpdateView
from .views import SucursalesListView

urlpatterns = [

    url(r'^sucursal/crear$', SucursalAjaxCreateView.as_view(), name='crear'),
    url(r'^sucursal/(?P<pk>\d+)/$', SucursalAjaxUpdateView.as_view(), name='actualizar'), 
    url(r'^sucursales/$', SucursalesListView.as_view(), name='listar'),
    
]
