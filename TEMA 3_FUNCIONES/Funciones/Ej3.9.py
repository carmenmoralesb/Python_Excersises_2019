#!/usr/bin/env python
# -*- coding: utf-8 -*-

def digitosbinarios(decimal):
    """Funcion que saca el numero de digitos de un numero binario"""
    contadordig=0
    binario = ''

    if decimal != 1:
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
            contadordig=len(str(decimal)+binario) #contar los elementos de la cadena resultante
        return contadordig
    else:
        return decimal

try:
    x = digitosbinarios(1)
    print("El número de digitos necesarios es " + str(x))
except:
    print("Introduce números")