#!/usr/bin/env python3

import sys

try:
    fichero = sys.argv[2]
    patron = sys.argv[1]
    opciones = sys.argv[3:]
    opcionesdisponibles = ['-l','-t'] 

    lineaparece = [] # linea + numero de linea
    numerolinea = '' 
    sinopcion = [] # lineas donde aparece, sin numero de linea

    contadorpatron = 0 # veces que se repite la palabra o el patron
    contadorlineas1 = 0 # numero de linea donde aparece
    contadorlineas = 0 # numero de lineas en als que aparece

    with open(fichero,'r') as fman:                 
        for linea in fman:
            contadorlineas += 1 
            if patron in linea:
                contadorpatron += linea.count(patron) # veces q aparece una palabra
                contadorlineas1 += 1
                sinopcion.append(linea)
                numerolinea = linea[:-1] + "  " + str(contadorlineas)
                lineaparece.append(numerolinea)
        
        if len(sys.argv) == 4:
            if sys.argv[3] in opcionesdisponibles:
                if '-l' in opciones: # si esta el comando -l en las opciones
                    for linea in lineaparece:
                        print(linea)
                
                elif '-t' in opciones: # si está el comando -t en las opciones
                    print("El patrón aparece en " + str(contadorlineas1) + " lineas y " + str(contadorpatron) + " veces")
            else:
                print("Comando incorrecto, las opcione son -l -t")
        
        elif len(sys.argv) > 4: # si uso mas de dos comandos
            if sys.argv[3] in opcionesdisponibles and sys.argv[4] in opcionesdisponibles:
                for linea in lineaparece:
                    print(linea)
                    print( "El patrón aparece en " + str(contadorlineas1) + " lineas y " + str(contadorpatron) + " veces" )
            else:
                print("Comando incorrecto, las opciones son -l -t")
        
        elif len(opciones) < 1:
             for linea in sinopcion:
                 print(linea)

        else:
            print("Ayuda: ej5.1.py [patron][fichero][opciones]")

except PermissionError:
    print("No se tienen los permisos necesarios")

except FileNotFoundError:
    print("No se encuentra")

# sys.argv[0] -> ejecutable
# sys.argv[1] -> patron
# sys.argv[2] -> fichero
# sys.argv[3] ->opciones