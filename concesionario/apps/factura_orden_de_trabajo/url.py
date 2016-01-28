from django.conf.urls import url
from .forms import FacturaOrdenDeTrabajoCreateView
from .forms import FacturaOrdenDeTrabajoDetailView

urlpatterns = [
    #pk es la pirmarykey de la cotizacion, que es necesaria para crear la factura
    url(r'^facturar/orden_de_trabajo/(?P<pk>\d+)/$',FacturaOrdenDeTrabajoCreateView.as_view(),name='facturar'),
    url(r'^factura/orden_de_trabajo/detalle(?P<pk>\d+)/$',FacturaOrdenDeTrabajoDetailView.as_view(),name='detalle'),
]
