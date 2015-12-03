
# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import *
from django.forms.extras.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.views.generic.edit import CreateView 
from .models import Empleado 
from django.forms import ModelForm
from models import *

 #form de usuario
class UserCreateForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    username = forms.CharField(label='Nombre de Usuario')
    email = forms.EmailField(label='Correo',required=True)
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ( "username", "email" )

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError("El correo ya existe")
		return email
	def clean(self):
		form_data = self.cleaned_data
		if form_data['password'] != form_data['password']:
			self._errors["password"] = "La contraseña no coincide"
			del form_data['password']
		return form_data

    def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
		self.fields['last_name'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
		self.fields['username'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
		self.fields['email'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
		self.fields['password1'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
		self.fields['password2'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})

 
 #creacion del form para empleado
class CrearEmpleado(forms.ModelForm): 

	#template_name = 'empleado/includes/crearEmpleado.html'
	identificacion = forms.CharField(label='Numero de Identificación')
	direccion = forms.CharField(label='Dirección')
	telefono = forms.CharField(label='Teléfono')
	salario= forms.CharField(label='Salario',required=True)
	 
	class Meta:
		model = Empleado 
		fields = ['user','identificacion', 'direccion', 'telefono','salario', 'imagen', 'tipo' ] 

	 