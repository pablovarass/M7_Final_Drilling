from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']
    list_filter = ('nombre',)

class DirectorioGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ['nombre']
    list_filter = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    # Configuración de las columnas a mostrar en la lista
    list_display = ('id', 'nombre', 'laboratorio', 'obtener_anio_fabricacion', 'precio_costo', 'precio_venta')
    list_display_links = ['nombre']
    list_filter = ('nombre', 'laboratorio', 'fecha_fabricacion')  # Filtros laterales
    date_hierarchy = 'fecha_fabricacion'  # Navegación jerárquica por fechas

    # Método personalizado para mostrar solo el año de fabricación
    @admin.display(description='Año de fabricación')  # Configura el encabezado de la columna
    def obtener_anio_fabricacion(self, obj):
        """
        Retorna únicamente el año del campo 'fecha_fabricacion' de un objeto Producto.
        """
        return obj.fecha_fabricacion.year  # Extrae solo el año del campo fecha_fabricacion

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorioGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)

