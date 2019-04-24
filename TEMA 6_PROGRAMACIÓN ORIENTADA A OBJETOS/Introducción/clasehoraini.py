#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Hora:
    def __init__(self,horas=0,minutos=0, segundos = 0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def imprimeHora(hora):
        print(str(hora.horas) + ":" +
             str(hora.minutos) + ":" +
             str(hora.segundos))

# Prueba del constructor

horaActual = Hora(9,14,30)
horaActual.imprimeHora()
