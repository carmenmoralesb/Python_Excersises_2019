#!/usr/local/bin/python3
import random

class Carta:
    # Codificamos las propiedades de las cartas
    palos = ["Bastos", "Copas", "Oros", "Espadas"]
    valores = [None, "As", "Dos", "Tres", "Cuatro", "Cinco",
             "Seis", "Siete", "Ocho", "Nueve", "Sota", "Caballo", "Rey"]
    
    def __init__(self, valor=None, palo=None):
        # Si no recibo palo o valor se asignan aleatoriamente
        while valor==None:
            valor = random.choice(self.valores)
        if palo==None:
            palo = random.choice(self.palos)
        # Discrimina si el valor esta expresado en números o texto
        if type(valor) == type(5):
            if valor<1 or valor>len(self.valores)-1:
                raise ValueError(str(valor) + " no es correcto.")
            self.valor = valor
        else:
            # Compruebo corrección de los valores
            if not valor in self.valores:
                raise ValueError(valor + " no es correcto.")
            self.valor = self.valores.index(valor)
        # Discrimina si el palo esta expresado en números o texto
        if type(palo) == type(5):
            if palo<0 or palo>len(self.palos):
                raise ValueError(str(palo) + " no es correcto.")
            self.palo = palo
        else:
            if not palo in self.palos:
                raise ValueError(palo + " no es correcto.")
            # Almaceno propiedades
            self.palo = self.palos.index(palo)
    
    def __cmp__(self, otra):
        if self.palo > otra.palo: return 1
        if self.palo < otra.palo: return -1
        if self.valor > otra.valor: return 1
        if self.valor < otra.valor: return -1
        return 0
    
    def __lt__(self, otra):
        if self.palo < otra.palo: return True
        if self.palo > otra.palo: return False
        if self.valor < otra.valor: return True
        return False        
    
    def __eq__(self, otra):
        if self.palo == otra.palo and self.valor == otra.valor: return True
        return False
    
    def __str__(self):
        return self.valores[self.valor] + " de " + self.palos[self.palo]
    
if __name__ == "__main__":
    c1 = Carta()
    print(c1)
    c2 = Carta("Rey", "Copas")
    print(c2)
    c3 = Carta(1, 3)
    print(c3)
    c4 = Carta(1, 3)
    print(c4)