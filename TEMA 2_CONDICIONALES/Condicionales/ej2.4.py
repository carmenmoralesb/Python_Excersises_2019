#!/usr/bin/python3
#programa que te dice si el numero es par o impar
try:
    numero=int(input(("Escribe un número para saber si es par o impar: ")))
    if numero%2==0: #el numero si se divide entre dos tiene un resto cero por tanto es par
    	print("Es par")
    else:
    	print("Es impar")
#si el dato no es el que se espera sale este error
except:
	print("Dato incorrecto, inténtalo de nuevo")