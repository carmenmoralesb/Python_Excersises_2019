#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random 
def hayDuplicados(lista):
    """Devuelve True si hay duplicados y False si no los hay"""
    duplicados = []

    for elementos in lista:
        if lista.count(elementos) > 1:
            duplicados.append(elementos)   

    if len(duplicados) == 0: # if bien indentado entro del for
        return False
    else:
        return True

# Probando si funciona

lista = [1,2,3,4,5,6,6]
x = hayDuplicados(lista)

if x == True:
    print("Hay duplicados" + '\n')
else:
    print("No hay duplicados" + '\n')

 #Numeros aleatorios

try:
    while True:
        lista = [random.randrange(100) for i in range(20)]

        if hayDuplicados(lista) == True:
            continue
        else:
            print(lista)
            break
except:
    print("Ha habido un error")




