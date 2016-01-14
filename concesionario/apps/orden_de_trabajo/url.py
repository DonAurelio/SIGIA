# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .forms import OrdenDeTrabajoCreateView
from .forms import OrdenDeTrabajoUpdateView

urlpatterns = [
	url(r'^orden_de_trabajo/crear/$',OrdenDeTrabajoCreateView.as_view(),name='crear'),
	url(r'^orden_de_trabajo/(?P<pk>\d+)/$',OrdenDeTrabajoUpdateView.as_view(),name='actualizar'),
]