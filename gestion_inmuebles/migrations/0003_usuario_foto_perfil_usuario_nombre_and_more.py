# Generated by Django 5.1.3 on 2024-11-28 13:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0002_inmueble_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='perfil/'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='propiedades_favoritas',
            field=models.ManyToManyField(blank=True, related_name='favoritos', to='gestion_inmuebles.inmueble'),
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_visita', models.DateField()),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmuebles.inmueble')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
