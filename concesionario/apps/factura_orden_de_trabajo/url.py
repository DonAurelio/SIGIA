from django.conf.urls import url
from .forms import FacturaOrdenDeTrabajoCreateView

urlpatterns = [
    #pk es la pirmarykey de la cotizacion, que es necesaria para crear la factura
    url(r'^factura/orden_de_trabajo/(?P<pk>\d+)/$',FacturaOrdenDeTrabajoCreateView.as_view(),name='facturar'),
]
