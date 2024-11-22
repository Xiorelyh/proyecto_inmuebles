import os
from django.conf import settings
from django.db import connection
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')  # Cambia 'tu_proyecto' por el nombre de tu proyecto
django.setup()

# Nombre del archivo donde se guardarán los resultados
output_file = "inmuebles_por_comuna.txt"

def fetch_inmuebles_por_comuna():
    with connection.cursor() as cursor:
        # Consulta SQL para obtener los inmuebles agrupados por comuna
        query = """
        SELECT comuna, nombre, descripcion 
        FROM gestion_inmuebles_inmueble
        ORDER BY comuna, nombre;
        """
        cursor.execute(query)
        results = cursor.fetchall()
    
    # Crear un diccionario para separar por comuna
    inmuebles_por_comuna = {}
    for comuna, nombre, descripcion in results:
        if comuna not in inmuebles_por_comuna:
            inmuebles_por_comuna[comuna] = []
        inmuebles_por_comuna[comuna].append(f"Nombre: {nombre}\nDescripción: {descripcion}")
    
    # Guardar los resultados en un archivo de texto
    with open(output_file, "w", encoding="utf-8") as file:
        for comuna, inmuebles in inmuebles_por_comuna.items():
            file.write(f"Comuna: {comuna}\n")
            file.write("\n".join(inmuebles))
            file.write("\n\n")
    
    print(f"Archivo generado: {output_file}")

# Ejecutar la función
fetch_inmuebles_por_comuna()