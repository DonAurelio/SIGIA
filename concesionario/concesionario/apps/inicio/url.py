from django.conf.urls import include, url
from django.contrib import admin
from .views import Inicio

urlpatterns = [
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Inicio.as_view()),
    
]
