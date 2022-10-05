#datos
entradaadulto = int(input("Número entradas adulto: "))
entradainfantil = int(input("Número entradas infantil: "))

#operación
importebase = entradaadulto * 20 + entradainfantil * 15.5
importetotal = (importebase * 0.95) if (importebase >= 100) else (importebase)

#solución 
print("Importe Base: ", round(importebase, 2), "$")
print("Descuento del 5%" if importebase >= 100 else "Sin descuento")
print("Importe Final: ", round(importetotal, 2), "$")