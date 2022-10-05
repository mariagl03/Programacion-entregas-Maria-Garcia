#datos
print("Cálculo de polínomios de segundo grado (y = ax2 +bx +c)")
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))
x = float(input("Introduce el valor de x: "))

#operación y=ax2 + bx + c
y = a * x ** 2 + b * x + c

#solucion
print("La solución es: ", y)

