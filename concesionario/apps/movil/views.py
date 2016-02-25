from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core import serializers
from apps.cliente.models import Cliente
from apps.orden_de_trabajo.models import OrdenDeTrabajo
from apps.vehiculo.models import Vehiculo
from apps.sucursal.models import Sucursal
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from rest_framework import serializers as r

class VehiculoSerializer(r.ModelSerializer):
	imagen = r.SerializerMethodField('get_image_url')
	class Meta:
		model = Vehiculo
		fields = ('imagen','marca','modelo')
		#fields = '__all__'
	def get_image_url(self, obj):
		return obj.imagen.url

class SucursalSerializer(r.ModelSerializer):

	class Meta:
		model = Sucursal
		fields = ('nombre','ciudad')
		#fields = '__all__'

class OrdenDeTrabajoSerializer(r.ModelSerializer):
	vehiculo = VehiculoSerializer()
	sucursal = SucursalSerializer()
	class Meta:
		model = OrdenDeTrabajo
		#fields = ('id','vehiculo')
		fields = '__all__'


# Create your views here.
class Validar(TemplateView):

	def get(self, request, *args, **kwargs):
		email = kwargs['email']
		identificacion = kwargs['id']

		try:
			cliente = Cliente.objects.get(email=email, identificacion=identificacion)
			data = json.dumps({'valido': True, 'cliente_id': cliente.id} )
		except ObjectDoesNotExist:
			data = json.dumps({'valido': False})

		return HttpResponse(data, content_type='application/json')

class OrdenDeTrabajoJSONList(TemplateView):

	def get(self,request,*args,**kwargs):
		cliente = Cliente.objects.get(id=kwargs['pk'])
		data = serializers.serialize(
			"json",
			cliente.ordendetrabajo_set.all()
		)

		s = OrdenDeTrabajoSerializer(cliente.ordendetrabajo_set.all(),many=True)
		return JsonResponse(s.data,safe=False)
		#return HttpResponse(data,content_type='application/json')
