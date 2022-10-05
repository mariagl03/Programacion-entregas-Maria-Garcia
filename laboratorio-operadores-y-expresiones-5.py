hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

finalHour = hour + (mins + dura) // 60
finalMins = (mins + dura) % 60

print(str(finalHour) + ":" + str(finalMins))
print (finalHour, ":", finalMins, sep=" ")
