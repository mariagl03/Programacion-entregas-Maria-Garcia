#Entrada: Interés compuesto
#Fórmula P x (1 + r/n)nt
invertir = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (Ej. 4.2%): "))
años = int(input("Introduce el número de años: "))

#Proceso
resultado = invertir * (1 + interes / 100) ** años

#Salida
print("El capital resultante es: ", round(resultado, 2))
