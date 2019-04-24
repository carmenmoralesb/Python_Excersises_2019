#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import collections

def csvadic(fichero,codificacion="mac-roman",separador=";"):
    """Recibe un fichero CSV y devuelve a una lista de diccionarios a partir del fichero
    utilizando las cabeceras como claves"""
    listadic = []   

    with open(fichero,encoding=codificacion) as fman:
        claves = fman.readline().split(separador)
        #print(claves)
        
        for linea in fman:
            valores = linea.split(separador)
            #print(valores)
            dictemp = {} 
            
            for indice in range(0,len(claves)):
                dictemp[claves[indice].rstrip()] = valores[indice].rstrip()
                listadic.append(dictemp)
        return(listadic)

### PROBANDO

if __name__ == "__main__":
    try:
        x = csvadic("Aemet.csv")
        print(x)  # imprime el primer elemento de la lista, o sea el primer diccionario
    except FileNotFoundError:
        print("Fichero no encontrado")
    except PermissionError:
        print("No tienes los permisos suficientes")