import tkinter as tk
import pygubu
import os
from datetime import datetime
from tkinter import messagebox
from Formula1 import *

class Aplicacion:
    def __init__(self, master,Formula1):
        self.formula1 = Formula1
        #0: Cambia el título a la ventana
        master.title("Campeonato Formula 1")   
        #1: Crea un constructor
        self.builder = builder = pygubu.Builder()
        img_path = os.path.abspath(os.path.dirname(os.getcwd()))
        builder.add_resource_path(img_path)
        #2: Carga un archivo con el diseño de la interfaz
        builder.add_from_file('campeonato.ui')
        #4: Crea el widget usando 'master' como padre
        self.mainwindow = builder.get_object('principal', master)
        builder.connect_callbacks(self)
        #5: Marca un radiobutton por defecto
        self.builder.get_variable("eleccion").set(1)
        # Carga contenido en el control de texto
        self.builder.get_object("salida").insert(tk.END, "Elige una opción para mostrar clasificación")


    def rEleccion(self):
        # Recupera el valor de la variable asociada a los radio button
        valor = self.builder.get_variable("eleccion").get()
        # Borra el contenido del control de texto
        self.builder.get_object("salida").delete(1.0, tk.END)
        # Carga contenido en el control de texto
        if valor == 1:
           self.builder.get_object("salida").insert(tk.END,(formula1.imprime_resultado()))
        if valor == 2:
           self.builder.get_object("salida").insert(tk.END,(formula1.clasificacion_pilotos()))
        if valor == 3:
           self.builder.get_object("salida").insert(tk.END,(formula1.clasificacion_escuderias()))

    def comprobar(self):
        """Comprueba que se ha seleccionado circuito y la fecha es correcta"""
        if self.builder2.get_object("cmbCircuito").get():   
            # El método strptime genera ValueError si la fecha no es correcta
            try:
                # Convierte el texto del control Entry en un objeto datetime
                self.fecha = datetime.datetime.strptime(self.builder2.get_variable("var_fecha").get(), "%d-%m-%Y")  
                # Si todo está correcto muestra el circuito y la fecha
                p = []
                for piloto in self.lista_resultado.get_children():                           
                    p.append(self.lista_resultado.item(piloto)["values"][0])
                    #print(piloto)
                print(p)
                self.formula1.resultado(self.fecha,self.builder2.get_object("cmbCircuito").get(),p)
                messagebox.showinfo("Selección", "Has elegido el circuito " + self.builder2.get_object("cmbCircuito").get() + " y la fecha " + self.fecha.strftime("%d-%m-%Y"))
            except ValueError:
                # Muestra un error
                messagebox.showerror("Fecha incorrecta", "La fecha introducida no es válida")
        else:
            # Muestra un error
            messagebox.showerror("Sin circuito", "No has elegido el circuito")

    def anadir_resultado(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('campeonato.ui')
        self.top = tk.Toplevel(self.mainwindow)
        self.builder2.get_object("resultados",self.top)
        self.builder2.connect_callbacks(self)

        self.lista_resultado = self.builder2.get_object("tvResultados")
        self.lista_resultado.configure(columns=("numero"))
        self.lista_resultado.heading("#0", text="Nombre")
        self.lista_resultado.heading("numero", text="Número")


        self.lista_pilotos = self.builder2.get_object("tvPilotos")
        self.lista_pilotos.configure(columns=("numero"))
        self.lista_pilotos.heading("#0", text="Número")
        self.lista_pilotos.heading("numero", text="Nombre")

        self.lista_circuitos = self.builder2.get_object("cmbCircuito")
        self.builder2.get_object("cmbCircuito").bind("<<ComboboxSelected>>", self.selecciona_circuito)
        
        circuitos = []
        for circuito in self.formula1.resultados:
            circuitos.append(circuito.nombre)
        self.lista_circuitos["values"] = circuitos
        
        for escuderia in self.formula1.escuderias:
            for piloto in escuderia.pilotos: 
                self.lista_pilotos.insert("", tk.END, text=piloto.nombre, values=piloto.numero) 

        self.builder2.get_variable("var_fecha").set(datetime.datetime.today().strftime("%d-%m-%Y"))
        self.fecha = datetime.datetime.today()   

        # Captura el evento de selección del combobox
        # self.lista_circuitos.current(0)
        #circuito_seleccionado = self.lista_circuitos.get()
        #nombre_circuito_selec = circuito_seleccionado.split(" ")[0]
        #self.fecha = datetime.datetime.today()
        #fecha_circuito_selec = self.fecha.strftime("%d-%m-%Y")
        #print(nombre_circuito_selec + " fecha " + fecha_circuito_selec)

    def btnAnadirPiloto(self):
        seleccionado = self.lista_pilotos.focus()
        if seleccionado:
           dato = self.lista_pilotos.item(seleccionado)
           self.lista_resultado.insert("",tk.END,text=dato["text"],values=dato["values"])
           #print("Insertando piloto")
    
    def btnQuitarPiloto(self):
        seleccionado= self.lista_resultado.selection()[0] 
        if seleccionado:
            self.lista_resultado.delete(seleccionado)
  
    def selecciona_circuito(self, event):
        """Captura evento de selección en el combobox de circuitos"""
        self.builder2.get_object("cmbCircuito").get()
        for i in self.lista_resultado.get_children():
            self.lista_resultado.delete(i)
        print("Has elegido: " + self.builder2.get_object("cmbCircuito").get())

        #for piloto in self.lista_resultado.get_children():                           
        #    self.lista_resultado.item(piloto)
        #    print(piloto)

        for circuitos in self.formula1.resultados:
            if circuitos.nombre == self.builder2.get_object("cmbCircuito").get():    
               for piloto in circuitos.resultado:
                   for escuderia in self.formula1.escuderias:
                       for pilotonumero in escuderia.pilotos:
                           if pilotonumero.numero == piloto:
                               self.lista_resultado.insert("",tk.END,text=pilotonumero.nombre,values=piloto)

if __name__ == '__main__':
    ventana = tk.Tk()
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

    formula1 = c
    app = Aplicacion(ventana,formula1)
    ventana.mainloop()        
