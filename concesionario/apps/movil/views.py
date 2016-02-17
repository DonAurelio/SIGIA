from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from apps.cliente.models import Cliente
import json
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class Validar(TemplateView):

	def get(self, request, *args, **kwargs):
		email = kwargs['email']
		identificacion = kwargs['id']

		try:
			cliente = Cliente.objects.get(email=email, identificacion=identificacion)
		except ObjectDoesNotExist:
			data = json.dumps({'valido': False})

		data = json.dumps({'valido': True})
		return HttpResponse(data, content_type='application/json')