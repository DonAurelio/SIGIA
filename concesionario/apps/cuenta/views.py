# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import UserUpdateForm
from .forms import UserPasswordUpdateForm
from .forms import EmpleadoUpdateForm
from apps.empleado.models import Empleado

#Permite mostrar el perfil de usuario
class Perfil(TemplateView):
	template_name = 'cuenta/perfil.html'

#Permite modificar la contraseña del usuario
class EditarContrasenia(TemplateView):

	def get(self,request,*args,**kwargs):
		user_password_update_form = UserPasswordUpdateForm(user=request.user)
		context = {'user_password_update_form':user_password_update_form}
		return render_to_response('cuenta/editar_contrasenia.html',context,context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):

		user_password_update_form = UserPasswordUpdateForm(user=request.user,data=request.POST)

		if user_password_update_form.is_valid():
			user_password_update_form.save()
			return HttpResponseRedirect(reverse('inicio:login'))
		else:
			messages.error(request,'Hay errores en algun campo')
			context = {'user_password_update_form':user_password_update_form}
			return render_to_response('cuenta/editar_contrasenia.html',context,context_instance=RequestContext(request))
			


#Permite modificar los datos de la cuenta de usuario (User, Empelado)
class Editar(TemplateView):

	#Cuando la peticion es de tipo GET se muestra el formulario para actualizar los datos
	def get(self,request,*args,**kwargs):
		#Se instancian los formularios con la informacion actual del usuario y empleado
		user_form = UserUpdateForm(instance=request.user)
		empleado_form = EmpleadoUpdateForm(instance=request.user.empleado)

		#Se colocan los formularios en el contexto
		context = {
		'user_form':user_form,
		'empleado_form':empleado_form
		}
		return render_to_response('form.html',context,context_instance=RequestContext(request))

	#Cuando la peticion es de tipo POST es porque se ha hecho un submit en el formulario diligenciado
	def post(self,request,*args,**kwargs):
		#Se obtiene la informacion del formulario diligenciado en el template del request.POST
		user_form = UserUpdateForm(request.POST,instance=request.user)
		
		#Se obtienen los datos de empleado del usuario a modificar 
		#junto con los archivos que se van a actualizar
		empleado_form = EmpleadoUpdateForm(request.POST,request.FILES,instance=request.user.empleado)
		
		#Se verifica si los formularios fueron diligenciados correctamente
		#Antes de guardar un formulario es obligatorio que se ejecute primero el metodo is_valid()
		#debido a que la ejecucion de este metodo activa el metodo save() de cada formulario
		if user_form.is_valid() and empleado_form.is_valid():
			user_form.save()
			empleado_form.save()

			#Se coloca un mensaje en el request, para que sea mostrado en el template 
			messages.info(request,'Tu cuenta ha sido modificada')
			context = {}
			return render_to_response('cuenta/perfil.html',context,context_instance=RequestContext(request))
		else:
			#En caso de que haya algun error, se vuelve a mostrar el formulario con los errores
			user_form = UserUpdateForm(request.POST,instance=request.user)
			empleado_form = EmpleadoUpdateForm(request.POST,instance=request.user.empleado)
			#Se coloca un mensaje en el request, para que sea mostrado en el template 
			messages.error(request,'Hay errores en algun campo')
			#Se colocan los formularios en el contexto
			context = {
			'user_form':user_form,
			'empleado_form':empleado_form
			}
			return render_to_response('cuenta/editar.html',context,context_instance=RequestContext(request))




