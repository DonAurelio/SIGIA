# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.template import loader
from django.template import Context
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django import forms

from .models import Vehiculo
from apps.sucursal.models import Sucursal
from apps.sucursal.models import SucursalVehiculo

import json
 

 
class VehiculoCreateView(CreateView):
	model = Vehiculo
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio']
	

	def get_context_data(self,**kwargs):
		context = super(VehiculoCreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Nuevo Vehiculo'
		context['button_text'] = 'Crear'
		return context

	def get_success_url(self):
		messages.info(self.request,"El vehiculo ha sido creado con exito")
		return reverse_lazy('vehiculo:listar-vehiculos')


class VehiculoUpdateView(UpdateView):
	model = Vehiculo 
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio']
	success_url = reverse_lazy('vehiculo:listar-vehiculos')

	def get_context_data(self,**kwargs):
		context = super(VehiculoUpdateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Vehiculo'
		context['button_text'] = 'Actualizar'
		return context

	def get_success_url(self):
		messages.info(self.request,"El vehiculo ha sido actualizado con exito")
		return reverse_lazy('vehiculo:listar-vehiculos')


class VehiculoSucursalCreateForm(forms.ModelForm):
	
	class Meta:
		model = SucursalVehiculo
		fields = ('vehiculo','sucursal','color','cantidad','habilitado')


class VehiculoSucursalAjaxCreateView(TemplateView):

	
	def get(self,request,*args,**kwargs):

		sucursal = Sucursal.objects.get(id=kwargs['spk']).id
		vehiculo = Vehiculo.objects.get(id=kwargs['vpk']).id

		template = loader.get_template('parciales/form.html')
		form = VehiculoSucursalCreateForm({'sucursal':sucursal,'vehiculo':vehiculo})
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':True,
			'html':html
		}

		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')

	def post(self,request,*args,**kwargs):
		form = VehiculoSucursalCreateForm(request.POST)
		if form.is_valid():
			form.save()
			template = loader.get_template('vehiculo/parciales/inventario.html')
			vehiculos = Vehiculo.objects.all()
			sucursal = Sucursal.objects.get(id=kwargs['spk'])
			sucursal_vehiculos = SucursalVehiculo.objects.filter(sucursal=sucursal)
			context = {
				'vehiculos':vehiculos,
				'sucursal':sucursal,
				'sucursal_vehiculos':sucursal_vehiculos
			}
			html = template.render(context)
			response = {
				'status':True,
				'html':html
			}
			data = json.dumps(response)
			return HttpResponse(data,content_type='application/json')
		
		template = loader.get_template('parciales/form.html')
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':False,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data, content_type='application/json')


class VehiculoSucursalAjaxUpdateView(TemplateView):

	
	def get(self,request,*args,**kwargs):

		sucursal_vehiculo = SucursalVehiculo.objects.get(id=kwargs['pk'])
		
		template = loader.get_template('parciales/form.html')
		form = VehiculoSucursalCreateForm(instance=sucursal_vehiculo)
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':True,
			'html':html
		}

		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')

	def post(self,request,*args,**kwargs):
		sucursal_vehiculo = SucursalVehiculo.objects.get(id=kwargs['pk'])
		form = VehiculoSucursalCreateForm(request.POST,instance=sucursal_vehiculo)
		if form.is_valid():
			form.save()
			template = loader.get_template('vehiculo/parciales/inventario.html')
			vehiculos = Vehiculo.objects.all()
			sucursal = sucursal_vehiculo.sucursal
			sucursal_vehiculos = SucursalVehiculo.objects.filter(sucursal=sucursal)
			context = {
				'vehiculos':vehiculos,
				'sucursal':sucursal,
				'sucursal_vehiculos':sucursal_vehiculos
			}
			html = template.render(context)
			response = {
				'status':True,
				'html':html
			}
			data = json.dumps(response)
			return HttpResponse(data,content_type='application/json')
		
		template = loader.get_template('parciales/form.html')
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':False,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data, content_type='application/json')