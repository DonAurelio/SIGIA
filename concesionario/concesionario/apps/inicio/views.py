from django.shortcuts import render 
from django.http import HttpResponse , HttpResponseRedirect
from django.template import Context
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from .models import VENDEDOR, GERENTE, JEFE_TALLER

class Inicio(TemplateView):
	template_name = 'inicio/inicio.html'

class PerfilGerente(TemplateView):
	template_name = 'inicio/perfil_gerente.html'

class PerfilJefeTaller(TemplateView):
	template_name = 'inicio/perfil_jefe_taller.html'

class PerfilVendedor(TemplateView):
	template_name = 'inicio/perfil_vendedor.html'

class IniciarSesion(TemplateView):
	
	def dispatch(self,request,*args,**kwargs):
		
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)

				if user.tipousuario == VENDEDOR:
					return HttpResponseRedirect('/perfil_vendedor/')
				elif user.tipousuario == GERENTE:
					return HttpResponseRedirect('/perfil_gerente/')
				elif user.tipousuario == JEFE_TALLER:
					return HttpResponseRedirect('/perfil_jefe_taller/')
			else:
				# Return a 'disabled account' error message
				pass
		else:
			# Return an 'invalid login' error message.
			pass
	





	
   
	


	



