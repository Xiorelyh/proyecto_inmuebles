from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
tipos_usuario = (
    ('arrendatario', 'Arrendatario'),
    ('arrendador', 'Arrendador'),
)

class Usuario(AbstractUser):
    rut = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.CharField(max_length=15, choices=tipos_usuario, default='arrendatario')

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
    

class Tipo_inmueble(models.Model):
    nombre=models.CharField(max_length=100,blank=False, null=False)

class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
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

class Region(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    numero = models.IntegerField(default=0, blank=False, null=False)

class Comuna(models.Model):
    nombre=models.CharField(max_length=100,blank=False, null=False)
    provincia_id = models.ForeignKey(Provincia,default=0, on_delete=models.PROTECT)


