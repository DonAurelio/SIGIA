# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from .forms import UserForm,EmpleadoForm
from .models import Empleado

class EmpleadoCreateView(TemplateView):

	def get(self,request,*args,**kwargs):
		nombre_seccion = "Crear Empleado"
		user_form = UserForm(),'Informacion del Usuario'
		empleado_form = EmpleadoForm(),'Informacion del Empleado'
		forms = [user_form,empleado_form]
		context = {'section_name':nombre_seccion,'forms':forms}
		return render_to_response(
			'empleado/empleado_form.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		user_form = UserForm(request.POST)
		empleado_form = EmpleadoForm(request.POST,request.FILES)

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
		user_form = (UserForm(request.POST),'Informacion del Usuario')
		empleado_form = (EmpleadoForm(request.POST),'Informacion del Empleado')
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

		empleado_form = (EmpleadoForm(instance=empleado), 'Informacion del Empleado')
		user_form = (UserForm(instance=user), 'Informacion del Usuario')
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

		empleado_form = EmpleadoForm(request.POST,request.FILES,instance=empleado)
		user_form = UserForm(request.POST,request.FILES,instance=user)

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

			#En caso de que el gerente este modificando su misma cuenta de empleado,
			#es necesario que vuelva a ser logeado con los nuevos datos username
			#y password 
			if user.id == request.user.id:
				user = authenticate(username=user.username,password=password1)
				if user is not None:
					if user.is_active:
						login(request,user)

			messages.info(request,'Empleado modificado con exito')
			context = {}
			return render_to_response(
				'cuenta/perfil.html',
				context,
				context_instance=RequestContext(request))
		else:
			empleado_form = (EmpleadoForm(request.POST,request.FILES), 'Informacion del Empleado')
			user_form = (UserForm(instance=user), 'Informacion del Usuario')
			nombre_seccion = 'Editar Empleado'
			forms = [user_form,empleado_form]
			context = {'section_name':nombre_seccion, 'forms':forms}

			return render_to_response(
				'empleado/empleado_form.html', 
				context,
				context_instance=RequestContext(request))

class EmpleadoListView(TemplateView):

	def get(self,request,*args,**kwargs):
		sucursal_id = kwargs['pk']
		empleados = Empleado.objects.filter(sucursal_id=sucursal_id)
		context = {'lista_empleados':empleados}
		return render_to_response(
			'empleado/empleado_list.html',
			context,
			RequestContext(request))