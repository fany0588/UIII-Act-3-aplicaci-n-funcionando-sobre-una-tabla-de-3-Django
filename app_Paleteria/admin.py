from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre_empresa', 'contacto', 'telefono', 'email', 'ciudad', 'fecha_registro')
    search_fields = ('nombre_empresa', 'contacto', 'ciudad')
