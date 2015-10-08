from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from .forms import UserUpdateForm
from .forms import EmpleadoUpdateForm

#Permite administrar la actualizacion de datos del perfil del empleado
class Editar(TemplateView):

	#Cuando la peticion de tipo GET se muestra el formulario para actualizar los datos
	def get(self,request,*args,**kwargs):
		#Se instancian los formularios con la informacion actual del usuario y empleado
		user_form = UserUpdateForm(instance=request.user)
		empleado_form = EmpleadoUpdateForm(instance=request.user.empleado)

		#Se colocan los formularios en el contexto
		context = {'user_form':user_form,'empleado_form':empleado_form}
		return render_to_response('cuenta/editar.html',context,context_instance=RequestContext(request))
