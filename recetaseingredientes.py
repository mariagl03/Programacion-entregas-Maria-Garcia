#Entrada
receta = "Compota de manzana"
URL = "https://www.recetasderechupete.com/compota-de-manzana-casera/12509/"
personas = 6
cantidad_manzana = 1500
cantidad_agua = 330
cantidad_azucar = 120
cantidad_limon = 1

#Proceso
print(receta)
print(URL)
personas2 = int(input("Escribe la cantidad de personas: "))
manzana = (cantidad_manzana * personas2) / personas
agua = (cantidad_agua * personas2) / personas
azucar = (cantidad_azucar * personas2) / personas
limon = (cantidad_limon * personas2) / personas

#Salida
print("Para hacer ", receta, " para ", personas2, " personas se necesita:")
print(round(manzana,2), "g de manzanas")
print(round(agua,2), "ml de agua")
print(round(azucar,2), "g de azúcar")
print(round(limon,2), " cucharaditas de limón")
