import tkinter as tk
import pygubu
import os
import pymysql

# MI SERVIDOR TIENE CONTRASEÑA root
con = pymysql.connect("localhost", "root", "root", "agenda")
# creo el cursor
cursor = con.cursor()

class Aplicacion:
    def __init__(self, master):

        #0: Cambia el título a la ventana
        master.title("Agenda")
        
        #1: Crea un constructor
        self.builder = builder = pygubu.Builder()

        #2: Carga un archivo con el diseño de la interfaz
        builder.add_from_file('agenda.ui')

        #3: Establece el directorio de imágenes antes de crear componentes
        img_path = os.path.abspath(os.path.dirname(os.getcwd()))
        builder.add_resource_path(img_path)

        #4: Crea el widget usando 'master' como padre
        self.mainwindow = builder.get_object('principal', master)
        builder.connect_callbacks(self)

        #5: Prepara el control treeview para cargar los contactos
        self.lista_contactos = builder.get_object("tvContactos")
        self.lista_contactos.configure(columns=("telefono"))
        self.lista_contactos.heading("#0", text="Nombre")
        self.lista_contactos.heading("telefono", text="Teléfono")
        #5.1: Prepara el control treeview para cargar las familias
        self.lista_familia = builder.get_object("tvFamilia")
        self.lista_familia.configure(columns=("telefono"))
        self.lista_familia.heading("#0", text="Nombre")
        self.lista_familia.heading("telefono", text="Teléfono")
        
        #6: Asocia un método al evento de click sobre el treeview para actualizar el listado de la familia
        self.lista_contactos.bind("<ButtonRelease-1>", self.actualiza_familia )

        #7: Extrae la lista de contactos para mostrarla en el treeview 
        cursor.execute("select * from contactos")
        print("Contactos encontrados: {0}".format(cursor.rowcount))
        for (nombre, telefono) in cursor:
            self.lista_contactos.insert("", tk.END, text=nombre, values=(telefono))
            
    def frmAlta(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('agenda.ui')
        self.top = tk.Toplevel(self.mainwindow)
        self.builder2.get_object('alta_contacto', self.top)
        self.builder2.connect_callbacks(self)

    def frmEdit(self):
        # Obtiene el id  del item seleccionado
        self.seleccionado = self.lista_contactos.focus()
        if self.seleccionado:
            # Recupera los datos del item seleccionado. Los recupera como un diccionario.
            datos = self.lista_contactos.item(self.seleccionado)
            # Crea un nuevo builder para la ventana
            self.builder2 = pygubu.Builder()
            # carga el diseño
            self.builder2.add_from_file('agenda.ui')
            # Crea la nueva ventana
            self.top = tk.Toplevel(self.mainwindow)
            # Le asocia el frame correspondiente a la nueva ventana
            self.builder2.get_object('edita_contacto', self.top)
            # Crea variables para cargar el texto en los controles Entry del formulario
            self.nombre_edit = tk.StringVar()
            self.numero_edit = tk.StringVar()
            # Del treeview se cargan los datos del nombre...
            self.nombre_edit.set(datos["text"])
            # ... y del número
            self.numero_edit.set(str(datos["values"][0]))
            # Se asignan los valores a los controles del formulario
            self.builder2.get_object("txtNombre_edit").configure(textvariable=self.nombre_edit)
            self.builder2.get_object("txtNumero_edit").configure(textvariable=self.numero_edit)
            self.builder2.connect_callbacks(self)

    def btnGuardar(self):
         datos = self.lista_contactos.item(self.seleccionado)
         nombre = str(datos["text"])
         # numero = str(datos["values"][0])

         self.lista_contactos.item(self.seleccionado, text=self.nombre_edit.get(), values=(self.numero_edit.get()))
         #cursor = con.cursor()

         nuevonombre=str(self.nombre_edit.get())
         nuevonumero = str(self.numero_edit.get())
         cursor.execute("UPDATE contactos SET nombre = '{0}',numero = '{1}' WHERE nombre = '{2}'".format(nuevonombre,nuevonumero,nombre))
         con.commit()
         self.top.destroy()

    def btnBorrar(self):
        #cursor = con.cursor()
        seleccionado = self.lista_contactos.focus()
        
        if seleccionado:
            datos = self.lista_contactos.item(seleccionado)
            self.lista_contactos.delete(seleccionado)
            
            busqueda = str(datos["text"])      
            cursor.execute("DELETE FROM contactos WHERE nombre = '{0}'".format(busqueda))
            print("Contactos eliminados: {0}".format(cursor.rowcount))
            con.commit()

    def btnBuscar(self):
        txtBusqueda = self.builder.get_object("txtBusqueda")
        
        if txtBusqueda.get():
            for c in self.lista_contactos.get_children():
                self.lista_contactos.delete(c)
            
            #cursor = con.cursor()
            cursor.execute("SELECT nombre,numero FROM contactos WHERE nombre = '{0}'".format(txtBusqueda.get()))

            for fila in cursor:
                print(str(fila[0]), str(fila[1]))
                self.lista_contactos.insert("", tk.END, text=fila[0],values=fila[1])
                self.builder.connect_callbacks(self) 

    def btnAnadir(self):
         self.alta(self.builder2.get_object("txtNombre").get(), self.builder2.get_object("txtNumero").get())
         self.top.destroy()

    def btnCancel(self):
        self.top.destroy()

    def alta(self, nombre, numero):
        #cursor = con.cursor()
        cursor.execute("INSERT INTO contactos VALUES ('{0}', '{1}')".format(nombre, numero))
        con.commit()

        for c in self.lista_contactos.get_children():
           self.lista_contactos.delete(c)
        
        cursor.execute("SELECT * FROM contactos")
        for (nombre, telefono) in cursor:
            self.lista_contactos.insert("", tk.END, text=nombre, values=(telefono))

    def actualiza_familia(self,event = None):
        self.seleccionado = self.lista_contactos.focus()
        
        if self.seleccionado:
            for f in self.lista_familia.get_children():
                self.lista_familia.delete(f)
            
            datos = self.lista_contactos.item(self.seleccionado)
            print(datos)
            nombre = str(datos["text"])
            
            #cursor = con.cursor()
            cursor.execute("SELECT DISTINCT contactofamiliar.nombrefamiliar,contactos.numero FROM contactos,contactofamiliar WHERE contactos.nombre = contactofamiliar.nombrefamiliar AND contactofamiliar.nombre = '{0}'".format(nombre))
            
            for fila in cursor:
                print(str(fila[0]), str(fila[1]))
                self.lista_familia.insert("", tk.END, text=fila[0],values=fila[1])
            self.builder.connect_callbacks(self) 

    def btnNueva_Familia(self):
        self.seleccionado = self.lista_contactos.focus()
        if self.seleccionado:
            datos = self.lista_contactos.item(self.seleccionado)
            nombre = str(datos["text"])
            
            self.builder2 = pygubu.Builder()
            self.builder2.add_from_file('agenda.ui')
            self.top = tk.Toplevel(self.mainwindow)
            self.builder2.get_object('edit_familia', self.top)
            self.lista_familiares = self.builder2.get_object("tvFamiliares")
            self.lista_familiares.configure(columns=("telefono"))
            self.lista_familiares.heading("#0", text="Nombre")
            self.lista_familiares.heading("telefono", text="Teléfono")
            
            #cursor = con.cursor()
            cursor.execute("SELECT nombre,numero FROM contactos WHERE nombre != '{0}' AND nombre NOT IN (SELECT nombrefamiliar FROM contactofamiliar WHERE nombre = '{0}' or nombrefamiliar = '{0}') AND nombre NOT IN (SELECT nombre FROM contactofamiliar WHERE nombre = '{0}' OR nombrefamiliar = '{0}')".format(nombre))
            # muestra los nombres y numeros de telefono de los contactos que aun no son familia
            
            for fila in cursor:
                #print(str(fila[0]), str(fila[1]))
                self.lista_familiares.insert("", tk.END, text=fila[0],values=fila[1])
                self.builder2.connect_callbacks(self)

    def btnAnadir_familiar(self):
        self.seleccionado1 = self.lista_familiares.focus()
        self.seleccionado2= self.lista_contactos.focus()

        if self.seleccionado2:
            datos = self.lista_familiares.item(self.seleccionado1)
            datos2= self.lista_contactos.item(self.seleccionado2)
            
            #cursor = con.cursor()
            contactofamiliarnombre = str(datos["text"])
            contactonombre = str(datos2["text"])
            cursor.execute("INSERT INTO contactofamiliar VALUES ('{0}','{1}')".format(contactonombre,contactofamiliarnombre))
            con.commit()
            
        self.top.destroy()
        self.actualiza_familia()


    def btnBorrar_Familiar(self):
        self.seleccionado1 = self.lista_familia.focus()
        self.seleccionado2= self.lista_contactos.focus()

        if self.seleccionado2:
            datos1 = self.lista_familia.item(self.seleccionado1)
            datos2= self.lista_contactos.item(self.seleccionado2)
            
            contactofamiliarnombre = str(datos1["text"])
            contactonombre = str(datos2["text"])

            #cursor = con.cursor()
            cursor.execute("DELETE FROM contactofamiliar WHERE nombrefamiliar = '{0}' AND nombre = '{1}'".format(contactofamiliarnombre,contactonombre))
            con.commit()
            
            self.actualiza_familia()
            

if __name__ == '__main__':
    ventana = tk.Tk() # Crea la ventana gráfica del programa
    app = Aplicacion(ventana)
    ventana.mainloop()