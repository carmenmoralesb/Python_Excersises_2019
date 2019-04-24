#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def añobisiesto(año):
    """devuelve true si un año es bisiesto y false si no lo es"""
    if año % 4 == 0 and año % 100 != 0 or (año % 400 == 0):
        return True
    else:
        return False

def esvalida(dia,mes,año):
    """"devuelve false si la fecha que recibe no es válida y true si lo es"""
    mes31=[1,3,5,7,8,10]
    mes30=[4,9,11]
      
    if not añobisiesto(año): #agrupo meses de 31 dias y de 30 y comparacion para febrero y las comparaciones del ejercicio anterior
       if mes in mes31 and dia > 31:
          return False
       elif mes in mes30 and dia > 30:
          return False
       elif mes == 2 and dia > 28:
          return False
       else:
          return True
    else:
        if mes in mes31 and dia > 31:
            return False
        elif mes in mes30 and dia > 30:
            return False
        elif mes==2 and dia>29:
            return False
        else:
            return True

try:
    #x=esvalida(29,2,1964)
    #x = esvalida(49,3,2018)
    x = esvalida(26,4,2018)
    if x==True:
        print("La fecha es válida")
    else:
        print("La fecha no es válida")
except:
    print("Introduce valores numéricos")