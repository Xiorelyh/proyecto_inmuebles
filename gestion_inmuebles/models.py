from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    image_url = models.URLField(blank=False)
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(max_length=50)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

#Modelo Usuario 
tipos_usuario = (
    ('arrendatario', 'Arrendatario'),
    ('arrendador', 'Arrendador'),
)

class Usuario(AbstractUser):
    rut = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.CharField(max_length=15, choices=tipos_usuario, default='arrendatario')
    propiedades_favoritas = models.ManyToManyField(Inmueble, related_name='favoritos', blank=True)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    # `related_name` para evitar el conflicto con los modelos de `auth.User`
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='gestion_inmuebles_user_set',  # Cambia el nombre del accesor al grupo
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='gestion_inmuebles_user_permissions_set',  # Cambia el nombre del accesor a los permisos
        blank=True,
    )


class Region(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    numero = models.IntegerField(default=0, blank=False, null=False)

class Comuna(models.Model):
    nombre=models.CharField(max_length=100,blank=False, null=False)
    region = models.ForeignKey(Region, default=0, on_delete=models.PROTECT)


class Tipo_inmueble(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre
  

#Modelo Visitas

class Visita(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_visita = models.DateField()

    def __str__(self):
        return f"Visita a {self.inmueble.nombre} por {self.usuario.username} el {self.fecha_visita}"



