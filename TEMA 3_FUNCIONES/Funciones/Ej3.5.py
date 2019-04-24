#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#:1+x+x2+x3 +...+xn

def progresion (x,n):
    """Función que devuelve la suma de una progresion dado un rango"""
    suma=1
    for exp in range(1,n+1):
        suma=suma+(x**exp)
    return suma

x = progresion(6,3)
print(x)