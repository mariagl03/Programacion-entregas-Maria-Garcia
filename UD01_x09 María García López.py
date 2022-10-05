#datos
milimetros = int(input("Introduce número de milímetros:"))
centimetros = int(input("Introduce número de centímetros:"))
metros = int(input("Introduce número de metros:"))

#programa sumar y expresar en centímetros
total = (metros * 100) + centimetros + (milimetros / 10)

#solución
print("La distancia en centímetros es:", total)
