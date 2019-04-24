#!/usr/bin/env python3

totalspam = 0
sumatotal = 0

try:
    with open("mbox-short.txt") as fman:
         for linea in fman:
             if "X-DSPAM-Confidence:" in linea:
                totalspam +=1
                valores = linea.split(" ")
                valornumerico = float(valores[1])
                #print(valornumerico)
                sumatotal += valornumerico
                media = sumatotal/totalspam 
         print(media)
     
except PermissionError:
        print("No se tienen permisos para leer el archivo")
     
except FileNotFoundError:
        print("El fichero no ha sido encontrado")
     
except ZeroDivisionError: # no hay lineas con spam
        print("No hay lineas con ese contenido")