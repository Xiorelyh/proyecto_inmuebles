# Proyecto Inmuebles 🏡

Aplicación web desarrollada en **Django** para la gestión de inmuebles y usuarios.

## Requisitos 🛠️

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.10 o superior
- Django 4.x
- PostgreSQL 
- pip para gestionar dependencias

## Modelos principales 📦
- Usuario: Basado en AbstractUser, incluye atributos como rut, direccion, telefono, y tipo_usuario.
- Inmueble: Detalles como nombre, m2_construido, m2_terreno, precio, tipo_inmueble y más.
- Región, Provincia y Comuna: Organización geográfica para inmuebles.
- Tipo de Propiedad: Clasificación de inmuebles.

## Estructura del proyecto

proyecto_inmuebles/
│
├── gestion_inmuebles/      # Aplicación principal
│   ├── migrations/         # Migraciones de la base de datos
│   ├── models.py           # Definición de los modelos
│   ├── views.py            # Vistas de la aplicación
│   ├── admin.py            # Configuración del panel de administración
│
├── exportar_inmuebles_por_comuna.py   # Script para exportar por comuna
├── exportar_inmuebles_por_regiones.py # Script para exportar por región
├── manage.py               # Archivo principal de Django
├── db.sqlite3              # Base de datos SQLite (opcional)
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Documentación del proyecto


## Contribuir 🤝

- Si deseas contribuir: Haz un fork del proyecto.

## Screenshots
<details>

<summary>Hito 2</summary>

![App Screenshot](Hito2/super_usuario.png)
![App Screenshot](Hito2/Migraciones.png)
![App Screenshot](Hito2/Django_Administration.png)
![App Screenshot](Hito2/pgAdmin_bd_y_tablas.png)
![App Screenshot](Hito2/inmuebles.png)
![App Screenshot](Hito2/usuario.png)

</details>
<details>

<summary>Hito 3</summary>

![App Screenshot](Hito3/loaddata.png)
![App Screenshot](Hito3/exportar_inmuebles_por_comuna.png)
![App Screenshot](Hito3/exportar_inmuebles_por_region.png)
![App Screenshot](Hito3/filtro_inmuebles.png)
![App Screenshot](Hito3/filtro_inmuebles_comuna.png)

</details>


## Autor

- [Xiorely Herrera](https://github.com/Xiorelyh)


