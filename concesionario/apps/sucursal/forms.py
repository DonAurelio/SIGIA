# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.template import Context
from django import forms
from .models import Sucursal
import json

class SucursalCreateForm(forms.ModelForm):
	class Meta:
		model = Sucursal
		fields = ('nombre', 'direccion', 'telefono', 'ciudad','habilitado')


class SucursalAjaxCreateView(TemplateView):

	def get(self,request,*args,**kwargs):
		template = loader.get_template('sucursal/parciales/form.html')
		form = SucursalCreateForm()
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':True,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')

	
	def post(self,request,*args,**kwargs):
		form = SucursalCreateForm(request.POST)
		if form.is_valid():
			form.save()
			template = loader.get_template('sucursal/parciales/tabla.html')
			context = {'sucursales':Sucursal.objects.all()}
			html = template.render(context)
			response = {
				'status':True,
				'html':html
			}
			data = json.dumps(response)
			return HttpResponse(data,content_type='application/json')
		
		template = loader.get_template('sucursal/parciales/form.html')
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':False,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')
			

class SucursalAjaxUpdateView(TemplateView):

	def get(self,request,*args,**kwargs):
		template = loader.get_template('sucursal/parciales/form.html')
		sucursal = Sucursal.objects.get(id=kwargs['pk'])
		form = SucursalCreateForm(instance=sucursal)
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':True,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')

	
	def post(self,request,*args,**kwargs):
		sucursal = Sucursal.objects.get(id=kwargs['pk'])
		form = SucursalCreateForm(request.POST,instance=sucursal)
		if form.is_valid():
			form.save()
			template = loader.get_template('sucursal/parciales/tabla.html')
			context = {'sucursales':Sucursal.objects.all()}
			html = template.render(context)
			response = {
				'status':True,
				'html':html
			}
			data = json.dumps(response)
			return HttpResponse(data,content_type='application/json')
		
		template = loader.get_template('sucursal/parciales/form.html')
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':False,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')
