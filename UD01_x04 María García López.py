velocidadMaxima = int(input("Introduce la velocidad máxima permitida: "))
velocidadVehiculo = int(input("Introduce la velocidad del vehiculo: "))

resultado = True if ((velocidadMaxima / 2) <= velocidadVehiculo<=velocidadMaxima) else False

print("Velocidad adecuada?", resultado)

#Casos de prueba:
#velocidadMaxima  velocidadVehiculo  resultado
#   80              70                  True
#   80              80                  True
#   80              81                  False
#   80              40                  True
#   80              39                  False