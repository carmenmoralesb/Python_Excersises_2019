#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def aniobisiesto (anio):
    """Funcion que dado un año dice si es , fue o será bisiesto"""
    if anio%4==0 and anio%100 != 0 or (anio%400==0):
       return True
    else:
       return False

try:
    x = aniobisiesto(1974)
    if x==True:
       print("Es bisiesto")
    else:
       print("No es bisiesto")
except:
    print("Introduce valores numéricos")
