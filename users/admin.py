from django.contrib import admin
from  users import models

class UserAdmin(admin.ModelAdmin):
    list_display =('Nombre', 'Cedula', 'Entidad_de_salud')
    list_filter = ('Nombre', )

admin.site.register(models.User)