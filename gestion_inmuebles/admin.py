from django.contrib import admin
from .models import Usuario, Tipo_inmueble, Inmueble, Region, Comuna, Favorito


# Personalizar Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'rut', 'tipo_usuario', 'email')  # Campos visibles en la tabla
    search_fields = ('username', 'rut', 'email')  # Campos para la barra de búsqueda
    list_filter = ('tipo_usuario', 'is_active', 'is_staff')  # Filtros en el lateral

# Personalizar Tipo_inmueble
@admin.register(Tipo_inmueble)
class TipoInmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Mostrar ID y nombre en la tabla
    search_fields = ('nombre',)  # Campo de búsqueda por nombre

# Personalizar Inmueble
@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comuna', 'tipo_inmueble', 'precio_mensual', 'habitaciones', 'banos')  # Campos visibles
    search_fields = ('nombre', 'direccion', 'comuna')  # Campos para búsqueda
    list_filter = ('tipo_inmueble', 'comuna', 'habitaciones')  # Filtros en el lateral

# Personalizar Region
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero')  # Mostrar ID, nombre y número en la tabla
    search_fields = ('nombre',)  # Campo de búsqueda por nombre

# Personalizar Comuna
@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'region')  # Mostrar ID, nombre y región en la tabla
    search_fields = ('nombre', 'region__nombre')  # Campo de búsqueda por nombre de la comuna o región
    list_filter = ('region',)  # Filtro por región

admin.site.register(Favorito)