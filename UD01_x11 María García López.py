#datos
print("Pasar de horas, minutos y segundos a segundos")
horas = int(input("Introduzca número de horas: "))
minutos = int(input("Introduzca número de minutos: "))
segundos = int(input("Introduzca número de segundos: "))

#operación a segundos
total = (horas * 3600) + (minutos * 60) + segundos

#solución
print("La solución es:", total, "segundos")