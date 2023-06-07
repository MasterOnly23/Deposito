from django.contrib import admin
from Racks.models import *

# Register your models here.

class ArticulosAdmin(admin.ModelAdmin):
    list_display=['articulo']
    search_fields = [ 'articulo']

class ImagenesAdmin(admin.ModelAdmin):
    list_display=['articulo', 'imagen']
    search_fields = [ 'articulo__articulo']

class CodigoAdmin(admin.ModelAdmin):
    list_display=['codigo']
    search_fields = [ 'codigo']

class ProductosAdmin(admin.ModelAdmin):
    list_display=['articulo','codigo','fecha_vencimiento','lote','cantidad','mueble','fecha_modificacion','ubicacionF','ubicacionS','ubicacionP','ubicacionE']

class DepositoPenetrableAdmin(admin.ModelAdmin):
    list_display=['ubicacion', 'ocupacion','contador']
    list_filter = ['ubicacion']
    list_editable = ['ocupacion','contador']
    search_fields = [ 'ubicacion']
    list_per_page = 15

class DepositoEstanteriaAdmin(admin.ModelAdmin):
    list_display=['ubicacion', 'ocupacion','contador']
    list_filter = ['ubicacion']
    list_editable = ['ocupacion','contador']
    search_fields = [ 'ubicacion']
    list_per_page = 15

class DepositoPsicotropicoAdmin(admin.ModelAdmin):
    list_display=['ubicacion', 'ocupacion','contador']
    list_filter = ['ubicacion']
    list_editable = ['ocupacion','contador']
    search_fields = [ 'ubicacion']
    list_per_page = 15

class DepositoSuplementoAdmin(admin.ModelAdmin):
    list_display=['ubicacion', 'ocupacion','contador']
    list_filter = ['ubicacion']
    list_editable = ['ocupacion','contador']
    search_fields = [ 'ubicacion']
    list_per_page = 15

class MuebleAdmin(admin.ModelAdmin):
    list_display=['mueble']
    list_filter = ['mueble']

    


admin.site.register(Productos,ProductosAdmin)
admin.site.register(Penetrable, DepositoPenetrableAdmin)
admin.site.register(Estanteria, DepositoEstanteriaAdmin)
admin.site.register(Psicotropico, DepositoPsicotropicoAdmin)
admin.site.register(Suplemento, DepositoSuplementoAdmin)
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Codigo, CodigoAdmin)
admin.site.register(Imagenes, ImagenesAdmin)

admin.site.register(Mueble,MuebleAdmin)