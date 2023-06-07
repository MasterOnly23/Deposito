from django import forms
from .models import Productos, Mueble, Codigo, Articulo, Suplemento, Penetrable, Psicotropico, Estanteria, Imagenes
from django import forms
from django_select2.forms import Select2Widget
from datetime import datetime





class ProductosForm(forms.ModelForm):

    muebles = (('M1','M1'),
            ('M2','M2'),
            ('M3','M3'),
            ('M4','M4'),
            ('ACC','ACC'),
            ('SUP','SUP'),
            ('PSI','PSI'))

    # codigo = forms.ModelChoiceField(queryset=Codigo.objects.all().order_by('codigo'), widget=Select2Widget(attrs={'class': 'select2 select-codigo'}), label='Codigo')
    articulo = forms.ModelChoiceField(queryset=Articulo.objects.all().order_by('articulo'), widget=Select2Widget(attrs={'class': 'select2'}), label='Articulo')
    fecha_vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    lote = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
    mueble = forms.ModelChoiceField(queryset=Mueble.objects.all(), widget=Select2Widget(attrs={'class': 'select2'}), label='Mueble')
    ubicacion = forms.CharField(max_length=5, disabled=True)



    class Meta:
        model = Productos
        fields = ['articulo', 'fecha_vencimiento', 'lote', 'cantidad', 'mueble', 'ubicacion']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # self.fields['codigo'].widget.attrs.update({'class':'codigoCorto', 'id':'id_codigoCorto'})
            self.fields['articulo'].widget.attrs.update({'class':'articulo', 'id':'id_articulo'})
            self.fields['fecha_vencimiento'].widget.attrs.update({'class':'fechaVencimiento', 'id':'id_fechaVencimiento'})
            self.fields['lote'].widget.attrs.update({'class':'lote', 'id':'id_lote'})
            self.fields['cantidad'].widget.attrs.update({'class':'cantidad', 'id':'id_cantidad'})
            self.fields['mueble'].widget.attrs.update({'class':'mueble', 'id':'id_mueble'})
            self.fields['ubicacion'].widget.attrs.update({'class':'ubicacion', 'id':'id_ubicacion'})

    def save(self, commit=True):
        # Guarda el objeto del formulario sin enviar a la base de datos
        producto = super().save(commit=False)
        
        valor_articulo = self.cleaned_data['articulo']
        codigo = valor_articulo.codigo
        articulo = valor_articulo.articulo
        producto.codigo = codigo.strip()
        producto.articulo = articulo.strip()
        

        try:

            # Obtén la ubicación del formulario y el objeto Estanteria correspondiente
            ubicacion = self.cleaned_data['ubicacion']
            

            if ubicacion and ubicacion.startswith('E'):
                estanteria = Estanteria.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                estanteria.ocupacion = '1'
                estanteria.contador += 1
                estanteria.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionE = estanteria

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
            elif ubicacion and ubicacion.startswith('S'):
                suplementos = Suplemento.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                suplementos.ocupacion = '1'
                suplementos.contador += 1
                suplementos.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionS = suplementos

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
            elif ubicacion and ubicacion.startswith('F'):
                penetrables = Penetrable.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                penetrables.ocupacion = '1'
                penetrables.contador += 1
                penetrables.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionF = penetrables

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
            elif ubicacion and ubicacion.startswith('P'):
                psicotropicos = Psicotropico.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                psicotropicos.ocupacion = '1'
                psicotropicos.contador += 1
                psicotropicos.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionP = psicotropicos

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
        except:
            logFecha = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
            logErrorFile = 'Racks/log_error/keyslog_{}.txt'.format(logFecha)
            with open (logErrorFile, 'a') as log_file:
                log_file.write("Ha ocurrido un Error al guardar el formulario - metodo save()")

    





class ProductosFormEditar(forms.ModelForm):

    muebles = (('M1','M1'),
            ('M2','M2'),
            ('M3','M3'),
            ('M4','M4'),
            ('ACC','ACC'),
            ('SUP','SUP'),
            ('PSI','PSI'))

    codigo = forms.CharField()
    articulo = forms.CharField()
    fecha_vencimiento = forms.DateField(widget=forms.DateInput())
    lote = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
    mueble = forms.ChoiceField(choices=muebles)
    ubicacion = forms.CharField(max_length=5, disabled=True)



    class Meta:
        model = Productos
        fields = ['codigo','articulo', 'fecha_vencimiento', 'lote', 'cantidad', 'mueble', 'ubicacion']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['codigo'].widget.attrs.update({'class':'codigoCorto', 'id':'id_codigoCorto'})
            self.fields['articulo'].widget.attrs.update({'class':'articulo', 'id':'id_articulo'})
            self.fields['fecha_vencimiento'].widget.attrs.update({'class':'fechaVencimiento', 'id':'id_fechaVencimiento'})
            self.fields['lote'].widget.attrs.update({'class':'lote', 'id':'id_lote'})
            self.fields['cantidad'].widget.attrs.update({'class':'cantidad', 'id':'id_cantidad'})
            self.fields['mueble'].widget.attrs.update({'class':'mueble', 'id':'id_mueble'})
            self.fields['ubicacion'].widget.attrs.update({'class':'ubicacion', 'id':'id_ubicacion'})

    def save(self, commit=True):
        # Guarda el objeto del formulario sin enviar a la base de datos
        producto = super().save(commit=False)
        

        try:

            # Obtén la ubicación del formulario y el objeto Estanteria correspondiente
            ubicacion = self.cleaned_data['ubicacion']
            

            if ubicacion and ubicacion.startswith('E'):
                estanteria = Estanteria.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                estanteria.ocupacion = '1'
    
                estanteria.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionE = estanteria

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
            elif ubicacion and ubicacion.startswith('S'):
                suplementos = Suplemento.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                suplementos.ocupacion = '1'
        
                suplementos.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionS = suplementos

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
            elif ubicacion and ubicacion.startswith('F'):
                penetrables = Penetrable.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                penetrables.ocupacion = '1'
        
                penetrables.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionF = penetrables

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
            elif ubicacion and ubicacion.startswith('P'):
                psicotropicos = Psicotropico.objects.get(ubicacion=ubicacion)

                # Actualiza los campos de Estanteria
                psicotropicos.ocupacion = '1'
                
                psicotropicos.save()

                # Asigna la instancia de Estanteria al campo ubicacionE de Productos
                producto.ubicacionP = psicotropicos

                # Guarda el objeto Productos en la base de datos si se especifica
                if commit:
                    producto.save()

            
                return producto
            
        except:
            logFecha = datetime.now().strftime('%y-%m-%d_%H-%M-%S')
            logErrorFile = 'Racks/log_error/keyslog_{}.txt'.format(logFecha)
            with open (logErrorFile, 'a') as log_file:
                log_file.write("Ha ocurrido un Error al guardar el formulario - metodo save()")

    
    
