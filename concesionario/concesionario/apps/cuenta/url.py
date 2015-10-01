from django.conf.urls import include, url
from concesionario.apps.cuenta.views import Editar

urlpatterns = [
	
	url(r'^editar_perfil$', Editar.as_view(), name='editar'),
    
]