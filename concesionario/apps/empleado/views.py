# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext, loader, Context, Template
from .forms import UserCreateForm
from .forms import EmpleadoCreateForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from apps.empleado.models import Empleado
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User

class EmpleadoCreateView(TemplateView):

	def get(self,request,*args,**kwargs):
		nombre_seccion = "Crear Empleado"
		user_form = UserCreateForm(),'Informacion del Usuario'
		empleado_form = EmpleadoCreateForm(),'Informacion del Empleado'
		forms = [user_form,empleado_form]
		context = {'section_name':nombre_seccion,'forms':forms}
		return render_to_response(
			'empleado/empleado_form.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		user_form = UserCreateForm(request.POST)
		empleado_form = EmpleadoCreateForm(request.POST,request.FILES)

		if user_form.is_valid() and empleado_form.is_valid():
			new_user = user_form.save()
			new_empleado = empleado_form.save()
			new_empleado.user = new_user
			new_empleado.save()
			messages.info(request,'Nuevo empleado creado')
			context = {}
			return render_to_response(
				"cuenta/perfil.html",
				context,
				RequestContext(request))

		nombre_seccion = "Crear Empleado"
		user_form = (UserCreateForm(request.POST),'Informacion del Usuario')
		empleado_form = (EmpleadoCreateForm(request.POST),'Informacion del Empleado')
		forms = [user_form,empleado_form]
		messages.error(request,'Hay errores en algun campo')
		context = {'section_name':nombre_seccion,'forms':forms}
		return render_to_response(
			'empleado/empleado_form.html',
			context,
			context_instance=RequestContext(request))

#Actualizar Empleado
class EmpleadoUpdateView(TemplateView):

	def get(self, request, *args, **kwargs):
		empleado = Empleado.objects.get(id=kwargs['pk'])
		user = User.objects.get(id=empleado.id)

		empleado_form = (EmpleadoCreateForm(instance=empleado), 'Informacion del Empleado')
		user_form = (UserCreateForm(instance=user), 'Informacion del Usuario')
		nombre_seccion = 'Editar Empleado'
		forms = [user_form, empleado_form]
		context = {'section_name':nombre_seccion, 'forms':forms}

		return render_to_response(
			'empleado/empleado_form.html', 
			context,
			context_instance=RequestContext(request))

	def post(sel, request, *args, **kwargs):
		empleado = Empleado.objects.get(id=kwargs['pk'])
		user = User.objects.get(id=empleado.id)

		empleado_form = EmpleadoCreateForm(request.POST, instance=empleado)
		user_form = UserCreateForm(request:POST, instance=user)

		if user_form.is_valid() and empleado_form.is_valid():
			empleado_form.save(commit=False)
			return HttpResponse(empleado_form.cleaned_data['identificacion'])
		else:
			empleado_form = (EmpleadoCreateForm(request.POST), 'Informacion del Empleado')
			nombre_seccion = 'Editar Empleado'
			forms = [empleado_form]
			context = {'section_name':nombre_seccion, 'forms':forms}

			return render_to_response(
				'empleado/empleado_form.html', 
				context,
				context_instance=RequestContext(request))
