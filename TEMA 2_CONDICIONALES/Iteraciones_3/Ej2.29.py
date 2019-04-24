#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

#Solicitar por teclado una cantidad de dinero con decimales hasta los céntimos y calcular el cambio en dinerototal y monedas de  curso legal.

dinerototal = float(input(" Dinero a cambiar: "))
listadeeuros = [500,200,100,50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]
for valor in listadeeuros:
      division=dinerototal/valor
      dinerototal=dinerototal%valor #elresto
      division =int(float(division)) #pasarlo a entero para que no me salgan 2.00 billetes

      if division!=0:
            if valor>=5:
                  if division>1:
                        print (str(division) + " billete(s) de " + str(valor) + " Euros")
                  else:
                        print (str(division)  + " billete(s) de " + str(valor) + " Euros")
            else:
                  if division>=2:
                        print (str(division)  + " moneda(s) de " + str(valor) + " Euros")
                  else:      
                        if valor<=1: 
                              print (str(division)  + " moneda(s) de " + str(valor) + " Euros")
                        else:
                              print (str(division)  +  "  moneda(s) de " + str(valor) + " Euros")

                              if valor <= 0.05:
                                    division = int((dinerototal * 100) / (valor * 100))
                                    print(str(division) + "  moneda(s) de " + str(valor) + " Euros")