# Generated by Django 5.0 on 2023-12-05 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listaDeAsistenciaApp', '0006_alter_ponderacion_asistencia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponderacion',
            name='noticia',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Si')], null=True),
        ),
    ]
