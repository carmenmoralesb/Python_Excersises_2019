#!/usr/bin/python3
#Programa que opera los numeros segun la opcion que elijas con control de errores
try:
	opciones = int(input("¿Qué quieres hacer? \n Opción 1: Sumar \n Opción 2: Restar \n Opcion 3: Multiplicar \n Opcion 4: Dividir\n" ))
    
	if opciones <= 4:
		num1=int(input("Introduce un número: "))
		num2=int(input("Introduce un número: "))

		if opciones == 1:
			totalsuma=num1+num2
			print("La suma es: " + str(totalsuma))
	
		elif opciones == 2:
		 	 totalresta=num1 - num2
		 	 print("La resta es: " + str(totalresta))

		elif opciones == 3:
			totalmultiplicar= num1 * num2
			print("La multiplicación es: " + str(totalmultiplicar))

		elif opciones == 4:
			if num2 != 0:
				totaldivision=num1/num2
				print("La división es: " + str(totaldivision))
			else:
			    print("¡No se puede dividir por cero!")
	else:
		print("No es una opción valida")
except:
	print("Introduce valores numéricos, por favor")

