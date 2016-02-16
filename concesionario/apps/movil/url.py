# -*- encoding: utf-8 -*-

from django.conf.urls import url

urlpatterns = [

	url(r'^', include(admin.site.urls)),


]
