from django.contrib import admin
from .models import Marca, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"] #Columna que se puede editar
    search_fields = ["nombre"] #Campo de búsqueda (barra de búsqueda)
    list_filter = ["marca", "nuevo"] #Filtro
    list_per_page = 5 #Número de registros que quiero por página

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
