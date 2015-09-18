from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.template import Context, RequestContext
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
	#template_name = 'calendario.html'

class IniciarSesion(TemplateView):
	
	def dispatch(self,request,*args,**kwargs):
		
		username = request.POST.get('username')
		password = request.POST.get('password')

		print username

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
				context = {'error':True}
				return render_to_response('inicio/inicio.html',context,context_instance=RequestContext(request))
				
		else:
			context = {'error':True}
			return render_to_response('inicio/inicio.html',context,context_instance=RequestContext(request))
	





	
   
	


	



