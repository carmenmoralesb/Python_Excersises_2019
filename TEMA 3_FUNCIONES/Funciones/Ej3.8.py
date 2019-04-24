#!/usr/bin/env python
# -*- coding: utf-8 -*-

def añobisiesto(año):
    """devuelve true si un año es bisiesto y false si no lo es"""
    if año % 4 == 0 and año % 100 != 0 or (año % 400 == 0):
        return True
    else:
        return False

def esvalida(dia,mes,año):
    """"devuelve true si la fecha es valida y false si no lo es"""
    mes31=[1,3,5,7,8,10]
    mes30=[4,9,11]       

    if not añobisiesto(año):
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

##########################################
    
dia = int(input("Introduce el dia actual: "))
mes = int(input("Introduce el mes actual: "))
año = int(input("Introduce el año actual: "))
    
dianacimiento = int(input("Introduce tu dia de nacimiento: "))
mesnacimiento = int(input("Introduce tu mes de nacimiento: "))
añonacimiento = int(input("Introduce tu año de nacimiento: "))

if esvalida(dia,mes,año)==True and esvalida(dianacimiento,mesnacimiento,añonacimiento)==True:
   if año - añonacimiento < 20:
      print("Eres menor de 20")
   elif año - añonacimiento > 20:
      print("Eres mayor de 20 años")
   elif año - añonacimiento == 20:
      if mes < mesnacimiento:
         print("Eres menor de 20 años")
      elif mes == mesnacimiento and dianacimiento < dia:
         print("Eres menor de 20 años")
      elif mes ==mesnacimiento and dianacimiento > dia:
          print("Eres mayor de 20 años")
      elif mes == mesnacimiento and dianacimiento==dia: #si naces el mismo dia
          print("Eres mayor de 20,¡felicidades!")  
else:
    print("No has escrito bien las fechas")
