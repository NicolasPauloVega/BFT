# Generated by Django 5.1.4 on 2025-01-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_usuario_habilitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='habilitacion',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
