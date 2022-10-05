#Entrada : nombre módulo y número horas

modulo = "Programación"
horas = 240
duracionsesion = 50
minutos = horas * 60
poercentaje_apercibimiento = 6
porcentaje_perdida = 10

#Proceso: Calcular nº sesiones, calcular 6% apercibimiento, calcular 10% pérdida evaluación

numerosesiones = minutos / duracionsesion
apercibimiento = numerosesiones * poercentaje_apercibimiento / 100
evaluacion = numerosesiones * porcentaje_perdida / 100

#Mostrar resultado

print("Hay un total de ", int(numerosesiones), " sesiones de ", modulo)
print("Máximo faltas para apercibimiento: ", int(apercibimiento,))
print("Máximo faltas para perdida de la evaluación: ", int(evaluacion,))

#Entrada: Faltas alumno

faltas = int(input("Número de faltas del alumno: "))
Apercibimiento = faltas > apercibimiento
Evaluacion = faltas > evaluacion 

#Salida: estado

print("Apercibimiento" if Apercibimiento else "")
print("Pérdida de Evaluación Continua" if Evaluacion else "") 