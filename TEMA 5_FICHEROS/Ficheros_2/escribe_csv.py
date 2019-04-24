#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lee_csv

def dicacsv(fichero,lista):
    """Recibe un fichero y una lista de diccionarios que fue creada a partir de un CSV
        en dicho fichero se escribirán los datos de todos los diccionarios"""
    
    with open(fichero,'w') as fman:
         # con la primera linea saco las cabeceras, cogiendo las claves de cualquier diccionario de la lista
         cabeceras = (';'.join(lista[0].keys())) + '\n'
         fman.write(cabeceras)
         # para cada diccionario, escribo los valores
         for diccionario in lista:
             fman.write((';'.join(diccionario.values())) + '\n')
         return()

# ### PROBANDO

if __name__ == "__main__":
    try:
        listadic = csvadic("Estaciones.csv")
        pasaracsv = dicacsv("pruebadic.csv",listadic)
        print('Datos escritos correctamente')
    except FileNotFoundError:
        print("Fichero no encontrado")
    except PermissionError:
        print("No tienes permiso para leer el fichero")