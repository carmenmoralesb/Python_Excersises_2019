#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
def adivinarnumero(numero, numeroadivinar): 
    """Función que recibe un numero y un numero random y que dice si lo has adivinado o no"""
    if numero > numeroadivinar:
       return 1
    elif numero < numeroadivinar:
       return 2
    elif (numeroadivinar - 2) == numeror or (numeroadivinar - 1) == numero:
       return 3


#Programa adivinar numero

numeroadivinar = random.randint(1, 100)
intentos = 0 
while intentos < 5:      
      numero = int(input("Intenta adivinar el numero: "))
      intentos += 1
      if intentos == 5:
          print("Has perdido, el numero era " + str(numeroadivinar))
      else:
        if adivinarnumero(numero,numeroadivinar) == 1:
            print("El número a adivinar es MENOR")
        elif adivinarnumero(numero,numeroadivinar) == 2:
            print("El numero a adivinar es MAYOR")
        elif adivinarnumero(numero, numeroadivinar) == 3:
            print("El número a adivinar es 1 unidad o 2 mayor/menor, ¡estás cerca!")

            


