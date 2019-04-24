#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import math
    
a = int(input("mete un numero: "))
b = int(input("mete un numero: "))
c = int(input("mete un numero: "))
   
discriminante = b**2 - 4 * (a * c)
#el polinomio dado en la actividad
primerasolu = 0
segundasolu = 0

if discriminante > 0:
   x1= (-b+math.sqrt(discriminante))/(2*a)
   x2= (-b-math.sqrt(discriminante))/(2*a)
   print("La primera solución es " + str(x1))
   print("La segunda solución es " + str(x2))
   
   if x1==x2:
      print("La solución única es" + str(x1))   
else:
   print("No hay solución")
