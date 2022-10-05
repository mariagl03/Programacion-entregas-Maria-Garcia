numero = int(input("Introduce un número entero: "))

resto = numero % 7

solucion = 0 if (resto == 0) else (7 - resto)

#Otra solucion: solucion = ((numero // 7) + 1) *7 - numero



print("Para obtener un múltiplo de 7 debemos sumar",solucion,"a",numero)

#numero  resto  solucion
#5       5      2
#13      6      1
#9       2      5
#7       0      0
