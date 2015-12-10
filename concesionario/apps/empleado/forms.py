# -*- coding: utf-8 -*-
from django import forms
from models import *
from django.forms.extras.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Empleado 


class UserForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    username = forms.CharField(label='Nombre de Usuario')
    email = forms.EmailField(label='Correo',required=True)
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput,required=False)
    
    class Meta:
        model = User
        fields = ( "username", "email", "first_name", "last_name")

class EmpleadoForm(forms.ModelForm): 

	identificacion = forms.CharField(label='Numero de Identificación')
	direccion = forms.CharField(label='Dirección')
	telefono = forms.CharField(label='Teléfono')
	salario= forms.CharField(label='Salario',required=True)
	 
	class Meta:
		model = Empleado 
		fields = ['identificacion', 'direccion', 'telefono',
		'salario','sucursal','imagen', 'tipo','habilitado' ] 
