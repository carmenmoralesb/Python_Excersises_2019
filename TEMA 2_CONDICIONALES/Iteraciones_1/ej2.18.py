#!/usr/bin/env python 
# -*- coding: UTF-8 -*-.

numero = int(input("Introduce un número: "))
listafactor = []

for factor1 in range(0,numero+1):
	if factor1!=1:
		listafactor.append(factor1)
		for factores in listafactor:
			if factor1*factores==numero:
				print(str(factores) + '*' + str(factor1),end=", ")
				if factores!=factor1:
					print(str(factor1) + '*' + str(factores),end=", ")
print()

#esto lo mejorare en el proximo envio si me da tiempo