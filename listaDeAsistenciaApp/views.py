from django.shortcuts import render
from .forms import ArchivoListaModelForm
from .models import Archivo_Lista, Clase, Alumno
import csv
import re
from unicodedata import normalize
from datetime import datetime


def upload_file_list_view(request):
    form = ArchivoListaModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        file = Archivo_Lista.objects.last()
        with open(file.archivo.path, 'r') as f:
            reader = csv.reader(f)
            alumnos = []
            fecha = ''

            # sanitizar cadena
            for i, row in enumerate(reader):
                if i == 0 or i == 2 or i == 3 or i == 4:
                    continue
                elif i == 1:
                    print(row[2][0:10])
                    fecha = datetime.strptime(row[2][0:10], '%d/%m/%Y')
                    print('datetime: ', fecha)
                elif row[0] == 'Usuario de Zoom':
                    continue
                else:
                    res = re.sub(r'[\d\.\-]', '', row[0])
                    sa = re.sub(
                        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                        normalize("NFD", res.strip()), 0, re.I
                    )
                    sa = normalize('NFC', sa)
                    alumnos.append(' '.join(sa.split()).upper())

            # correccion de nombres
            for i, row in enumerate(alumnos):
                if row == 'KELLY BAUTISTA REYES':
                    alumnos[i] = 'BAUTISTA REYES KELLY'
                if row == 'GENESIS REYES':
                    alumnos[i] = 'REYES SANCHEZ GENESIS FRIDA'
                if row == 'SUSAN ZURIZADAY GUZMAN GARCIA':
                    alumnos[i] = 'GUZMAN GARCIA SUSAN ZURIZADAY'
                if row == 'ALISON CAMARGO':
                    alumnos[i] = 'CAMARGO SANCHEZ ALISON DANIELA'
                if row == 'ALEJANDRO ANTONIO LOPEZ DELGADO':
                    alumnos[i] = 'LOPEZ DELGADO ALEJANDRO ANTONIO'
                if row == 'MARIANA SANCHEZ MENDEZ':
                    alumnos[i] = 'SANCHEZ MENDEZ MARIANA'
                if row == 'CHAIDEZ VANESSA':
                    alumnos[i] = 'CHAIDEZ LOPEZ ARELI VANESSA'
                if row == 'MARCO MENDIZABAL ARELLANO':
                    alumnos[i] = 'MENDIZABAL ARELLANO MARCO SERGIO'
                if row == 'MARIANO JAIMES ALEJANDRO':
                    alumnos[i] = 'MARIANO JAIMES ALEJANDRO'
                if row == 'LESLI GARFIAS ROSAS':
                    alumnos[i] = 'GARFIAS ROSAS LESLI SARAI'
                if row == 'INDIRA SANCHEZ PRADO':
                    alumnos[i] = 'SANCHEZ PRADO INDIRA MARIEL'
                if row == 'MARIA FERNANDA ROMERO':
                    alumnos[i] = 'ROMERO HERNANDEZ MARIA FERNANDA'
                if row == 'MAYRA GARCIA POMPOSO':
                    alumnos[i] = 'GARCIA POMPOSO MAYRA DENISSE'
                if row == 'AMELLALLI CRUZ':
                    alumnos[i] = 'CRUZ CRUZ AMELLALLI MONSERRAT'
                if row == 'AKETZALI HERNANDEZ FLORES':
                    alumnos[i] = 'HERNANDEZ FLORES AKETZALI'
                if row == 'LUCERO MONTOYA PACHECO':
                    alumnos[i] = 'MONTOYA PACHECO LUCERO'
                if row == 'ALEJANDRA RAMOS PARRA':
                    alumnos[i] = 'RAMOS PARRA ALEJANDRA'
                if row == 'YOSELIN TAPIA':
                    alumnos[i] = 'TAPIA RUIZ YOSELIN GUADALUPE'
                if row == 'OMAR MEZA ROSETE':
                    alumnos[i] = 'MEZA ROSETE OMAR ANTONIO'
                if row == 'JOSELIN VERA ARMENDARIZ':
                    alumnos[i] = 'VERA ARMENDARIZ JOSELIN'
                if row == 'ABIGAIL CASTAÑEDA S':
                    alumnos[i] = 'CASTAÑEDA SANCHEZ ABIGAIL'
                if row == 'MARIUS GABRIEL GORI':
                    alumnos[i] = 'GORI URIBE MARIUS GABRIEL'
                if row == 'RODOLFO GARCIA HERNANDEZ':
                    alumnos[i] = 'GARCIA HERNANDEZ JOSE RODOLFO'
                if row == 'EMILIA RENATA PINEDA LOZOYA':
                    alumnos[i] = 'PINEDA LOZOYA EMILIA RENATA'
                if row == 'EDGAR ALEJANDRO RIVERA MACHUCA':
                    alumnos[i] = 'RIVERA MACHUCA EDGAR ALEJANDRO'
                if row == 'XIMENA CHAVEZ':
                    alumnos[i] = 'CHAVEZ SANCHEZ XIMENA'
                if row == 'MARIA FERNANDA FLORES RIVERO':
                    alumnos[i] = 'FLORES RIVERO MARIA FERNANDA'
                if row == 'TANIA CAMILO':
                    alumnos[i] = 'CAMILO BASILIO TANIA ISELA'
                if row == 'CHRISTIAN IRVIN MEJIA ALCANTARA':
                    alumnos[i] = 'MEJIA ALCANTARA CHRISTIAN IRVIN'
                if row == 'SALAZA TREJO JORGE FRANCISCO':
                    alumnos[i] = 'SALAZAR TREJO JORGE FRANCISCO'
                if row == 'PESCINA MEZA EMMANUEL ALEJANDRO':
                    alumnos[i] = 'PESCINA MEZA ALEJANDRO EMMANUEL'

            # asistencia
            for row in alumnos:
                print(row)
                alumno = Alumno.objects.get(nombre__icontains=row)
                print(alumno)
                # clase = Clase.objects.update_or_create(
                #     fecha=fecha, fk_alumno=alumno)
                Clase.objects.create(fecha=fecha, fk_alumno=alumno)
                # print(clase)

            # reader = csv.reader(f)
            # for i, row in enumerate(reader):
            #     fecha = ''
            #     if i == 0 or i == 2 or i == 3 or i == 4:
            #         continue
            #     elif i == 1:
            #         fecha = row[2][0:10]
            #         print(row[2][0:10])
            #     else:
            #         K = ''
            #         res = re.sub(r'[\d\.\-]', '', row[0])
            #         sa = re.sub(
            #             r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
            #             normalize("NFD", res.strip()), 0, re.I
            #         )
            #         sa = normalize( 'NFC', sa)
            #         alumno = Alumno.objects.filter(nombre__icontains=sa)
            #         clase = Clase.objects.aupdate_or_create(
            #             fecha=fecha, fk_alumno=alumno.id)

        form = ArchivoListaModelForm()

    return render(request, 'listaDeAsistenciaApp/ListForm.html', {'form': form})
