from django.contrib import admin
from .models import Persona, Policia, Vehiculo, Infraccion


class PersonaModelAdmin(admin.ModelAdmin):

    list_display = ('id', '__str__',)


admin.site.register(Persona, PersonaModelAdmin)
admin.site.register(Policia)
admin.site.register(Vehiculo)
admin.site.register(Infraccion)
