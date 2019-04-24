#!/usr/bin/python3
try:
#he metido como numero mayor el primero y luego lo voy comparando
	mayor = int(input("introduce un numero: ")) 
	numero = int(input("Introduce un numero: "))
	
	if mayor > numero > int(input("Introduce un numero ")):
		print("El número mayor es el primero")
#si el primero no es mayor se comparan aqui empezando por el segundo numero
	elif numero > mayor and numero > int(input("Introduce un numero ")):
#mayor=numero
#print(mayor)
		print("El número mayor es el segundo") 
	else:
#si no se cumple el tercero es el mayor
		print("El número mayor es el tercero")

except:
	print("Por favor, introduce valores numéricos")