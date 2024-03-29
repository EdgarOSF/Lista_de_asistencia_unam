# Generated by Django 5.0 on 2023-12-05 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listaDeAsistenciaApp', '0004_alter_alumno_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='fk_ponderacion',
        ),
        migrations.RemoveField(
            model_name='clase',
            name='fk_alumno',
        ),
        migrations.AddField(
            model_name='ponderacion',
            name='fk_alumno',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='alumno_ponderacion', to='listaDeAsistenciaApp.alumno'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listaDeAsistenciaApp.alumno')),
                ('fk_clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listaDeAsistenciaApp.clase')),
            ],
        ),
    ]
