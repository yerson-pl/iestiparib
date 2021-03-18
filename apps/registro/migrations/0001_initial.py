# Generated by Django 2.2.19 on 2021-03-17 16:41

import apps.registro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dni_num', models.IntegerField(verbose_name='N° DNI')),
                ('ap_paterno', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('ap_materno', models.CharField(max_length=100, verbose_name='Apellido Mterno')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombres')),
                ('sexo', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')], verbose_name='Sexo')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('departamento', models.CharField(max_length=80, verbose_name='Departamento')),
                ('provincia', models.CharField(max_length=100, verbose_name='Provincia')),
                ('distrito', models.CharField(max_length=150, verbose_name='Distrito')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('inst_procedencia', models.CharField(max_length=150, verbose_name='Colegio de Procedencia')),
                ('egreso', models.IntegerField(verbose_name='Año de egreso')),
                ('celular', models.IntegerField(verbose_name='N° Celular')),
                ('carrera', models.IntegerField(choices=[(1, 'Contrucción Civil'), (2, 'Contabilidad'), (3, 'Explotación Minera')], default=1, verbose_name='Programa de Estudios al que postula')),
                ('foto', models.FileField(upload_to=apps.registro.models.upload_location, verbose_name='Foto')),
                ('dni', models.FileField(upload_to=apps.registro.models.upload_location, verbose_name='Foto DNI')),
                ('num_operacion', models.IntegerField(unique=True, verbose_name='N° Operación Voucher')),
                ('voucher', models.FileField(upload_to=apps.registro.models.upload_location, verbose_name='Voucher')),
            ],
            options={
                'verbose_name': 'Postulante',
                'verbose_name_plural': 'Postulantes',
            },
        ),
    ]