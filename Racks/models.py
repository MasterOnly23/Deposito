from django.db import models

# Create your models here.

ocupacion = (('0','0'),
            ('1','1'))

muebles = (('M1','M1'),
            ('M2','M2'),
            ('M3','M3'),
            ('M4','M4'),
            ('ACC','ACC'),
            ('SUP','SUP'),
            ('PSI','PSI'))

class Mueble(models.Model):
    mueble = models.CharField(max_length=3, blank=True, null=True) 

    def __str__(self):
        return self.mueble


class Penetrable(models.Model):
    
    ubicacion = models.CharField(max_length=5, unique=True, default=None)
    ocupacion = models.CharField(max_length=1, choices=ocupacion, default='0')
    contador = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.ubicacion}'
    
    def save(self, *args, **kwargs):
        if self.ocupacion == '0':
            self.contador = 0
        else:
            pass
        super(Penetrable, self).save(*args, **kwargs)

class Estanteria(models.Model):
    
    ubicacion = models.CharField(max_length=5, unique=True)
    ocupacion = models.CharField(max_length=1, choices=ocupacion, default='0')
    contador = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.ubicacion}'
    
    def save(self, *args, **kwargs):
        if self.ocupacion == '0':
            self.contador = 0
        else:
            pass
        super(Estanteria, self).save(*args, **kwargs)

class Psicotropico(models.Model):
    
    ubicacion = models.CharField(max_length=5, unique=True)
    ocupacion = models.CharField(max_length=1, choices=ocupacion, default='0')
    contador = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.ubicacion}'
    
    def save(self, *args, **kwargs):
        if self.ocupacion == '0':
            self.contador = 0
        else:
            pass
        super(Psicotropico, self).save(*args, **kwargs)

class Suplemento(models.Model):
    
    ubicacion = models.CharField(max_length=5, unique=True)
    ocupacion = models.CharField(max_length=1, choices=ocupacion, default='0')
    contador = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.ubicacion}'
    
    def save(self, *args, **kwargs):
        if self.ocupacion == '0':
            self.contador = 0
        else:
            pass
        super(Suplemento, self).save(*args, **kwargs)


class Productos(models.Model):
    articulo = models.CharField(max_length=60, null=False)
    codigo = models.CharField(max_length=4, null=False)
    fecha_vencimiento = models.DateField()
    lote = models.CharField(max_length=20, null=False)
    cantidad = models.IntegerField()
    mueble = models.CharField(max_length=10, blank=True, null=True, choices=muebles) 
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.URLField(default="https://i.postimg.cc/1549gc7Y/default-prod.png", null=True)
    ubicacionF = models.ForeignKey(Penetrable, on_delete=models.CASCADE, blank=True, null=True, default=None, to_field='ubicacion')
    ubicacionE = models.ForeignKey(Estanteria, on_delete=models.CASCADE, blank=True, null=True, default=None, to_field='ubicacion')
    ubicacionP = models.ForeignKey(Psicotropico, on_delete=models.CASCADE, blank=True, null=True, default=None, to_field='ubicacion')
    ubicacionS = models.ForeignKey(Suplemento, on_delete=models.CASCADE, blank=True, null=True, default=None, to_field='ubicacion')

    class Meta:
        verbose_name_plural = "Productos"


class Articulo(models.Model):
    codigo = models.CharField(max_length=5, null=True)
    articulo = models.CharField(max_length=60, null=False)


    class Meta:
        verbose_name_plural = "Articulos"


    def __str__(self):
        return f"{self.codigo} -- {self.articulo}"
    

class Codigo(models.Model):
    codigo = models.CharField(max_length=5, null=False)

    class Meta:
        verbose_name_plural = "Codigos"


    def __str__(self):
        return self.codigo
    


class UltimaEjecucion(models.Model):
    ultimaEjecucion = models.DateTimeField()

    def __str__(self):
        return str(self.ultimaEjecucion)
    


class Imagenes(models.Model):
    imagen = models.URLField(default="https://i.postimg.cc/1549gc7Y/default-prod.png", null=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True)
