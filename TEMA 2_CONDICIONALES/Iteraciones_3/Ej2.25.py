#!/usr/bin/env python 
# -*- coding: utf-8 -*-

mes31 = [1, 3, 5, 7, 8, 10, 12]
mes30 = [4, 9, 11]

dia=int(input("Introduce el dia: "))
mes=int(input("Introduce el mes: "))
año = int(input("Introduce el año "))

primerdia = input("Introduce en que dia fue 1 de enero ")

if primerdia == 'L':
   primerdia = 1
elif primerdia == 'M':
   primerdia = 2
elif primerdia == 'X':
   primerdia = 3
elif primerdia == 'J':
   primerdia = 4
elif primerdia == 'V':
   primerdia = 5
elif primerdia == 'S':
   primerdia = 6
elif primerdia == 'D':
   primerdia = 7

elif mes == 1:
   modulo = (primerdia + 31 - dia) % 7
   print(modulo)
   
elif mes == 2:
   modulo = (primerdia + 31) % 7
   print(modulo)

elif mes == 3:
   modulo = (primerdia + 31 + 28) % 7
   print(modulo)
   
elif mes == 4:
   modulo = (primerdia + 31 + 28 + 31) % 7
   print(modulo)
   
elif mes == 5:
   modulo = (primerdia + 31 + 28 + 30 + 3) % 7
   print(modulo)
   
elif mes == 6:
   modulo = modulo = (primerdia + 31 + 28 + 30 + 31 + 30 + dia) % 7
   print(modulo)
   
elif mes == 7:
   modulo = (primerdia + 31 + 28 + 30 + 31 + 30 + 3 + dia) % 7
   print(modulo)
   
elif mes == 8:
   modulo = (primerdia + 31 + 28 + 30 + 31 + 30 + 31 + 3 + dia) % 7
   print(modulo)
   
elif mes == 9:
   modulo = (primerdia + 31 + 28 + 30 + 31 + 30 + 31 + 30 + 31 + dia) % 7
   print(modulo)
   
elif mes == 10:
   modulo = (primerdia + 31 + 28 + 30 + 31 + 30 + 31 + 30 + 31 + dia) % 7
   print(modulo)

elif mes == 11:
   modulo = (primerdia + 31 + 28 + 30 + 31 + 30 + 31 + 30 + 31 + dia) % 7
   print(modulo)
   
elif mes == 12:
   modulo = (primerdia + 31 + 28 + 30 + 31 + 30 + 31 + 30 + 31 + dia) % 7
   print(modulo)
      
   if modulo == 0:
      print("fue lunes")
   elif modulo == 1:
      print("fue martes")
   elif modulo == 2:
      print("fue miercoles")
   elif modulo == 3:
      print("fue jueves")
   elif modulo == 4:
      print("fue viernes")
   elif modulo == 5:
      print("fue sabado")
   elif modulo == 6:
      print("fue domingo")
