import tkinter as tk
import pygubu
import os
from agenda import *


class Aplicacion:
    def __init__(self, master, agenda):
        self.agenda = agenda
        #0: Cambia el título a la ventana
        master.title("Agenda")
        
        #1: Crea un constructor
        self.builder = builder = pygubu.Builder()

        #2: Carga un archivo con el diseño de la interfaz
        builder.add_from_file('agenda.ui')

        #3: Set images path before creating any widget
        img_path = os.path.abspath(os.path.dirname(os.getcwd()))
        builder.add_resource_path(img_path)

        #4: Crea el widget usando 'master' como padre
        self.mainwindow = builder.get_object('principal', master)
        builder.connect_callbacks(self)

        #5: Extrae la lista de contactos para actualizarla 
        #Prepara el control treeview para cargar los datos
        self.lista_contactos = builder.get_object("tvContactos")
        self.lista_contactos.configure(columns=("telefono"))
        self.lista_contactos.heading("#0", text="Nombre")
        self.lista_contactos.heading("telefono", text="Teléfono")

        # Extraer la lista de contactos para mostrarla en el treeview
        for contacto in self.agenda.contactos:
            self.lista_contactos.insert("", tk.END, text=contacto.nombre, values=(contacto.numero))
            
    def frmAlta(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('agenda.ui')
        self.top = tk.Toplevel(self.mainwindow)
        self.builder2.get_object('alta_contacto', self.top)
        self.builder2.connect_callbacks(self)

    def btnBorrar(self):
        seleccionado = self.lista_contactos.focus()
        if seleccionado:
            datos = self.lista_contactos.item(seleccionado)
            self.agenda.borrar(datos["text"], str(datos["values"][0]))
            self.lista_contactos.delete(seleccionado)
    
    def btnBuscar(self):
        txtBusqueda = self.builder.get_object("txtBusqueda")
        if txtBusqueda.get():
            elementos = self.lista_contactos.get_children()
            for e in elementos:
                datos = self.lista_contactos.item(e)
                if txtBusqueda.get() in datos["text"]:
                     self.lista_contactos.selection_set(e)
                     self.lista_contactos.focus(e)
                     break
    
    def btnAnadir(self):
        self.alta(self.builder2.get_object("txtNombre").get(), self.builder2.get_object("txtNumero").get())
        self.top.destroy()

    def btnCancel(self):
        self.top.destroy()

    def alta(self, nombre, numero):
        self.agenda.alta(nombre, numero)
        self.lista_contactos.insert("", tk.END, text=nombre, values=(numero))

if __name__ == '__main__':
    ventana = tk.Tk()
    agenda = Agenda()
    agenda.carga("agenda.txt")
    app = Aplicacion(ventana, agenda)
    ventana.mainloop()
    agenda.guarda("agenda.txt")
