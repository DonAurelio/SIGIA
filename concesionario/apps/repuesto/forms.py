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



class RepuestoSucursalCreateView(CreateView):
	model = SucursalRepuesto
	template_name  = 'repuesto/inventario_list.html'
	fields = ['sucursal','repuesto','cantidad','habilitado']

	def get_context_data(self,**kwargs):
		context = super(RepuestoSucursalCreateView,self).get_context_data(**kwargs)
		context['repuestos'] =  Repuesto.objects.all()
		context['form_mode'] = 'create'
		context['sucursal'] = Sucursal.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('repuesto:listar-repuestos-sucursal',kwargs={'pk':self.kwargs['pk']})


class RepuestoSucursalUpdateView(UpdateView):
	model = SucursalRepuesto
	template_name  = 'repuesto/inventario_list.html'
	fields = ['sucursal','repuesto','cantidad','habilitado']

	def get_context_data(self,**kwargs):
		context = super(RepuestoSucursalUpdateView,self).get_context_data(**kwargs)
		# Vehiculos que no estan en la sucursal con id = self.kwargs['pk']
		#context['vehiculos']  = Vehiculo.objects.exclude(sucursalvehiculo__sucursal__id=self.kwargs['pk'])
		context['repuestos'] =  Repuesto.objects.all()
		context['form_mode'] = 'update'
		sucursal_repuesto = SucursalRepuesto.objects.get(id=self.kwargs['pk'])
		sucursal_id = sucursal_repuesto.sucursal_id
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		context['sucursal_repuestos'] = SucursalRepuesto.objects.filter(sucursal=sucursal)

		return context

	def get_success_url(self):
		sucursal_repuesto = SucursalRepuesto.objects.get(id=self.kwargs['pk'])
		return reverse_lazy('repuesto:listar-repuestos-sucursal',kwargs={'pk':sucursal_repuesto.sucursal.id})
