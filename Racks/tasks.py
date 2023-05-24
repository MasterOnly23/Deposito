import schedule
import time
from datetime import date, datetime, timedelta
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from Racks.models import Productos
from django.conf import settings


def mailVencimientos():
    today = date.today()
    maxVencimiento = today + timedelta(days=90)

    productos = Productos.objects.filter(fecha_vencimiento__lte=maxVencimiento)


    if productos:

        subject = "!IMPORTANTE! Vecimientos Proximos"
        html_message = render_to_string('vencimientosMail.html', {'productos':productos})
        plain_message = render_to_string('vencimientosMail.html', {'productos':productos})
        from_email = 'pruebacomprasinternas@gmail.com'

        send_mail(subject, plain_message, from_email, ['pruebacomprasinternas@gmail.com'], html_message=html_message)

def ejecutar_tarea():
    mailVencimientos()
    # Programar la siguiente ejecución de la tarea
    schedule.every().day.at('14:31').do(mailVencimientos)

# Iniciar la ejecución de la tarea
ejecutar_tarea()

# Ejecutar el programa continuamente con un tiempo de espera de 10 minutos
print("antes del bucle")
while True:
    schedule.run_pending()
    time.sleep(1)  # 600 segundos = 10 minutos
