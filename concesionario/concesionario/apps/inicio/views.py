from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Context 


# Create your views here.
def hola_mundo(request):
	return render(request,'inicio/inicio.html',Context())
