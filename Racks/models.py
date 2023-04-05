from django.db import models

# Create your models here.



class Productos(models.Model):
    articulo = models.CharField(max_length=60, null=False)
    codigo = models.CharField(max_length=4, null=False)
    fecha_vencimiento = models.DateField()
    lote = models.CharField(max_length=20, null=False)
    cantidad = models.IntegerField()
    fecha_modificacion = models.DateTimeField(auto_now=True)




class RacksFrente(models.Model):

    standsChoices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10') )
    racksXstand = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'))
    lugares = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))


    stands = models.CharField(max_length=5, choices=standsChoices, null=False)
    racks = models.CharField(max_length=5, choices=racksXstand, null=False)
    posicion = models.CharField(max_length=5, choices=lugares, null=False)
    articulo = models. ForeignKey(Productos, max_length=60, on_delete=models.CASCADE, related_name='articulos')