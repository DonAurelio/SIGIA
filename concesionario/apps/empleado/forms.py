# -*- coding: utf-8 -*-
from django import forms
from models import *
from django.forms.extras.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse

from .models import Empleado 
from apps.sucursal.models import Sucursal
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    username = forms.CharField(label='Nombre de Usuario')
    email = forms.EmailField(label='Correo',required=True)
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput,required=False)
    
    class Meta:
        model = User
        fields = ( "username", "email", "first_name", "last_name")

class EmpleadoForm(forms.ModelForm): 

	identificacion = forms.CharField(label='Numero de Identificación')
	direccion = forms.CharField(label='Dirección')
	telefono = forms.CharField(label='Teléfono')
	salario= forms.CharField(label='Salario',required=True)
	 
	class Meta:
		model = Empleado 
		fields = ['identificacion', 'direccion', 'telefono',
		'salario','sucursal','imagen', 'tipo','habilitado' ] 

class EmpleadoCreateView(TemplateView):
	"""Crea un empleado dada una sucursal."""

	def get(self,request,*args,**kwargs):
		"""Despliega el formulario de creacion de 
		usuario y empleado para una sucursal.
		"""

		sucursal = Sucursal.objects.get(id=kwargs['spk'])
		
		user_form = UserForm()
		empleado_form = EmpleadoForm( initial={'sucursal':sucursal.id} )
		
		forms = [user_form,empleado_form]
		context = {
		'section_title':'Nuevo Empleado',
		'button_text':'Crear',
		'sucursal':sucursal,
		'user_form':user_form,
		'empleado_form':empleado_form }
		
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
			 
			messages.info(request,'Nuevo empleado creado con exito')
					
			url = reverse(
				'empleado:listar-empleados-sucursal', 
				kwargs={'spk': new_empleado.sucursal.id})

			return HttpResponseRedirect(url)
			

		sucursal = Sucursal.objects.get(id=kwargs['spk'])
		user_form = UserForm(request.POST)
		empleado_form = EmpleadoForm(request.POST)
		
		
		messages.error(request,'Hay errores en algun campo, revise el formulario')
		
		context = {
		'section_title':'Nuevo Empleado',
		'sucursal':sucursal,
		'user_form':user_form,
		'empleado_form':empleado_form }
		
		return render_to_response(
			'empleado/empleado_form.html',
			context,
			context_instance=RequestContext(request))


class EmpleadoUpdateView(TemplateView):

	def get(self, request, *args, **kwargs):
		
		empleado = Empleado.objects.get(id=kwargs['epk'])
		sucursal = Sucursal.objects.get(id=empleado.sucursal.id)
		user = empleado.user

		empleado_form = EmpleadoForm(instance=empleado)
		user_form = UserForm(instance=user)
		
		context = {
		'section_title':'Actualizar Empleado',
		'sucursal':sucursal,
		'user_form':user_form,
		'empleado_form':empleado_form }

		return render_to_response(
			'empleado/empleado_form.html', 
			context,
			context_instance=RequestContext(request))

	def post(sel, request, *args, **kwargs):
		empleado = Empleado.objects.get(id=kwargs['epk'])
		sucursal = Sucursal.objects.get(id=empleado.sucursal.id)
		user = empleado.user

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
			return HttpResponseRedirect(reverse('cuenta:perfil'))
		
		else:
			empleado_form = EmpleadoForm(request.POST,request.FILES)
			user_form = UserForm(instance=user)
			
			context = {
			'section_title':'Actualizar Empleado',
			'sucursal':sucursal,
			'user_form':user_form,
			'empleado_form':empleado_form }

			return render_to_response(
				'empleado/empleado_form.html', 
				context,
				context_instance=RequestContext(request))