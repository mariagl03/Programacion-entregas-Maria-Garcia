#datos
#hectárea = 100 x 100 metros = 10000 m2

hectareas = float(input("Número de hectáreas:"))

#proceso
#Campo de fútbol: 105 x 70 metros 
#Cancha de baloncesto: 28 x 15 metros
#Pista de tenis: 23,77 x 10,97 metros
#Parque del Retiro: 125 hectáreas

campofutbol = (hectareas * 1000 ) / (105 * 70)
canchabaloncesto = (hectareas * 1000) / (28 * 15)
pistatenis = (hectareas * 1000) / (23.77 * 10.97)
parqueretiro = hectareas / 125

#solucion

print("El número de hectáreas equivale a:")
print(campofutbol, " campos de fútbol")
print(canchabaloncesto, " canchas de baloncesto")
print(pistatenis, " pistas de tenis")
print(parqueretiro, " arques de retiro")