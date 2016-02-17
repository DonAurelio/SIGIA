# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django import forms

from .models import Repuesto
from apps.sucursal.models import Sucursal
from apps.sucursal.models import SucursalRepuesto

import json

class CrearRepuesto(CreateView):
	model = Repuesto
	fields = ['nombre', 'precio', 'marca', 'clasificacion',
	'imagen', 'proveedor', 'descripcion']
	success_url = reverse_lazy('repuesto:listar')
	template_name = 'repuesto/form.html'

	def get_context_data(self,**kwargs):
		context = super(CreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Nuevo Repuesto'
		context['button_text'] = 'Crear'
		return context


class ActualizarRepuesto(UpdateView):
	model = Repuesto
	fields = ['nombre', 'precio', 'marca', 'clasificacion',
	'imagen', 'proveedor', 'descripcion']
	success_url = reverse_lazy('repuesto:listar')
	template_name = 'repuesto/form.html'

	def get_context_data(self,**kwargs):
		context = super(ActualizarRepuesto,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Repuesto'
		context['button_text'] = 'Actualizar'
		return context


class RepuestoSucursalCreateForm(forms.ModelForm):
	class Meta:
		model = SucursalRepuesto
		fields = ('sucursal','repuesto','cantidad','habilitado')


class RepuestoSucursalAjaxCreateView(TemplateView):

	def get(self,request,*args,**kwargs):

		sucursal_id = Sucursal.objects.get(id=kwargs['spk']).id
		repuesto_id = Repuesto.objects.get(id=kwargs['rpk']).id

		template = loader.get_template('includes/form.html')
		form = RepuestoSucursalCreateForm({
			'sucursal':sucursal_id,
			'repuesto':repuesto_id})

		context = {'form':form}
		html = template.render(context)
		response = {
			'status':True,
			'html':html
		}

		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')

	def post(self,request,*args,**kwargs):
		form = RepuestoSucursalCreateForm(request.POST)
		if form.is_valid():
			form.save()
			template = loader.get_template('repuesto/includes/inventario.html')
			repuestos = Repuesto.objects.all()
			sucursal = Sucursal.objects.get(id=kwargs['spk'])
			sucursal_repuestos = SucursalRepuesto.objects.get(sucursal=sucursal)
			context = {
				'repuestos':repuestos,
				'sucursal':sucursal,
				'sucursal_repuestos':sucursal_repuestos
			}

			html = template.render(context)
			response = {
				'status':True,
				'html':html
			}

			data = json.dumps(response)
			return HttpResponse(data,content_type='application/json')

		template = loader.get_template('includes/form.html')
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':False,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data, content_type='application/json')


class RepuestoSucursalAjaxUpdateView(TemplateView):

	def get(self,request,*args,**kwargs):

		sucursal_repuesto = SucursalRepuesto.objects.get(id=kwargs['pk'])
		template = loader.get_template('includes/form.html')
		form = RepuestoSucursalCreateForm(instance=sucursal_repuesto)
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':True,
			'html':html
		}

		data = json.dumps(response)
		return HttpResponse(data,content_type='application/json')

	def post(self,request,*args,**kwargs):
		sucursal_repuesto = SucursalRepuesto.objects.get(id=kwargs['pk'])
		form = RepuestoSucursalCreateForm(
			request.POST,
			instance=sucursal_repuesto)

		if form.is_valid():
			form.save()
			template = loader.get_template('repuesto/includes/inventario.html')
			template = loader.get_template('repuesto/includes/inventario.html')
			repuestos = Repuesto.objects.all()
			sucursal = Sucursal.objects.get(id=kwargs['spk'])
			sucursal_repuestos = SucursalRepuesto.objects.get(sucursal=sucursal)
			context = {
				'repuestos':repuestos,
				'sucursal':sucursal,
				'sucursal_repuestos':sucursal_repuestos
			}

			html = template.render(context)
			response = {
				'status':True,
				'html':html
			}

			data = json.dumps(response)
			return HttpResponse(data,content_type='application/json')

		template = loader.get_template('includes/form.html')
		context = {'form':form}
		html = template.render(context)
		response = {
			'status':False,
			'html':html
		}
		data = json.dumps(response)
		return HttpResponse(data, content_type='application/json')
