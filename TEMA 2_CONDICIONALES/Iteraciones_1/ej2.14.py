#!/usr/bin/env python 
# -*- coding: UTF-8 -*-.
listanumero=[]
principio=0

while principio in range(0,52):
	principio+=1
	listanumero.append(principio)
	for numeros in listanumero:
		if numeros%2!=0 and numeros!=principio:
			numeros+=2
		if numeros%2==0:
			numeros=52-numeros
	print(numeros,end=", ")

#no sé si esto esta bien
