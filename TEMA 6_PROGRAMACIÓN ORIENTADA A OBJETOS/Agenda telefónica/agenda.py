class Agenda:
    def __init__(self, contactos=[]):
        self.contactos = contactos

    def __str__(self):
        resultado = ""
        for contacto in self.contactos:
            resultado += str(contacto) + "\n"
        return resultado

    def familia_de(self, nombre, numero):
        compara = Contacto(nombre, numero)
        for i in range(len(self.contactos)):
            if self.contactos[i] == compara:
                return self.contactos[i].familia

    def alta(self, nombre, numero):
        self.contactos.append(Contacto(nombre, numero))

    def borrar(self, nombre, numero):
        compara = Contacto(nombre, numero)
        for i in range(len(self.contactos)):
            if self.contactos[i] == compara:
                del self.contactos[i]
                #print(i)
                break

    def modificar(self, nombre, numero, nombre_edit, numero_edit):
        compara = Contacto(nombre, numero)
        for i in range(len(self.contactos)):
            if self.contactos[i] == compara:
                self.contactos[i].nombre = nombre_edit
                self.contactos[i].numero = numero_edit
                break

    def carga(self, archivo_contactos, archivo_familias):
        manf = open(archivo_contactos)
        for linea in manf:
            ld = linea.rstrip().split(";")
            self.contactos.append(Contacto(ld[0], ld[1]))
        manf.close()
        manf = open(archivo_familias)
        for linea in manf:
            ld = linea.rstrip().split(";")
            buscar = Contacto(ld[0], ld[1])
            for contacto in self.contactos:
                if contacto == buscar:
                    destino = contacto
                    break
            buscar = Contacto(ld[2], ld[3])
            for contacto in self.contactos:
                if contacto == buscar:
                    familiar = contacto
                    break
            destino.familia.append(familiar)
      
    def guarda(self, archivo_contactos, archivo_familias):
        with open(archivo_contactos, "w") as manf:
            for contacto in self.contactos:
                manf.write(contacto.nombre + ";" + contacto.numero + "\n")
        with open(archivo_familias, "w") as manf:
            for contacto in self.contactos:
                for familiar in contacto.familia:
                    manf.write(contacto.nombre + ";" + contacto.numero + ";" + familiar.nombre + ";" + familiar.numero + "\n")

    
class Contacto:
    def __init__(self, nombre, numero, familia=[]):
        self.nombre = nombre
        self.numero = numero
        self.familia = familia[:]

    def __str__(self):
        return self.nombre + " -> " + self.numero
    
    def __lt__(self, otro):
        return self.nombre < otro.nombre
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.numero == otro.numero