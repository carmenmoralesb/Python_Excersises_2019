import pytest
from Formula1 import *

def test_piloto():
    for escuderia in c.escuderias:
        assert len(escuderia.pilotos) == 2

def test_escuderia():
    assert len(c.escuderias) == 6

def test_circuitos():
    assert len(c.resultados) == 6

def test_puntos():
    for escu in c.escuderias:
        for piloto in escu.pilotos:
            if piloto.nombre == "Valteri Bottas":
               assert piloto.puntos == 28

def test_ganador():
    r = []
    for escu in c.escuderias:
        for piloto in escu.pilotos:
            r.append(piloto)
    r.sort(reverse=True)
    assert r[0].nombre == "Lewis Hamilton"
    assert r[0].numero == 44

def test_ganador_circuito():
    for circu in c.resultados:
        if circu.nombre == "Albert Park":
           ganador = circu.resultado[0]
    assert ganador == 44

def test_clasi_escu():
    assert c.clasificacion_escuderias()

def test_clasi_pil():
    assert c.clasificacion_pilotos()

def test_calendario():
    assert c.calendario()

def test_resul():
    assert type(c.resultado(date(2019,4,14),"Shanghái",[44,77,5,16,10,33,3,27,8,20,4,55]))

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

e1 = Escuderia("Mercedes","Mercedes",p1)
e2 = Escuderia("Ferrari","Ferrari",p2)
e3 = Escuderia("Red Bull","Honda",p3)
e4 = Escuderia("Renault","Renault",p4)
e5 = Escuderia("Haas","Ferrari",p5)
e6 = Escuderia("McLaren","Renault",p6)

r1 = Circuito("Albert Park", "Australia", date(2019,3,17))
r2 = Circuito("Baréin", "Baréin", date(2019,3,31),[])
r3 = Circuito("Shanghái", "China", date(2019,4,14),[])
r4 = Circuito("Baku", "Azerbaiyán", date(2019,4,28),[])
r5 = Circuito("Barcelona", "España", date(2019,5,12),[])
r6 = Circuito("Mónaco", "Mónaco", date(2019,5,26),[])
           
lista_escuderias = [ e1, e2, e3, e4, e5, e6]
lista_resultados = [ r1, r2, r3, r4, r5, r6]       
    
c = Campeonato("2019", lista_escuderias, lista_resultados)

c.resultado(date(2019,3,17), "Albert Park",[44,77,5,16,10,33,3,27,8,20,4,55])
c.resultado(date(2019,3,31), "Baréin", [77,44,5,16,10,33,3,27,8,20,4,55])

