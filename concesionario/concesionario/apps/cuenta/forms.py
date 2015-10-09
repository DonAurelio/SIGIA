from django import forms
from django.contrib.auth.models import User
from concesionario.apps.empleado.models import Empleado

#Este formulario permitira actualizar la informacion del User en la base de datos
class UserUpdateForm(forms.ModelForm):
	#Modificamos las etiquetas de los campos de texto que se mostraran en el formuario
	first_name = forms.CharField(label="Nombre")
	last_name = forms.CharField(label="Apellido")
	email = forms.CharField(label="Correo electronico")
	
	class Meta:
		#Definimos que modelo va a ser actualizado 
		model = User
		#Definimos que campos del modelo pueden ser modificados
		fields = ('first_name','last_name','email')

#Este formulario permitira actualizar la informacion de un empleado en la base de datos
class EmpleadoUpdateForm(forms.ModelForm):
	class Meta:
		#Definimos que modelo va a ser actualizado 
		model = Empleado
		#Definimos que campos del modelo pueden ser modificados
		fields = ('identificacion','direccion','telefono','salario','imagen')
