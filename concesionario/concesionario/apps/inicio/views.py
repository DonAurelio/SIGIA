from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from concesionario.apps.empleado.models import Empleado

# Create your views here.

class Login(TemplateView):

	#Cuando la peticion es tipo GET, se renderiza el template de login
	def get(self,request,*args,**kwargs):
		context = {}
		return render_to_response('inicio/login.html',context,context_instance=RequestContext(request))

	#Cunado la peticion es tipo POST se hace el proceso de login
	def post(self,request,*args,**kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')

		#Usando el la funcion authenticate, obtenemos el usuario que corresponde con los datos 
		#pasados como argumentos
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				#Redireccionamos a la pagina de perfil del usuario


				#Obtenemos el empleado que corresponde con el usuario logeado
				empleado = Empleado.objects.get(user_id=user.id)

				#Introducimos el empleado en el contexto para que pueda ser usado en el template
				context = {'empleado':empleado}
				#Retornamos una respuesta con el perfil del usuario
				return render_to_response('cuenta/empleado.html',context)
			else:
				context = {'messaje':'Su usuario no esta activo'}
		else:
			context = {'messaje':'Revise su usuario y clave'}

		return render_to_response('inicio/login.html',context,context_instance=RequestContext(request))

class Logout(TemplateView):

	def dispatch(self,request,*args,**kwargs):
		logout(request)
		context = {}
		return render_to_response('inicio/login.html',context)


