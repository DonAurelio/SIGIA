from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout

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

		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				#Redirect to profile page
			else:
				context = {'messaje':'Su usuario no esta activo'}
		else:
			context = {'messaje':'Revise su usuario y clave'}

		return render_to_response('inicio/login.html',context,context_instance=RequestContext(request))




