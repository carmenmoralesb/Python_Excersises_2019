#!/usr/bin/env python 
# -*- coding: UTF-8 -*-.
suma1=0
suma2=0
try:
	amigo1 = int(input("Introduce un número: "))
	amigo2 = int(input("Introduce un número: "))
	suma = 0
	
	for divisores1 in range(1,amigo1): 
		if(amigo1%divisores1==0):
			suma1 += divisores1
	for divisores2 in range(1,amigo2):
		if(amigo2%divisores2==0): #aqui he añadido que mire tb los divisores de amigo2 y compare las sumas
			suma2 += divisores2		
	if suma1==amigo2 and suma1==amigo2: #comparo si la suma de los divisores de amigo1 es igual a amigo2 y viceversa
		print("Son amigos :)")
	else:
		print("No son amigos :(")
except:
	print("Introduce números")
