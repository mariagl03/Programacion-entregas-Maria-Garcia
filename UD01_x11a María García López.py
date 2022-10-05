#Entrada: temperaturas
print("Convesión de temperaturas")
print("1. Celsius a Farenheit")
print("2. Farenheit a Celsius")
opcion = input("Opción? ")
temp = float(input("temperatura: "))

#Proceso
tempFinal = temp * 9 / 5 + 32 if opcion == "1" else (temp - 32) * 5 / 9

#Salida
print("Temperatura convertida: ", round(tempFinal, 4), " grados ", "Farenheit" if opcion ==1 else "Celsius")