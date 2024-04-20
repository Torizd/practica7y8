# Generated by Django 5.0.3 on 2024-03-20 23:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerapagina', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_de_orden', models.IntegerField()),
                ('nombre', models.CharField(max_length=512)),
                ('correo', models.IntegerField()),
                ('metodo', models.CharField(choices=[('ef', 'Efectivo'), ('ta', 'Tarjeta')], max_length=2)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Reservacion',
        ),
    ]