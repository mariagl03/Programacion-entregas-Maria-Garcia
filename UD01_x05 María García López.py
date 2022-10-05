#datos
n = float(input("Introduce el primer número: "))
m = float(input("Introduce el segundo número: "))

#operación: n + x es múltiplo de m
nm = (m % n) if (n < m) else (n % m)

#solucion
print("Hay que sumar a ", n,": ", nm)
