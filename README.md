<h1 align="center">	Trabajar con archivos</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Ejercicio_archivos_POO)

***
<h2>¿De qué trata esta tarea?</h2>

**En este ejercicio nos piden lo siguiente:** 

*El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:*

*Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.*

*Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.*

*Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.*


***

<h2>Resolución (Utilizando Pandas)</h2>

**Código**

```
import pandas as pd #Libreria para trabajar con dataframes
#Creamos un DataFrame desde la url del fichero csv
datos = pd.read_csv('/Users/hectorbernaltrujillo/Documents/informática/Programación python/Ejercicio_archivos_POO/calificaciones (1).csv', sep=',') #Separador de campos
#A continuacion, vamos a dejar tan solo en el fichero los datos no nulos con .dropna()
datos = datos.dropna()
#Eliminamos el caracter % de la columna 'Asistencia' y la convertimos a float
datos['Asistencia'] = datos['Asistencia'].str.replace('%','').astype(float)

class Calificaciones:
    def __init__(self, calificaciones, aprobados, suspensos):
        self.calificaciones = calificaciones
        self.aprobados = aprobados
        self.suspensos = suspensos

#Creamos una función que el fichero de calificaciones (1).csv y devuelva una lista de diccionarios, donde cada diccionario contiene la informacion de los examenes y la asistencia de un alumno. Ordenamos la lista por apellido y nombre de alumno
    def calificaciones(self):
        calificaciones = []
        for i in range(len(datos)):
            calificaciones.append({'Nombre': datos['Nombre'][i], 'Apellido': datos['Apellido'][i], 'Asistencia': datos['Asistencia'][i], 'Examen 1': datos['Parcial 1'][i], 'Examen 2': datos['Parcial 2'][i]})
        calificaciones.sort(key=lambda x: x['Apellido']) #Ordenamos la lista por apellido para ello usamos la funcion sort()
        return calificaciones

    def nota_final(self):
        #Creamos una nueva columna con la nota de los parciales multiplicados por 0.3 mas la nota de las practicas multiplicada por 0.4
        datos['Nota final'] = datos['Parcial 1'] * 0.3 + datos['Parcial 2'] * 0.3 + datos['Practicas'] * 0.4
        return datos

    def aprobados_suspensos(self):
        #Creamos una funcion que nos indique si el alumno está aprobado o suspenso, para ello asistencia tiene que ser mayor o igual a 75% , nota examenes parciales tiene que ser mayor o igual a 4, nota practicas tiene que ser mayor o igual a 4 y nota final tiene que ser mayor o igual a 5
        #Creamos una lista vacia para almacenar los aprobados y una para los suspensos
        aprobados = []
        suspensos = []
        for i in range(len(datos)):
            if datos['Asistencia'][i] >= 75 and datos['Examen 1'] >= 4 and datos['Examen 2'] >= 4 and datos['Practicas'] >= 4 and datos['Nota final'] >= 5:
                aprobados.append(datos['Nombre'][i])
            else:
                suspensos.append(datos['Nombre'][i])
        return aprobados, suspensos

```



***

**UML:**

<img width="266" alt="image" src="https://user-images.githubusercontent.com/91721875/166509808-1e1cb73d-79ef-4775-b6dc-7bf2d230f47a.png">

