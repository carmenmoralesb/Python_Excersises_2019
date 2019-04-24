#!/usr/bin/env python 
# -*- coding: UTF-8 -*-.

contador=0
numeros=0
suma=0
while contador < 50:
	  contador+=1
	  numeros+=2
	  suma+=numeros
	  print(numeros,end=", ")
print()
print("La suma de todos es " + str(suma)) #igual que el otro