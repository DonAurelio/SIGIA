from django import forms
from django.contrib.auth.models import User
from concesionario.apps.empleado.models import Empleado

#Este formulario permitira actualizar la informacion del User en la base de datos
class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password','first_name','last_name','email')

#Este formulario permitira actualizar la informacion de un empleado en la base de datos
class EmpleadoUpdateForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ('identificacion','direccion','telefono','salario','imagen')
