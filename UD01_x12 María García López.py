#Entrada: Interés bancario
INTERES = 4

ahorros_depositados = float(input("Introduce los ahorros depositados: "))

#Proceso
ahorros_año1 = ahorros_depositados + ahorros_depositados * INTERES/100
ahorros_año2 = ahorros_año1 + ahorros_año1 * INTERES/100
ahorros_año3 = ahorros_año2 + ahorros_año2 * INTERES/100

#Salida
print("Los ahorros tras el primer año son: ", round(ahorros_año1, 2))
print("Los ahorros tras el segundo año son: ", round(ahorros_año2, 2))
print("Los ahorros tras el tercer año son: ", round(ahorros_año3, 2))