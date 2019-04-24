#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import math
def areacirculo(diametro):
    """Función que calcula el area de un circulo dado su diametro"""
    
    calculaarea=math.pi*((diametro/2)**2)
    return calculaarea

try:
    x = areacirculo(10)
    print("El area es " + str(x))
except:
    print("Introduce valores numéricos")