class Vivienda:
    def __init__(self,piso,letra,propietario,coeficiente,voto):
        self.piso = piso
        self.letra = letra
        self.propietario = propietario
        self.coeficiente = coeficiente
        self.voto = voto

    def __str__(self):
        return str(self.piso) + " " + self.letra + " " + self.propietario + " Ha votado al presupuesto: " + str(self.voto)

class Presupuesto:
    def __init__(self,descripcion,importe):
        self.descripcion = descripcion
        self.importe = importe
        self.votos = 0.0
    
    def __str__(self):
        return self.descripcion + " " + str(self.importe) + " con: " + str(self.votos) + " votos"
    
    def __lt__(self,otro):
        return self.votos < otro.votos
    

class Bloque:
    def __init__(self,numero, viviendas = []):
        self.numero = numero
        self.viviendas = []
    
    def __str__(self):
        return str(self.numero)
    
    def devuelve_viviendas(self):
        for vivienda in self.viviendas:
            return vivienda

    def añadir_vivienda(self,piso,letra,propietario,coeficiente,voto):
        self.viviendas.append(Vivienda(piso,letra,propietario,coeficiente,voto))
    
    
class Comunidad:
    def __init__(self,nombre,bloques = [],presupuestos= []):
        self.nombre =  nombre
        self.bloques = bloques
        self.presupuestos = presupuestos
    

    def __str__(self):
        r = "Nombre " + self.nombre + '\n' 
        for bloque in bloques:
            r += "Bloque " + str(bloque) + '\n'
            for vivienda in viviendas:
                r += "Vivienda " + str(vivienda) + '\n'
        return r

    def devuelve_bloques(self):
        for bloque in self.bloques:
            return bloque
            
    def añadir_presupuesto(self,numpresu,descripcion,importe):
        self.presupuestos.append(Presupuesto(descripcion,importe))

    def devuelve_presupuestos(self):
        for presupuesto in self.presupuestos:
            return presupuesto

    def sumar_votos(self):
        total_votos = 0.0
        for b in self.bloques:
            for v in b.viviendas:
                self.presupuestos[v.voto-1].votos += v.coeficiente
                total_votos += v.coeficiente
        presupuesto_final = max(self.presupuestos)
        print(presupuesto_final)
        
        for b in self.bloques:
            print("Bloque " + str(b.numero) + '\n')
            for v in b.viviendas:
                print(str(v) + " Derrama" + str((v.coeficiente*presupuesto_final)/total_votos + ""))

if __name__ == "__main__":
    viviendas = [Vivienda(1, "A", "Juan Pérez", 2.2, 1),
          Vivienda(1, "B", "José López", 1.8, 3),
          Vivienda(2, "A", "María Rodríguez", 2, 2),
          Vivienda(2, "B", "Manuel Martínez", 2, 1),
          Vivienda(3, "A", "Luís González", 2, 3),
          Vivienda(3, "B", "Ana Ramírez", 2, 2),
          Vivienda(4, "A", "Carmen Gutiérrez", 1.8, 1),
          Vivienda(4, "B", "Josefa Sánchez", 2.2, 2)]

    viviendas2 = [Vivienda(1, "A", "Juana Pérez", 2, 2),
          Vivienda(1, "B", "Josefa López", 2, 1),
          Vivienda(2, "A", "Mario Rodríguez", 1.5, 3),
          Vivienda(2, "B", "Manuela Martínez", 2.5, 3),
          Vivienda(3, "A", "Luisa González", 2.5, 1),
          Vivienda(3, "B", "Enrique Ramírez", 1.5, 2),
          Vivienda(4, "A", "Carmelo Gutiérrez", 2, 1),
          Vivienda(4, "B", "José Sánchez", 2, 3)]

    bloques = [Bloque(1, viviendas),
         Bloque(2, viviendas2)]

    presupuestos = [Presupuesto("Pinturas Roja y Gualda", 300),
         Presupuesto("Toro Fachadas", 275),
         Presupuesto("Española de Pinturas", 400)]

    c = Comunidad("La española", bloques, presupuestos)

    print(c)
    print('\n')

    for presupuesto in presupuestos:
        print(presupuesto)

    print('\n')
    print("El ganador es " + str(max(presupuestos)))
    # c.sacar_ganador()
    c.sumar_votos()