# Generated by Django 5.1.4 on 2025-01-21 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_puntos_evidencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puntos',
            name='comentario',
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='puntos',
            name='puntos',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='puntos',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puntos_relacionados', to='user.subcategoria'),
        ),
    ]
