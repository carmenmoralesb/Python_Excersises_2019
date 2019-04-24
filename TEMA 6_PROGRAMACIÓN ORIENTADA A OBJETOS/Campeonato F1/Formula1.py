import datetime
from datetime import date
import random

class Piloto:
    def __init__(self,nombre,nacionalidad,numero):
        self.nombre = nombre
        self.numero = numero
        self.nacionalidad = nacionalidad
        self.puntos = 0

    def __str__(self):
        return self.nombre + " " + str(self.puntos) + " puntos"
    
    def __lt__(self, otro):
        return self.puntos < otro.puntos

class Escuderia:
    def __init__(self,nombre,motor,pilotos = []):
        self.nombre = nombre
        self.motor = motor
        self.pilotos = pilotos
    
    def __str__(self):
        return " Escuderia " + self.nombre
    
    def __lt__(self, otro):
        total1 = 0
        total2 = 0

        for piloto in self.pilotos:
            total1 += piloto.puntos
        for piloto in otro.pilotos:
            total2 += piloto.puntos
        
        return total1 < total2

class Circuito:
    def __init__(self,nombre,pais,fecha,resultado = []):
        self.nombre = nombre
        self.pais = pais
        self.fecha = fecha
        self.resultado = resultado

    def __str__(self):
        r = self.nombre + " " + self.pais + " en " + str(self.fecha)
        return r

class Campeonato:
    def __init__(self,temporada,escuderias=[],resultado=[]):
        self.temporada = temporada
        self.escuderias = escuderias
        self.resultados = resultado

    def __str__(self):
        r = "CAMPEONATO " + str(self.temporada)  + '\n'*2
        for circuito in self.resultados:
            r += "Circuitos " + str(circuito) + '\n'

        for escuderia in self.escuderias:
            r += "[x]" + str(escuderia) + '\n'
            for piloto in escuderia.pilotos:
                r += str(piloto) + '\n'
        return r

    def clasificacion_pilotos(self):
        """Crea una clasificación de pilotos sumando sus puntos en un campeonato y devuelve el ganador y los demás ordenados
        segun puntuacion"""

        rlista = []
        r = ''
        #r = "CLASIFICACIÓN DE PILOTOS" + " " + str(self.temporada) + '\n'*2
    
        for escuderia in self.escuderias:
            for piloto in escuderia.pilotos:
                rlista.append(piloto)

        rlista = sorted(rlista,reverse=True)
        ganador = str(rlista[0])

        r += "Ganador: " + str(ganador) + '\n'*2

        for piloto in range(1,len(rlista)):
            r += str(piloto + 1 ) + " " + str(rlista[piloto]) + '\n'
        return r

    def clasificacion_escuderias(self):
        """crea una clasificación por escudería sumando los puntos totales de sus pilotos"""
        rlista = []
        r = ''
        #r = "CLASIFICACIÓN DE ESCUDERÍAS" + " " + str(self.temporada) +  '\n'*2
        for escuderia in self.escuderias:
            rlista.append(escuderia)
        
        for escu in range(len(sorted(rlista,reverse=True))):
            r += str(escu + 1) + " " + str(self.escuderias[escu]) + '\n'
        return r
    
    def resultado(self,fecha,nomcircuito,pilotos=[]):
        for circuito in self.resultados:
            if nomcircuito == circuito.nombre:
               circuito.resultado = pilotos
               circuito.fecha = fecha
            elif not fecha:
               circuito.fecha = circuito.fecha
            

            if fecha == circuito.fecha:
               for pil in range(len(circuito.resultado)):
                   for escuderia in self.escuderias:
                       for piloto in escuderia.pilotos:
                           if pilotos[pil] == piloto.numero:
                               if pil == 0:
                                   piloto.puntos += 25
                               elif pil == 1:
                                   piloto.puntos += 18
                               elif pil == 2:
                                   piloto.puntos += 15   
                               elif pil == 3:
                                   piloto.puntos += 10
                               elif pil == 4:
                                   piloto.puntos += 8
                               elif pil == 5:
                                   piloto.puntos += 6
                               elif pil == 6:
                                   piloto.puntos += 5
                               elif pil == 7:
                                   piloto.puntos += 3
                               elif pil == 8:
                                   piloto.puntos += 2
                               elif pil == 9:
                                   piloto.puntos += 1
                               else:
                                   piloto.puntos += 0
    
    def calendario(self):
        r = ''
        for circuito in self.resultados:
            for i in range(len(circuito.resultado)):
                if i==0:
                    ganador = circuito.resultado[i]

            for escuderia in self.escuderias:
                for piloto in escuderia.pilotos:
                    if piloto.numero == ganador:
                        ganador = str(piloto.nombre) 
                        r += str(circuito) +  " ganador: " + str(ganador) + '\n'
        return r

