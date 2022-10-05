#Calcular el IVA
#Entrada de Datos
baseImponible = float(input("Introduce la base imponible: "))
iva = int(input("Introduce el % de Iva: "))

# Proceso y salida de información por consola
importeIva = baseImponible * iva / 100
print("El importe del IVA es", round(importeIva, 2), "€")

importeTotal = baseImponible + importeIva
print("El importe total es de", round(importeTotal, 2), "€")