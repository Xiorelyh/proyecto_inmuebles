# Generated by Django 5.1.3 on 2024-11-29 15:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0004_favorito'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='arrendador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to=settings.AUTH_USER_MODEL),
        ),
    ]
