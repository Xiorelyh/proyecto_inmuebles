# Generated by Django 5.1.3 on 2024-11-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='image_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]