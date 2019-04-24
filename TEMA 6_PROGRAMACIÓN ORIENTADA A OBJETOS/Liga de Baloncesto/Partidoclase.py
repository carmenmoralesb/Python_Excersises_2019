#!/usr/local/bin/python3

from Equipoclase import Equipo
from datetime import date

class Partido:
    """Clase Partido donde se crea el tipo de dato partido, el cual tiene un equipo local un visitante y puntuaciones para ambos"""
    def __init__(self,equipolocal,puntoslocal,equipovisitante,puntosvisitante,fecha = date.today()):
        self.equipolocal = equipolocal
        self.equipovisitante = equipovisitante
        self.puntoslocal = puntoslocal
        self.puntosvisitante = puntosvisitante
        self.fecha = fecha

        self.resultado = str(self.fecha) + " " + self.equipolocal + " " + str(self.puntoslocal) + " " + self.equipovisitante + " " + str(self.puntosvisitante)

    def __str__(self):
        return self.resultado

if __name__ == "__main__":
    # CREANDO PUNTUACION
    Puntuacion1 = Partido('Cadiz Wheels',40,'Victoria Bedouins',30)