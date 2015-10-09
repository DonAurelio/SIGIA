from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib import messages
from .forms import UserUpdateForm
from .forms import EmpleadoUpdateForm

#Permite mostrar el perfil de usuario
class Perfil(TemplateView):
	template_name = 'cuenta/perfil.html'

#Permite modificar los datos de la cuenta de usuario (User, Empelado)
class Editar(TemplateView):

	#Cuando la peticion es de tipo GET se muestra el formulario para actualizar los datos
	def get(self,request,*args,**kwargs):
		#Se instancian los formularios con la informacion actual del usuario y empleado
		user_form = UserUpdateForm(instance=request.user)
		empleado_form = EmpleadoUpdateForm(instance=request.user.empleado)

		#Se colocan los formularios en el contexto
		context = {'user_form':user_form,'empleado_form':empleado_form}
		return render_to_response('cuenta/editar.html',context,context_instance=RequestContext(request))

	#Cuando la peticion es de tipo POST es porque se ha hecho un submit en el formulario diligenciado
	def post(self,request,*args,**kwargs):
		#Se obtiene la informacion del formulario diligenciado en el template del request.POST
		user_form = UserUpdateForm(request.POST,instance=request.user)
		empleado_form = EmpleadoUpdateForm(request.POST,instance=request.user.empleado)

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
			user_form = UserUpdateForm(instance=request.user)
			empleado_form = EmpleadoUpdateForm(instance=request.user.empleado)
			#user_form = UserUpdateForm(request.POST)
			#empleado_form = EmpleadoUpdateForm(request.POST)
			#Se coloca un mensaje en el request, para que sea mostrado en el template 
			messages.error(request,'Hay errores en algun campo')
			#Se colocan los formularios en el contexto
			context = {'user_form':user_form,'empleado_form':empleado_form}
			return render_to_response('cuenta/editar.html',context,context_instance=RequestContext(request))




