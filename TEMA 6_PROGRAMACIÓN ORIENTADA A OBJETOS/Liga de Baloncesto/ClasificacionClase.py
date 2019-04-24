#!/usr/local/bin/python3

from Equipoclase import Equipo
from Partidoclase import Partido
from datetime import date

class Liga:
    """Clase que inicializa con una lista de equipos y una lista de partidos"""
    def __init__(self,equipos=[Equipo('CAW','Cadiz Wheels',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0),
                               Equipo('CHB','Chiclana Blues',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0),
                               Equipo('CSUN','Conil Suns',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0),
                               Equipo('VIB','Victoria Bedouins',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0),
                               Equipo('CHE','Cortadura Hearts',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0)],
                listapartidos=None):

        self.equipos = equipos
        if listapartidos is None:
            self.listapartidos = []
        
    def añadir_partido(self,equipolocal,puntoslocal,equipovisitante,puntosvisitante):
        """Método para añadir partidos"""
        self.listapartidos.append(Partido(equipolocal,puntoslocal,equipovisitante,puntosvisitante))
        self.suma_puntos()

    def suma_puntos(self):
        """Método que suma los puntos a la clasificación de cada equipo participante en los partidos"""
        i=len(self.listapartidos)-1
        for j in range(0,len(self.equipos)):
            if self.listapartidos[i].equipolocal == self.equipos[j].nombre or self.listapartidos[i].equipolocal == self.equipos[j].iden:
                self.equipos[j].PJ += 1
                self.equipos[j].PAF += self.listapartidos[i].puntoslocal
                self.equipos[j].PEC += self.listapartidos[i].puntosvisitante
                    
                if self.listapartidos[i].puntoslocal > self.listapartidos[i].puntosvisitante:
                    self.equipos[j].PG += 1
                else:
                    self.equipos[j].PP += 1 
            
            elif self.listapartidos[i].equipovisitante == self.equipos[j].nombre or self.listapartidos[i].equipovisitante == self.equipos[j].iden:    
                self.equipos[j].PJ += 1   
                self.equipos[j].PAF += self.listapartidos[i].puntosvisitante
                self.equipos[j].PEC += self.listapartidos[i].puntoslocal 
                self.equipos[j].MAR += (self.equipos[j].PAF - self.equipos[j].PEC) // (self.equipos[j].PJ)
            
                if self.listapartidos[i].puntoslocal > self.listapartidos[i].puntosvisitante:
                    self.equipos[j].PP += 1
                else:
                    self.equipos[j].PG += 1

    def calendario(self):
        """Muestra las fechas y partidos realizados en una temporada"""
        for partido in self.listapartidos:
            print(str(partido.fecha) + " " + partido.equipolocal + " " + str(partido.puntoslocal)  + " " + partido.equipovisitante + " " + str(partido.puntosvisitante))
    
    def clasificacion(self):
        """Muestra de forma ordenada la clasificación de equipos según partidos ganados"""
        contador = 0
        self.equipos.sort(reverse=True)
        for equipo in self.equipos:
            contador += 1
            print(str(contador) + " " + str(equipo))

if __name__ == "__main__":
    c1 = Liga()

    # Esto funciona
    c1.añadir_partido('Cortadura Hearts',20,'Victoria Bedouins',50)
    c1.añadir_partido('Cadiz Wheels',40,'Conil Suns',60)
    c1.añadir_partido('VIB',20,'CHE',50)
    c1.añadir_partido('CHB',40,'CSUN',20)

    c1.calendario()
    c1.clasificacion()