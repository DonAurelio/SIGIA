# -*- encoding: utf-8 -*-



from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext, loader, Context, Template
from .forms import UserCreateForm
from .forms import CrearEmpleado
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.contrib.auth.models import User
from apps.empleado.models import Empleado

#Se vaalida el formulario y se guarda
def nuevo_usuario(request):
	first_name = last_name = username = password = email =''
	if request.POST:
		user_form = UserCreateForm(request.POST)
		if user_form.is_valid():
			usuario = User(first_name=request.POST['first_name'],last_name=request.POST['last_name'], username=request.POST['username'], email=request.POST['email'])
			usuario.set_password(request.POST['password1'])
			usuario.save()
			#se direcciona a crear empleado para los datos adicionales
			return HttpResponseRedirect('crearEmpleado')
	else:
		user_form = UserCreateForm()

	dictionary = {
		'user_form': user_form,
		'page_title': 'Aplicacion - Register',
		'body_class': 'register',
	}
	#se direcciona de nuevo a crear usuario si se encuentran errores
	return render_to_response("empleado/includes/crear.html", dictionary, context_instance=RequestContext(request))

 
#Se valida  y guarda el formulario
def nuevo_empleado(request):
	user = identificacion = direccion = telefono = salario = imagen = tipo = ''
	if request.POST:
		form = CrearEmpleado(request.POST)
		if  form.is_valid():
			form.save()
			return HttpResponseRedirect('crear')
	else:
		form = CrearEmpleado()

	dictionary = {
		'form': form,
	}
	#se direcciona de nuevo a crearEmpleado si se encuentran errores en el formulario
	return render_to_response("empleado/includes/crearEmpleado.html", dictionary, context_instance=RequestContext(request))
 