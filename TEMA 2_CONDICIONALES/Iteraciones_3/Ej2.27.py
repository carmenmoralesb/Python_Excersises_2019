#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#Solicitar un número en decimal por teclado y convertirlo a binario.
decimal = int(input("Introduce un numero decimal para convertirlo a binario: "))
binario = '' # cadenavacia

if decimal != 1:
	while decimal//2 != 0:
		binario = str(decimal % 2) + binario
		decimal = decimal//2
	print("El número binario es " + (str(decimal) + binario))
else:
	print("El numero binario es " + (decimal))
