from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from concesionario.apps.cuenta.models import VENDEDOR,JEFE_TALLER,GERENTE 


class IniciarSesion(TemplateView):

	template_name = 'inicio/inicio.html'

	def get(self,request,*args,**kwargs):
		return render_to_response(self.template_name,{},context_instance=RequestContext(request))
		

	def post(self,request,*args,**kwargs):
		
		username = request.POST.get('username')
		password = request.POST.get('password')

		print username

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)

				if user.is_staff and user.is_superuser:
					return HttpResponseRedirect(reverse_lazy('admin:index'))
				elif user.tipousuario == VENDEDOR:
					return HttpResponseRedirect('cuenta/vendedor/')
					
				elif user.tipousuario == GERENTE:
					return HttpResponseRedirect('cuenta/gerente/')
					
				elif user.tipousuario == JEFE_TALLER:
					return HttpResponseRedirect('cuenta/jefe_taller/')
			else:
				context = {'error':True}
				return render_to_response(self.template_name,context,context_instance=RequestContext(request))
				
		else:
			context = {'error':True}
			return render_to_response(self.template_name,context,context_instance=RequestContext(request))
	

class CerrarSesion(TemplateView): 

	def dispatch(self,request,*args,**kwargs):
		logout(request)
		return HttpResponseRedirect(reverse_lazy('inicio:inicio'))

	
   
	


	



