from django.conf.urls import url
from .views import FacturaOrdenDeTrabajoCreateView

urlpatterns = [
    url(r'^factura/orden_de_trabajo/(?P<pk>\d+)/$',FacturaOrdenDeTrabajoCreateView.as_view(),name='facturar'),
]
