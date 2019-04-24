#!/usr/bin/env python
# -*- coding: utf-8 -*-

palabra = input("Mete una palabra : ")
nuevapalabra1 = ''
nuevapalabra = ''

vocales = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']

for letra in palabra:
    if letra in vocales:
        for i in range(-1, -len(letra) - 1, -1):
            # sacar la cadena con vocales invertida
            nuevapalabra = nuevapalabra + letra[i]
        # saca la palabra sin vocales,reemplaza la vocal por un espacio
        palabra = palabra.replace(letra, "")
        # muestra la palabra con las vocales en mayusculas
        nuevapalabra1 = nuevapalabra1 + letra.upper()
    else:
        nuevapalabra1 = nuevapalabra1 + letra

print(nuevapalabra)
print(nuevapalabra1)
print(palabra)
