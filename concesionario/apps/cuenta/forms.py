# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from apps.empleado.models import Empleado
from django.forms.widgets import ClearableFileInput
from apps.inicio.mixins import LoginRequiredMixin
#Este formulario permitira actualizar la informacion del User en la base de datos
class UserUpdateForm(LoginRequiredMixin, forms.ModelForm):
	#Modificamos las etiquetas de los campos de texto que se mostraran en el formuario
	first_name = forms.CharField(label='Nombre')
	last_name = forms.CharField(label='Apellido')
	email = forms.CharField(label='Correo electronico')

	class Meta:
		#Definimos que modelo va a ser actualizado
		model = User
		#Definimos que campos del modelo pueden ser modificados
		fields = ('first_name','last_name','email')

class UserPasswordUpdateForm(LoginRequiredMixin, PasswordChangeForm):
	#Modificamos las etiquetas de los campos de texto que se mostraran en el formuario
	new_password1 = forms.CharField(label='Nueva contraseña',widget=forms.PasswordInput)
	new_password2 = forms.CharField(label='Confirmacion nueva contraseña',widget=forms.PasswordInput)
	old_password = forms.CharField(label='Contraseña antigua',widget=forms.PasswordInput)

#Este formulario permitira actualizar la informacion de un empleado en la base de datos
class EmpleadoUpdateForm(LoginRequiredMixin, forms.ModelForm):
	class Meta:
		#Definimos que modelo va a ser actualizado
		model = Empleado
		#Definimos que campos del modelo pueden ser modificados
		fields = ('identificacion','direccion','telefono','salario','imagen')
