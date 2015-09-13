from django.conf.urls import include, url
from django.contrib import admin
from .views import hola_mundo

urlpatterns = [
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', hola_mundo),
    url(r'^inicio/$', hola_mundo),
]
