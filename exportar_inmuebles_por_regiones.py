import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto_inmuebles.settings")  
django.setup()

from gestion_inmuebles.models import Inmueble, Region, Comuna

def exportar_inmuebles_por_region():
    # Abrir el archivo de texto para guardar los resultados
    with open("inmuebles_por_region.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Listado de Inmuebles para Arriendo por Regiones\n")
        archivo.write("=" * 50 + "\n\n")
        
        # Consultar todas las regiones
        regiones = Region.objects.all()
        
        for region in regiones:
            archivo.write(f"Región: {region.nombre}\n")
            archivo.write("-" * 50 + "\n")
            
            # Consultar las comunas asociadas a esta región
            comunas = Comuna.objects.filter(region=region)
            
            # Consultar los inmuebles para las comunas de esta región
            inmuebles = Inmueble.objects.filter(comuna__in=Region.objects.values_list('nombre', flat=True))
            
            if inmuebles.exists():
                for inmueble in inmuebles:
                    archivo.write(f"- {inmueble.nombre}: {inmueble.descripcion}\n")
            else:
                archivo.write("No hay inmuebles disponibles en esta región.\n")
            
            archivo.write("\n")
    
    print("Exportación completada. Archivo: inmuebles_por_region.txt")

if __name__ == "__main__":
    exportar_inmuebles_por_region()
