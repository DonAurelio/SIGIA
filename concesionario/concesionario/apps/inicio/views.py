from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Context
from django.views.generic import TemplateView 

class Inicio(TemplateView):
	template_name = 'inicio/inicio.html'