if __name__ == "__main__":
    p1 = [ Piloto("Lewis Hamilton", "UK", 44),
           Piloto("Valtteri Bottas", "Finlandia", 77) ]
    p2 = [ Piloto("Sebastian Vettel", "Alemania", 5),
           Piloto("Charles Leclerc", "Mónaco", 16) ]
    p3 = [ Piloto("Pierre Gasly", "Francia", 10),
           Piloto("Max Verstappen", "Holanda", 33) ]
    p4 = [ Piloto("Daniel Ricciardo", "Australia", 3),
           Piloto("Nico Hulkenberg", "Alemania", 27) ]
    p5 = [ Piloto("Romain Grosjean", "Francia", 8),
           Piloto("Kevin Magnussen", "Dinamarca", 20) ]
    p6 = [ Piloto("Lando Norris", "UK", 4),
           Piloto("Carlos Sainz", "España", 55) ]
    p7 = [ Piloto("Sergio Pérez", "México", 11),
           Piloto("Lance Stroll", "Canadá", 18) ]
    p8 = [ Piloto("Kimi Raikkonen", "Finlandia", 7),
           Piloto("Antonio Giovinazzi", "Italia", 99) ]
    p9 = [ Piloto("Alexander Albon", "Tailandia", 23),
           Piloto("Daniil Kviat", "Rusia", 26) ]
    p10= [ Piloto("George Russel", "UK", 63),
           Piloto("Robert Kubica", "Polonia", 88) ]

    e1 = Escuderia("Mercedes","Mercedes",p1)
    e2 = Escuderia("Ferrari","Ferrari",p2)
    e3 = Escuderia("Red Bull","Honda",p3)
    e4 = Escuderia("Renault","Renault",p4)
    e5 = Escuderia("Haas","Ferrari",p5)
    e6 = Escuderia("McLaren","Renault",p6)
    e7 = Escuderia("Racing Point","Mercedes",p7)
    e8 = Escuderia("Alfa Romeo","Ferrari",p8)
    e9 = Escuderia("Red Bull","Honda",p9)
    e10= Escuderia("Williams","Mercedes",p10)

    r1 = Circuito("Albert Park", "Australia", date(2019,3,17))
    r2 = Circuito("Baréin", "Baréin", date(2019,3,31),[])
    r3 = Circuito("Shanghái", "China", date(2019,4,14),[])
    r4 = Circuito("Baku", "Azerbaiyán", date(2019,4,28),[])
    r5 = Circuito("Barcelona", "España", date(2019,5,12),[])
    r6 = Circuito("Mónaco", "Mónaco", date(2019,5,26),[])
    r7 = Circuito("Gilles Villeneuve", "Canadá", date(2019,6,9),[])
    r8 = Circuito("Paul Ricard", "Francia", date(2019,6,23),[])
    r9 = Circuito("Red Bull Ring", "Austria", date(2019,6,30),[])
    r10 = Circuito("Silverstone", "UK", date(2019,7,14),[])
    r11 = Circuito("Hockenheimring", "Alemania", date(2019,7,28),[])
    r12 = Circuito("Hungaroring", "Hungría", date(2019,8,4),[])
    r13 = Circuito("Spa-Francorchamps", "Bélgica", date(2019,9,1),[])
    r14 = Circuito("Monza", "Italia", date(2019,9,8),[])
    r15 = Circuito("Marina Bay", "Singapur", date(2019,9,22),[])
    r16 = Circuito("Sochi", "Rusia", date(2019,9,29),[])
    r17 = Circuito("Suzuka", "Japón", date(2019,10,13),[])
    r18 = Circuito("Hermanos Rodríguez", "México", date(2019,10,27),[])
    r19 = Circuito("Américas", "USA", date(2019,11,3),[])
    r20 = Circuito("José Carlos Pace", "Brasil", date(2019,11,17),[])
    r21 = Circuito("Yas Marina", "Abu Dabi", date(2019,12,1),[])
           
    lista_escuderias = [ e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
    lista_resultados = [ r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21]       
    
    c = Campeonato("2019", lista_escuderias, lista_resultados)

    c.resultado(date(2019,3,17), "Albert Park",[77,44,33,5,16,20,27,7,18,26,10,4,11,23,99,63,88,8,3,55])
    c.resultado(date(2019,3,31), "Baréin", [16, 33, 26, 4, 55, 8, 77, 20, 5, 11, 88, 44, 18, 7, 10, 99, 3, 23, 63, 27])
    c.resultado(date(2019,4,14), "Shanghái",[3, 33, 4, 63, 99, 8, 44, 10, 55, 27, 7, 88, 18, 26, 77, 5, 23, 20, 11, 16])
    c.resultado(date(2019,4,28), "Baku", [18, 7, 8, 26, 4, 27, 11, 55, 5, 33, 77, 3, 23, 88, 63, 16, 20, 99, 10, 44])
    c.resultado(date(2019,5,12), "Barcelona",[99, 3, 5, 77, 44, 63, 88, 11, 55, 26, 33, 23, 16, 18, 8, 27, 4, 10, 7, 20])
    c.resultado(date(2019,5,26), "Mónaco",[44, 55, 20, 10, 5, 99, 3, 27, 8, 33, 63, 23, 16, 11, 88, 4, 77, 26, 18, 7])

    print(c)
    print(c.clasificacion_pilotos())
    print(c.clasificacion_escuderias())
    print(c.calendario())