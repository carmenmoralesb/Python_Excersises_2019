#!/usr/local/bin/python3
from carta import Carta
import random
import copy

class Mazo:
    def __init__(self, cartas=None):
        if cartas == None:
            self.baraja_completa()
        elif type(cartas) == type(Mazo()):
            self.cartas = copy.copy(cartas.cartas)
        else:
            # TODO: Comprobar que cartas es una lista de objetos Carta
            self.cartas = copy.copy(cartas)
    
    def __str__(self):
        resultado = ""
        contador = 0
        for carta in self.cartas:
            contador += 1
            resultado += str(contador) + " - " + str(carta) + "\n"
        if not resultado:
            resultado = "¡Mazo vacío!\n"
        return resultado
    
    def __len__(self):
        return len(self.cartas)

    def baraja_completa(self):
        self.cartas = list()
        # Estilo Python
        for palo in Carta.palos:
            # HACK: Se usa una porción de los valores para eliminar el primero
            for valor in Carta.valores[1:]:
                self.cartas.append(Carta(valor,palo))
        # Estilo C++
        #for i in range(len(palos)):
        #    for j in range(1, len(valores)):
        #        self.cartas.append(Carta(j,i))
        self.mezcla()
        
    def mezcla(self):
        #print(self)
        random.shuffle(self.cartas)
    
    def ordena(self):
        self.cartas.sort()
    
    def saca(self, n=1):
        resultado = list()
        for i in range(n):
            if len(self.cartas)==0:
                break
            resultado.append(self.cartas.pop())
        return Mazo(resultado)
    
    def dame(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            return True
        return False

    def mete(self, mazo):
        self.cartas.extend(mazo.cartas)

if __name__ == "__main__":
    m1 = Mazo()
    if m1.dame(Carta("Rey", "Copas")):
        print("Sacado/a Rey Copas")
    if not m1.dame(Carta("Rey", "Copas")):
        print("No había Rey Copas")
    m2 = m1.saca(10)
    m3 = m1.saca(10)
    m2.mete(m3)
    print(m2)
    m2.ordena()
    print(m2)
    