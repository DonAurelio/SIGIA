# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .views import ProveedorListView
from .forms import ProveedorCreateView, ProveedorUpdateView

urlpatterns = [
	url(r'^proveedor/crear/$',ProveedorCreateView.as_view(), name='crear'),
	url(r'^proveedor/(?P<pk>\d+)/$', ProveedorUpdateView.as_view(), name='actualizar'),
	url(r'^proveedores/$', ProveedorListView.as_view(), name='listar'),
]
