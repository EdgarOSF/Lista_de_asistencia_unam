# Generated by Django 5.0 on 2023-12-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listaDeAsistenciaApp', '0005_remove_alumno_fk_ponderacion_remove_clase_fk_alumno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponderacion',
            name='asistencia',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Si')], null=True),
        ),
        migrations.AlterField(
            model_name='ponderacion',
            name='exposicion',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Si')], null=True),
        ),
        migrations.AlterField(
            model_name='ponderacion',
            name='participacion',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Si')], null=True),
        ),
    ]
