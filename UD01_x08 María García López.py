#datos
segundos = int(input("Introduce número de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
Segundos = (segundos % 3600) - (minutos * 60)


#solucion
print(horas, minutos, Segundos, sep=":")

