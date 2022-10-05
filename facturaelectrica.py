#Entrada
potencia_punta = float(input("Introduce la Potencia Punta: "))
potencia_valle = float(input("Introduce la Potencia Valle: "))
consumo_punta = float(input("Introduce el Consumo Punto: "))
consumo_llano = float(input("Introduce el Consumo Llano: "))
consumo_valle = float(input("Introduce el Consumo Valle: "))
numero_dias = int(input("Introduce el número de días: "))

#Proceso
terminofijo = ((3.45 * potencia_punta * 30) / numero_dias) + ((3.45 * potencia_valle * 30) / 365 ) + (3.45 * potencia_punta *30) / 365
terminovariable = (56 * consumo_punta) + (48 * consumo_llano) + (96 * consumo_valle) + (200 * 30 * / 365)

#Salida
print("Días facturables en total: ", numero_dias, " días")
print("Término fijo: ", terminofijo)