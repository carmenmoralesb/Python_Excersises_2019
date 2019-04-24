#!/usr/local/bin/python3
from mazo import Mazo
from carta import Carta
import random

class Mona:
    def __init__(self, jugadores=["Mona", "Mono"]):
        # Reordenamos jugadores para evitar que el primero pierda más
        random.shuffle(jugadores)
        # Crea mazo completo y retira Rey de Copas
        self.mazo = Mazo()
        self.mazo.dame(Carta("Rey", "Copas"))
        cartas_mazo = len(self.mazo)
        print(len(self.mazo))
        
        # Crea las listas de jugadores y manos
        self.jugadores = jugadores
        self.manos = []
        for nombre in jugadores:
            self.manos.append(Mazo([]))
        
        # Reparte las cartas
        for i in range(len(jugadores)):
            self.manos[i] = self.mazo.saca(cartas_mazo//len(self.jugadores))
        resto_cartas = len(self.mazo)
        # Reparte el resto de cartas
        for i in range(resto_cartas):
            self.manos[i].mete(self.mazo.saca(1))
        self.juego()
        
    def juego(self):
        # Se eliminan las parejas en el reparto inicial
        for i in range(len(self.jugadores)):
            self.elimina_parejas(self.manos[i])
            if len(self.manos[i])==0:
                del self.jugadores[i]
                del self.manos[i]
                break

        while len(self.jugadores)>1:
            for i in range(len(self.jugadores)):
                self.elimina_parejas(self.manos[i])
                if len(self.manos[i])==0:
                    del self.jugadores[i]
                    del self.manos[i]
                    break
                # Calculo el siguiente jugador
                siguiente = (i+1) % len(self.jugadores)
                # Roba carta
                self.manos[i].mete(self.manos[siguiente].saca(1))
                self.manos[i].mezcla()
                print(self.manos[i])
                # Si se queda sin cartas sale del juego
                self.elimina_parejas(self.manos[i])
                print(self.manos[i])
                if len(self.manos[i])==0:
                    del self.jugadores[i]
                    del self.manos[i]
                    break
                
        print(self.jugadores[0] + " ha perdido...")

    def elimina_parejas(self, mano):
        eliminadas = True
        while eliminadas:
            eliminadas = False
            for i in range(len(mano)-1):
                carta_actual = mano.cartas[i]
                for j in range(i+1, len(mano)):
                    if carta_actual.valor == mano.cartas[j].valor:
                        del mano.cartas[j]
                        del mano.cartas[i]
                        eliminadas = True
                        break
                if eliminadas:
                    break


if __name__ == "__main__":
    Mona(["Ivan", "Alejandro", "Joaquin", "Mario"])