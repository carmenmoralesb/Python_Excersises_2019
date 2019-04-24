#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
import lee_csv
import escribe_csv

# PROGRAMA PARA GUARDAR EN UN 
# CSV NUEVO LAS TEMPERATURAS MEDIAS
# UTILIZANDO LAS FUNCIONES CREADASA ANTERIORMENTE

try:
    while True:
        listaprovincias = lee_csv.csvadic("Estaciones.csv")
        listatemperaturas = lee_csv.csvadic("Aemet.csv")
        provinciasinrepetir = []
        #contador = 0
        nuevosdatos = [] #datos q se escribirán en el csv
    # pasaracsv = dicacsv("pruebafichero.csv",listadotemperaturas)        

        for dicprov in listaprovincias:
            if dicprov["PROVINCIA"] not in provinciasinrepetir:
                provinciasinrepetir.append((dicprov["PROVINCIA"])) # hago una lista con las provincias para no repetirlas
        
        for provincias in provinciasinrepetir:
            print(provincias) # Me faltan las columnas que no tengo forma de formatear bien la salida..

        provincia = input("Elige una provincia de la lista: ")
        
        if provincia not in provinciasinrepetir:
           print("No es una provincia correcta")
           time.sleep(10)
        
        else:
            for dictempe in listatemperaturas: # si el diccionario de temperaturas contiene la provincia, lo añado a nuevosdatos para posteriormente escribirlo
                if dictempe["Provincia"] == provincia:
                   #print(dictempe) 
                   nuevosdatos.append(dictempe) 

            ficheroguardar = input("Elige donde se guardarán los datos de las estaciones: ") # nombre de fichero
            
            if os.path.isfile(ficheroguardar):
                encontrado = True
            
            else:
                encontrado = False
          
            if encontrado:
                confirmar = input("Este fichero ya existe,¿Quieres sobreescribirlo? (S/N): ")
                
                if confirmar == "S":
                    escribe_csv.dicacsv(ficheroguardar,nuevosdatos)
                    print("¡Datos escritos en " + ficheroguardar + " !") # si confirma la respuesta se escribe el fichero
                    break
                
                else: # si es no se vuelve a pedir una provincia y un nombre de fichero
                    continue
            else:
                escribe_csv.dicacsv(ficheroguardar,nuevosdatos) #si no se encuentra el fichero se guardará
                print("¡Datos escritos en " + ficheroguardar + " !")
                break
               
except PermissionError:
    print("Error, no tienes permisos necesarios")

except FileNotFoundError:
    print("Fichero no encontrado")
