#Entrada de datos
distancia = float(input("Introduce la distancia del trayecto en km:"))
consumo = float(input("Introduce el consumo de litros cada 100km:"))
precio = float(input("Introduce el precio de cada lito de combustible:"))
pasajeros = float(input("Introduce el número de pasajeros:"))

#calculo
importetotal = (distancia/100) * consumo * precio
importemedioporkm = importetotal / distancia
importepasajero = importetotal / pasajeros

#resultado
print("El importe total es: ")  
print(round(importetotal,2))
print("El importe medio por km es: ") 
print(round(importemedioporkm,2))
print("El importe a aportar por cada pasajero es: ")
print(round(importepasajero,2))
