#!/usr/bin/python3
#Programa que te dice de una entrada de tres numeros cual es mayor
try:
	num1=int(input("Introduce un número: "))
	num2=int(input("Introduce un número: "))
	num3=int(input("Introduce un número: "))
	    
	if num1 > num2 and num1 > num3:
		print("El numero " + str(num1) + " es mayor")
	elif num2 > num1 and num2 > num3:
		print("El numero " + str(num2) + " es mayor")
	elif num3 > num1 and num3 > num2:
		print("El numero " + str(num3) + " es mayor")
except:
	print("Introduce números, por favor")