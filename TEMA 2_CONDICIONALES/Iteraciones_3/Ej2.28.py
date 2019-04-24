#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#Solicitar por teclado un número en hexadecimal y calcular su valor en decimal.
hexadecimal = str(input("Introduce un numero hexadecimal para convertirlo a decimal: "))
exponente = len(hexadecimal)
decimal = 0

for digito in hexadecimal:
    if digito == 'A':
        digito = 10
    elif digito == 'B':
        digito = 11
#segun los valores de ABCDEF voy dandoles el valor en decimal
    elif digito == 'C':
        digito = 12
    elif digito == 'D':
        digito = 13
    elif digito == 'E':
        digito = 14
    elif digito == 'F':
        digito = 15

    exponente -= 1
    base = int(digito) * (16**exponente)
    decimal = decimal + base
print("El numero en decimal es " + str(decimal))

