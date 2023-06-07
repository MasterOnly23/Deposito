from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Imagenes, Productos
from datetime import datetime

@receiver(post_save, sender=Productos)
def asignarImagen(sender, instance, created, **kwargs):
    if created:
        # Obtén el nombre del artículo del producto
        nombre_articulo = instance.articulo
        
        # Busca la imagen correspondiente en el modelo Imagenes
        try:
            imagen = Imagenes.objects.get(articulo__articulo=nombre_articulo)
            
            # Asigna la imagen al campo de imagen del producto
            instance.imagen = imagen.imagen
            instance.save()
            
        except Imagenes.DoesNotExist:
            logFecha = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
            logErrorFile = 'Racks/log_error/keyslog_{}.txt'.format(logFecha)
            with open (logErrorFile, 'a') as log_file:
                log_file.write("Error al asignar instacia de imagen")