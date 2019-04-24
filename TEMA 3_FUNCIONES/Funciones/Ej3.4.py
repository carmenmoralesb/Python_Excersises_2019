#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import math
def distanciavector(x1,x2,y1,y2):
    """Funcion que obtiene la distancia entre dos vectores dadas las coordenadas de X e Y"""
    resultado=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return resultado

try:
    x=distanciavector(2,1,-3,1)
    print("La distancia de los vectores es " + str(x))
except:
    print("Por favor introduce valores numéricos")