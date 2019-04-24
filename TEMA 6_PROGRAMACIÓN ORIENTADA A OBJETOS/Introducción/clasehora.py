#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Hora:
    hora = Hora()
    hora.horas = 11
    hora.minutos = 59
    hora.segundos = 30

def sumaHora(t1,t2):
    """crea un nuevo objeto Hora que inicializa sus atributos y devuelve
       una referencia al nuevo objeto. A esto se le llama funcion pura porque no modifica
       ninguno de los objetos que se le pasan"""   
    suma = Hora()
    suma.horas = t1.horas + t2.horas
    suma.minutos = t1.minutos + t2.minutos
    suma.segundos = t1.segundos + t2.segundos
    return suma

# La salida puede ser correcta pero no trata elcaso de que los segundos o minutos
# sumen mas que 60, no es quizá la solución mas eficiente

def sumaHora(t1,t2):
    """crea un nuevo objeto Hora que inicializa sus atributos y devuelve
       una referencia al nuevo objeto. A esto se le llama funcion pura porque no modifica
       ninguno de los objetos que se le pasan"""   
    suma = Hora()
    suma.horas = t1.horas + t2.horas
    suma.minutos = t1.minutos + t2.minutos
    suma.segundos = t1.segundos + t2.segundos

    if suma.segundos >= 60:
       suma.segundos = suma.segundos - 60 
       suma.minutos = suma.minutos + 1
    if suma.minutos >= 60:
        suma.minutos = suma.minutos - 60
        suma.horas = suma.horas + 1
    return suma


# Mediante esta función podemos incrementar la hora
# de manera correcta, no es una solución eficiente

def incremento(hora,segundos):
    hora.segundos = hora.segundos + segundos
    
    while hora.segundos >= 60:
        hora.segundos = hora.segundos - 60
        hora.minutos = hora.minutos + 1
    
    while hora.minutos >= 60:
        hora.minutos = hora.minutos - 60
        hora.horas = hora.horas + 1