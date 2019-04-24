#!/usr/bin/env python
# -*- coding: utf-8 -*-

def esPalindromo(lista):
	"""recibe una lista y mira si hay palindromos, si los hay los mete en una lista nueva"""
	listapalindromos = []
	
	for palabra in lista:
		inversa = palabra[::-1] # slice para invertir la palabra y meterla en la variable inversa  

		if palabra == inversa: 
			listapalindromos.append(palabra) # si es igual se mete en la lista
	return listapalindromos

try:
	lista = ['rallar','eje','salas','banana','galleta']
	x = esPalindromo(lista)
	print(x) # arreglada la función
except:
	print("Ha habido un error")
