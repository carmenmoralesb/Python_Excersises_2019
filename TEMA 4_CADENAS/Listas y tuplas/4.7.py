#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quitarDuplicados(lista):
	"""quita los duplicados en una lista y devuelve los elementos que se han eliminado"""
	sindupli = [] #lista para meter elementos unicos
	dupli = []
	duplisinrepe = []

	for elemento in lista:
		if lista.count(elemento) > 1:
			dupli.append(elemento)
# Añade los elementos repetidos a una lista y luego quita los duplicados de esa misma lista,
# no se si habra una forma mas facil
			for elementos in dupli:
				if elementos not in sindupli:
					duplisinrepe.append(elementos)
	
		if elemento not in sindupli:
			sindupli.append(elemento)
			sindupli.sort()

	return duplisinrepe
	#return sindupli
	
try:
	lista = [10,5,6,7,8,8,9,5,10]
	x = quitarDuplicados(lista)

	print("Estos son los elementos que se han eliminado")
	print(x)
except ValueError:
	print("Ha habido un error")
