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



print(Calificaciones.calificaciones('calificaciones'))
print(Calificaciones.nota_final('nota_final'))
print(Calificaciones.aprobados_suspensos('aprobados', 'suspensos'))

