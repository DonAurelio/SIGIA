from django.conf.urls import include, url
from django.contrib import admin
from concesionario import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('concesionario.apps.inicio.url', namespace='inicio')),
    url(r'', include('concesionario.apps.cuenta.url', namespace='cuenta')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }), 

]
