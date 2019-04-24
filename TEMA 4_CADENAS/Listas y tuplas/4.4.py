#!/usr/bin/env python
# -*- coding: utf-8 -*-

def borrarExtremos(lista):
    """Borra los valores maximo y minimo de una lista
    devuelve la media calculada"""

    del lista[0]
    del lista[-1]

#Programa que calcula la media ordenando la lista y eliminando los extremos con la función anterior
try:
    lista = [5,6,7,8,5,9,8]
    lista.sort()
    borrarExtremos(lista)
    media = sum(lista) / len(lista)
    print("La media es " + str(media))
except:
    print("Ha habido un error")