from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Region, Comuna, Inmueble, Tipo_inmueble
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Carga datos ficticios para probar los filtros'

    def handle(self, *args, **kwargs):
        # Crear tipos de inmueble ficticios
        tipos_inmueble = ['Casa', 'Departamento', 'Oficina', 'Bodega']
        for tipo in tipos_inmueble:
            tipo_inmueble_obj = Tipo_inmueble.objects.filter(nombre=tipo).first()
            if not tipo_inmueble_obj:
                tipo_inmueble_obj = Tipo_inmueble.objects.create(nombre=tipo)
            self.stdout.write(f"Tipo de inmueble '{tipo_inmueble_obj.nombre}' creado.")

        # Datos ficticios de inmuebles
        comunas = Comuna.objects.all()
        for i in range(20):  # Crear 20 inmuebles ficticios
            comuna = random.choice(comunas)
            tipo_inmueble = random.choice(tipos_inmueble)
            
            inmueble = Inmueble.objects.create(
                nombre=f"Inmueble {i+1}",
                descripcion="Descripción del inmueble",
                m2_construidos=random.uniform(30, 200),
                m2_totales=random.uniform(30, 300),
                estacionamientos=random.randint(0, 5),
                habitaciones=random.randint(1, 5),
                banos=random.randint(1, 3),
                direccion=f"Dirección {i+1}",
                comuna=comuna.nombre,
                tipo_inmueble=tipo_inmueble,
                precio_mensual=Decimal(random.randint(100000, 1000000))  # Precio entre 100,000 y 1,000,000
            )
            self.stdout.write(f"Inmueble {inmueble.nombre} creado.")