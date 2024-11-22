import csv
from gestion_inmuebles.models import Region, Comuna

# Ruta del archivo CSV
csv_file_path = 'regiones_y_comunas.csv'

# Leer el archivo CSV con codificación ISO-8859-1
with open(csv_file_path, 'r', encoding='ISO-8859-1') as file:
    reader = csv.reader(file)
    next(reader)  # Salta la cabecera (si tiene)

    for row in reader:
        region_name = row[0].strip()
        comuna_name = row[1].strip()

        # Obtener o crear la región
        region, created = Region.objects.get_or_create(nombre=region_name)

        # Crear la comuna
        Comuna.objects.get_or_create(nombre=comuna_name, region=region)

print("Datos importados correctamente")

