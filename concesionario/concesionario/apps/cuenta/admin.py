from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

# Register your models here.

#Example:
#http://doomatel.web-profile.org/entries/show/using-django-auth-useradmin-for-a-custom-user-model/

"""
UserAdmin.list_display = ('identificacion', 'foto', 'thumbnail', 'tipousuario','email', 'first_name', 'last_name', 'direccion','telefono','is_active', 'date_joined', 'is_staff')
UserAdmin.fieldsets = (
        (('Additional information'), {'fields': ('identificacion', 'foto', 'direccion','telefono','tipousuario',)}),
    ) + UserAdmin.fieldsets 

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
"""
