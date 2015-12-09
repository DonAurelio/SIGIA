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

		empleado_form = EmpleadoCreateForm(request.POST,request.FILES,instance=empleado)
		user_form = UserCreateForm(request.POST,request.FILES,instance=user)

		if user_form.is_valid() and empleado_form.is_valid():

			empleado.identificacion = empleado_form.cleaned_data['identificacion']
			empleado.direccion = empleado_form.cleaned_data['direccion']
			empleado.telefono = empleado_form.cleaned_data['telefono']
			empleado.salario = empleado_form.cleaned_data['salario']
			empleado.sucursal = empleado_form.cleaned_data['sucursal']
			empleado.imagen = empleado_form.cleaned_data['imagen']
			empleado.tipo = empleado_form.cleaned_data['tipo'] 
			empleado.habilitado = empleado_form.cleaned_data['habilitado']
			empleado.save()

			user.username = user_form.cleaned_data['username']
			user.first_name = user_form.cleaned_data['first_name']
			user.last_name = user_form.cleaned_data['last_name']
			user.email = user_form.cleaned_data['email']
			
			password1 = user_form.cleaned_data['password1']
			password2 = user_form.cleaned_data['password2']
			
			if password1 != "" and password2 != "":
				user.set_password(user_form.cleaned_data['password1'])
			
			user.save()

			messages.info(request,'Empleado modificado con exito')
			context = {}
			return render_to_response(
				'cuenta/perfil.html',
				context,
				context_instance=RequestContext(request))
		else:
			empleado_form = (EmpleadoCreateForm(request.POST,request.FILES), 'Informacion del Empleado')
			user_form = (UserCreateForm(instance=user), 'Informacion del Usuario')
			nombre_seccion = 'Editar Empleado'
			forms = [empleado_form]
			context = {'section_name':nombre_seccion, 'forms':forms}

			return render_to_response(
				'empleado/empleado_form.html', 
				context,
				context_instance=RequestContext(request))