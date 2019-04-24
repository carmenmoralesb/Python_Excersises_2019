#!/usr/local/bin/python3

class Equipo:
    """Clase equipo con unas siglas,nombre y varias puntuaciones PJ partidos jugados PG partidos ganados..."""
    def __init__(self,iden,nombre,PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0):
        self.iden = iden
        self.nombre = nombre
        self.PJ = PJ
        self.PG = PG
        self.PP = PP
        self.PAF = PAF
        self.PEC = PEC
        self.MAR = MAR

    def __str__(self): # Devuelve los puntos del equipo
        self.equipo = self.iden + " " + self.nombre + " PJ: " + str(self.PJ) + " PG: " + str(self.PG) + " PP: " + str(self.PP) + " PAF: " + str(self.PAF) + " PEC: " + str(self.PEC) + " MAR: " + str(self.MAR)
        return self.equipo

    def __cmp__(self, otro):
        if self.PG > otro.PG: return 1
        if self.PG < otro.PG: return -1
        return 0
    
    def __lt__(self, otro):
        if self.PG < otro.PG:
           return True
        elif self.PG > otro.PG:
           return False    

        elif self.PP > otro.PP:
             return True
        elif self.PP < otro.PP:
            return False

        elif self.MAR < otro.MAR:
            return False
        elif self.MAR > otro.MAR:
            return True
            
    
    def __eq__(self, otro):
        if self.PG == otro.PG:return True
        return False

    def actualiza_resultado(self, pf, pc):
        pass

if __name__ == "__main__":
    #  CREANDO LOS EQUIPOS
    CadizWheels = Equipo('CAW','Cadiz Wheels',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0)
    ChiclanaSurf = Equipo('CHB','Chiclana Blues',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0)
    CaletaSurf = Equipo('CSUN','Conil Suns',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0)
    VictoraBedouins = Equipo('VIB','Victoria Bedouins',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0)
    CortaduraHearts = Equipo('CHE','Cortadura Hearts',PJ=0,PG=0,PP=0,PAF=0,PEC=0,MAR=0)