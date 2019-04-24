#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mazo import Mazo
from carta import Carta
import random

class PuntosMayor:
    """Juego donde gana la carta mayor, en la partida se reparten tantas cartas como jugadores haya,
        se miran los valores y gana el más alto"""

    def __init__(self, jugadores=[]):
        self.mazo = Mazo() 
        # Mezcla las cartas
        self.jugadores = jugadores
        self.cartas = []
        
        for jugador in range(0,len(jugadores)): # Por cada jugador se saca una carta
            self.carta = self.mazo.saca(1).cartas[0]
            self.cartas.append(self.carta)
    
        self.decideganador()    
        
    def decideganador(self): 
        """En este método hsago una lista donde guardo los valores que se han sacado
           para compararlos con la función max para saber el indice de la carta
           ganadora y el índice del jugador ganador"""
        self.valores = []

        for indice in range(0,len(self.cartas)):  
            print(self.jugadores[indice] + " ha sacado " + str(self.cartas[indice]))
            self.valores.append(self.cartas[indice].valor)

        print(self.valores)

        self.indiceganador = self.valores.index(max(self.valores))   
        self.valorganador = max(self.valores)
        
        if self.valores.count(max(self.valores)) == 1: # No hay empate, se imprime el jugador ganador
           print("El ganador es " + str(self.jugadores[self.indiceganador]))
        
        else:
            self.resuelve_empate() # Se ejecuta el método de desempate

    def resuelve_empate(self):
        """Si hay un empate quitamos de la lista los jugadores que no han sacado
           la carta con valor ganador"""
        jugadores2 = []   
        print('\n'"¡Empate! Haciendo otra ronda ..." + '\n')
        # se quitan las cartas para volver a repartir
        for indice2 in range(0,len(self.jugadores)):
            if self.cartas[indice2].valor == self.valorganador:
               jugadores2.append(self.jugadores[indice2])
        #print(jugadores)
        PuntosMayor(jugadores2)

if __name__ == "__main__":
    PuntosMayor(["Mono", "Monito", "Mona", "Monita"])