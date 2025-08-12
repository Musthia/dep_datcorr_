import tkinter as tk
import webbrowser
from datetime import datetime
from tkinter import ttk, messagebox
from tkinter import filedialog
from modeld.perfiles_dao import crear_tabla_usuarios 
from tkinter import PhotoImage
import sqlite3
from PIL import Image, ImageTk
from time import strftime
import os
import openpyxl
import pandas as pd

def abrir_whatsapp():
    numero = "543794996116"  # Reemplaza con el número correcto
    url = f"https://wa.me/{numero}"
    webbrowser.open(url)  # Abre WhatsApp Web o la app si está instalada

def barra_menu(root,  nivel_seguridad):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=100, height=100)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    menu_inicio.config(bg="#adacab")
    barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)
    menu_inicio.add_command(label="Salir", command = root.destroy)

    menu_usuario = tk.Menu(barra_menu, tearoff = 0)
    menu_usuario.config(bg="#adacab")
    barra_menu.add_cascade(label = "Usuarios", menu = menu_usuario)
    
    # Habilitar o deshabilitar opciones de acuerdo al nivel de seguridad
    if nivel_seguridad == 'Admin':  # Ajusta el nivel de seguridad según tus necesidades
        menu_usuario.add_command(label="Manejo de Usuarios", command=crear_usuario)
        menu_usuario.add_command(label="Crear", command=crear_tabla_usuarios)

    else:
        menu_usuario.add_command(label="Manejo de Usuarios", command=lambda: messagebox.showwarning("Acceso Denegado", "No tienes permiso para acceder a esta sección."))
        menu_usuario.add_command(label="Crear", command=lambda: messagebox.showwarning("Acceso Denegado", "No tienes permiso para acceder a esta sección."))

    # Cargar icono personalizado (asegurar que existe y es PNG)
    root.icono_wp = PhotoImage(file="img/whastapp.png")  # Se guarda en la instancia

    menu_ayuda = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Ayuda", menu = menu_ayuda)
    menu_ayuda.add_command(
            label="Fabio",    command=abrir_whatsapp, 
            image=root.icono_wp,  # Asigna el icono
            compound="left"  # Ubica el icono a la izquierda del texto
        )
    menu_ayuda.config(bg= "#45d000")
    menu_ayuda.config(font=("Linkin Park ExtraBold", 20))

def crear_usuario():
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("Inicio de Sesión")
    ventana_crear_usuario.geometry("400x400")
    ventana_crear_usuario.config(bg="#676767")
    ventana_crear_usuario.iconbitmap("img/Datcorr.ico")
    ventana_crear_usuario.resizable(0,0)

    label_usuario = tk.Label(ventana_crear_usuario,text="Usuario:")
    label_usuario.config(font=("Linkin Park ExtraBold", 15), bg= "#676767") 
    label_usuario.grid(row=0, column=1, padx=5, pady=5)

    entry_usuario = tk.Entry(ventana_crear_usuario)
    entry_usuario.grid(row=0, column=2, padx=5, pady=5)
    entry_usuario.bind("<Return>", lambda event: entry_contrasena.focus_set())
    
    label_contrasena = tk.Label(ventana_crear_usuario, text="Contraseña:")
    label_contrasena.config(font=("Linkin Park ExtraBold", 15), bg= "#676767") 
    label_contrasena.grid(row=1, column=1, padx=5, pady=5)
    
    entry_contrasena = tk.Entry(ventana_crear_usuario, show="*")
    entry_contrasena.grid(row=1, column=2, padx=5, pady=5)
    entry_contrasena.bind("<Return>", lambda event: entry_nombre.focus_set())
    
    label_nombre = tk.Label(ventana_crear_usuario, text="Nombre:")
    label_nombre.config(font=("Linkin Park ExtraBold", 15), bg= "#676767") 
    label_nombre.grid(row=2, column=1, padx=5, pady=5)
    
    entry_nombre = tk.Entry(ventana_crear_usuario)
    entry_nombre.grid(row=2, column=2, padx=5, pady=5)
    entry_nombre.bind("<Return>", lambda event: entry_apellido.focus_set())
    
    label_apellido = tk.Label(ventana_crear_usuario, text="Apellido:")
    label_apellido.config(font=("Linkin Park ExtraBold", 15), bg= "#676767") 
    label_apellido.grid(row=3, column=1, padx=5, pady=5)
    
    entry_apellido = tk.Entry(ventana_crear_usuario)
    entry_apellido.grid(row=3, column=2, padx=5, pady=5)
    entry_apellido.bind("<Return>", lambda event: entry_rol.focus_set())
    
    label_rol = tk.Label(ventana_crear_usuario, text="Rol:")
    label_rol.config(font=("Linkin Park ExtraBold", 15), bg= "#676767") 
    label_rol.grid(row=4, column=1, padx=5, pady=5)
    
    entry_rol = tk.Entry(ventana_crear_usuario)
    entry_rol.grid(row=4, column=2, padx=5, pady=5)
    entry_rol.bind("<Return>", lambda event: button_registrarse.focus_set())
    
    entry_usuario.focus_set()   
    button_registrarse = tk.Button(ventana_crear_usuario, text="Registrarse", command=lambda: registrar_usuario(entry_usuario, entry_contrasena, entry_nombre, entry_apellido, entry_rol))
    button_registrarse.grid(row=5, column=1, columnspan=2, pady=10)
    button_registrarse.config(width=15, font=("M_karina",15, "bold"), fg = "#DAD5D6", bg="green",cursor = "hand2", activebackground= "#35BD6D")
    
    # Botón para abrir la ventana secundaria
    button_edicion_usuarios = tk.Button(ventana_crear_usuario, text="Edicion Usuarios", command=abrir_ventana_secundaria)
    button_edicion_usuarios.grid(row=6, column=1, columnspan=2, padx=5, pady=5)
    button_edicion_usuarios.config(width=15, font=("M_karina",15, "bold"), fg = "#DAD5D6", bg="green",cursor = "hand2", activebackground= "#35BD6D")
    
def abrir_ventana_secundaria():
        # Conectar a la base de datos
        conn = sqlite3.connect("database/Datcorr.db")
        cursor = conn.cursor()
        ventana_secundaria = tk.Toplevel()
        ventana_secundaria.title("Lista de Usuarios")
        ventana_secundaria.iconbitmap("img/datcorr.ico")
        ventana_secundaria.geometry("550x350")
        ventana_secundaria.resizable(0,0)
        ventana_secundaria.config(bg= "#676767")
        
        # Realiza una consulta para obtener la lista de usuarios desde la tabla Usuarios_database
        cursor.execute("SELECT * FROM Usuarios_database")
        usuarios = cursor.fetchall()

        # Crear un Treeview para mostrar los empleados
        treeview = tk.ttk.Treeview(ventana_secundaria)
        treeview['columns'] = ('nombre', 'apellido', 'usuario', 'contrasena', 'rol', 'registro')

        treeview.heading('#0', text='id_Usuarios')
        treeview.column('#0', width=75)
    
        treeview.heading('nombre', text='Nombre')
        treeview.column('nombre', width=75)
    
        treeview.heading('apellido', text='Apellido')
        treeview.column('apellido', width=75)
    
        treeview.heading('usuario', text='Usuario')
        treeview.column('usuario', width=75)
    
        treeview.heading('contrasena', text='Contraseña')
        treeview.column('contrasena', width=75)
    
        treeview.heading('rol', text='Rol')
        treeview.column('rol', width=75)
    
        treeview.heading('registro', text='Registro')
        treeview.column('registro', width=75)

        # Insertar los usuarios en el Treeview
        for usuario in usuarios:
            treeview.insert('', 'end', text=usuario[0], values=(usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6]))
        treeview.pack()

        # Botón para editar un usuario
        editar_button = tk.Button(ventana_secundaria, text="Editar usuario", command=lambda: editar_usuario(treeview, cursor, conn))
        editar_button.config(font=("Action of the Time", 16, "bold"), cursor="hand2")
        editar_button.pack()  

         # Botón para eliminar un usuario
        eliminar_button = tk.Button(ventana_secundaria, text="Eliminar usuario", command=lambda: eliminar_usuario(treeview, cursor, conn))
        eliminar_button.config(font=("Action of the Time", 16, "bold"), cursor="hand2")
        eliminar_button.pack()  

def editar_usuario(treeview, cursor, conn):
    # Obtener el ID del usuario seleccionado en el Treeview
    selected_item = treeview.selection()
    if len(selected_item) == 0:
        messagebox.showerror("Error", "Selecciona un usuario para editar.")
        return

    usuario_id = treeview.item(selected_item)['text']

    # Consultar los datos del usuario en la base de datos
    cursor.execute("SELECT * FROM Usuarios_database WHERE rowid = ?", (usuario_id,))
    usuario = cursor.fetchone()

    # Crear una nueva ventana emergente para editar los datos del usuario
    editar_ventana = tk.Toplevel()
    editar_ventana.title("Editar usuario")
    editar_ventana.geometry("300x300")
    editar_ventana.iconbitmap("img/datcorr.ico")
    editar_ventana.resizable(0,0)
    editar_ventana.config(bg= "#676767")
    label_nombre = tk.Label(editar_ventana, text="Edicion de usuarios")
    label_nombre.config(font=("Linkin Park ExtraBold", 10), bg= "#676767") 
    label_nombre.grid(row=0, column=0, columnspan=2)  # Se extiende a través de dos columnas

    # Etiquetas y entradas para editar los datos del usuario
    nombre_label = tk.Label(editar_ventana, text="Nombre:")
    nombre_label.grid(row=0, column=0, padx=5, pady=5)
    nombre_label.config(font=("Linkin Park ExtraBold", 11)) 
    nombre_entry = tk.Entry(editar_ventana)
    nombre_entry.bind("<Return>", lambda event: apellido_entry.focus_set())
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)
    nombre_entry.insert(0, usuario[1])

    apellido_label = tk.Label(editar_ventana, text="Apellido:")
    apellido_label.grid(row=1, column=0, padx=5, pady=5)
    apellido_label.config(font=("Linkin Park ExtraBold", 11)) 
    apellido_entry = tk.Entry(editar_ventana)
    apellido_entry.bind("<Return>", lambda event: usuario_entry.focus_set())
    apellido_entry.grid(row=1, column=1, padx=5, pady=5)
    apellido_entry.insert(1, usuario[2])

    usuario_label = tk.Label(editar_ventana, text="Usuario:")
    usuario_label.grid(row=2, column=0, padx=5, pady=5)
    usuario_label.config(font=("Linkin Park ExtraBold", 11)) 
    usuario_entry = tk.Entry(editar_ventana)
    usuario_entry.bind("<Return>", lambda event: contrasena_entry.focus_set())
    usuario_entry.grid(row=2, column=1, padx=5, pady=5)
    usuario_entry.insert(2, usuario[3])

    contrasena_label = tk.Label(editar_ventana, text="Contraseña:")
    contrasena_label.grid(row=3, column=0, padx=5, pady=5)
    contrasena_label.config(font=("Linkin Park ExtraBold", 11)) 
    contrasena_entry = tk.Entry(editar_ventana)
    contrasena_entry.bind("<Return>", lambda event: rol_entry.focus_set())
    contrasena_entry.grid(row=3, column=1, padx=5, pady=5)
    contrasena_entry.insert(3, usuario[4])

    rol_label = tk.Label(editar_ventana, text="Rol:")
    rol_label.grid(row=4, column=0, padx=5, pady=5)
    rol_label.config(font=("Linkin Park ExtraBold", 11)) 
    rol_entry = tk.Entry(editar_ventana)
    rol_entry.bind("<Return>", lambda event: guardar_button.focus_set())
    rol_entry.grid(row=4, column=1, padx=5, pady=5)
    rol_entry.insert(4, usuario[5])

    # Función para guardar los cambios del usuario
    def guardar_cambios():
        nuevo_nombre = nombre_entry.get()
        nuevo_apellido = apellido_entry.get()
        nuevo_usuario = usuario_entry.get()
        nueva_contrasena = contrasena_entry.get()
        nuevo_rol = rol_entry.get()        

        # Actualizar los datos del usuario en la base de datos
        cursor.execute("UPDATE Usuarios_database SET nombre = ?, apellido = ?, usuario = ?, contrasena = ?, rol = ? WHERE rowid = ?",
                      (nuevo_nombre, nuevo_apellido, nuevo_usuario, nueva_contrasena, nuevo_rol, usuario_id))
        conn.commit()
        messagebox.showinfo("Edición de usuario", "Los cambios han sido guardados correctamente.")

        # Actualizar el Treeview en la ventana secundaria
        treeview.item(selected_item, text=usuario_id, values=(nuevo_nombre, nuevo_apellido, nuevo_usuario, nueva_contrasena, nuevo_rol))

        editar_ventana.destroy()

    # Botón para guardar los cambios
    guardar_button = tk.Button(editar_ventana, text="Guardar cambios", command=guardar_cambios)
    guardar_button.config(font=("Action of the Time", 16, "bold"), cursor="hand2")
    guardar_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

def eliminar_usuario(treeview, cursor, conn):
    # Obtener el ID del usuario seleccionado en el Treeview
    selected_item = treeview.selection()
    if len(selected_item) == 0:
        messagebox.showerror("Error", "Selecciona un usuario para eliminar.")
        return

    usuario_id = treeview.item(selected_item)['text']

    # Confirmar la eliminación del usuario
    respuesta = messagebox.askyesno("Eliminar usuario",
                                    "¿Estás seguro de que deseas eliminar este usuario? Esta acción no se puede deshacer.")

    if respuesta:
        # Eliminar el usuario de la base de datos
        cursor.execute("DELETE FROM Usuarios_database WHERE rowid = ?", (usuario_id,))
        conn.commit()
        messagebox.showinfo("Eliminación de usuario", "El usuario ha sido eliminado correctamente.")

        # Eliminar el usuario del Treeview en la ventana secundaria
        treeview.delete(selected_item)

def asignar_nivel_seguridad(rol):
    niveles = {
        'admin': 'Admin',
        'editor': 'Editor',
        'viewer': 'Viewer',
        'guest': 'Guest'
    }
    return niveles.get(rol, 'Guest')

def registrar_usuario(entry_usuario, entry_contrasena, entry_nombre, entry_apellido, entry_rol):
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    rol = entry_rol.get()

    if not (usuario and contrasena and nombre and apellido and rol):
        messagebox.showwarning("Registro", "Todos los campos son obligatorios.")
        return

    # Asignar nivel de seguridad basado en el rol
    nivel_de_seguridad = asignar_nivel_seguridad(rol)

    # Verificar si el usuario ya existe en la base de datos
    conn = sqlite3.connect("database/Datcorr.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios_database WHERE usuario = ?", (usuario,))
    if cursor.fetchone():
        messagebox.showwarning("Registro", "El nombre de usuario ya está en uso.")
        conn.close()
        return

    # Insertar nuevo usuario en la base de datos
    cursor.execute("INSERT INTO Usuarios_database (nombre, apellido, usuario, contrasena, rol, nivel_de_seguridad) VALUES (?, ?, ?, ?, ?, ?)",
                   (nombre, apellido, usuario, contrasena, rol, nivel_de_seguridad))
    conn.commit()
    conn.close()


    messagebox.showinfo("Registro", "Usuario registrado exitosamente.")

CARPETA_EXCEL = "arch_exc"

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.grid(row=0, column=0, sticky="nsew")       

        self.etiqueta_reloj1 = tk.Label(self, font=('alarm clock', 28, 'bold'), bg="#676767", foreground='#000000')
        self.etiqueta_reloj1.grid(row=16, column=2)
        self.actualizar_reloj1()       

         # Configuración general de la grilla principal
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)  # Donde estará el Treeview

        self.crear_widgets()

    def actualizar_reloj1(self):
        tiempo_actual = strftime('%H:%M:%S %p')
        self.etiqueta_reloj1['text'] = tiempo_actual
        self.after(1000, self.actualizar_reloj1)

    def crear_widgets(self):
        # Label
        label = tk.Label(self, text="Dato a buscar:")
        label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Entry
        self.entry_busqueda = tk.Entry(self)
        self.entry_busqueda.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        

        # Combobox para seleccionar carpeta
        self.combo_area = ttk.Combobox(self, state="readonly")
        self.combo_area['values'] = self.obtener_areas()
        self.combo_area.grid(row=0, column=2, padx=10, pady=10)

        # Estilo personalizado para el botón "Buscar dato"
        style = ttk.Style()
        style.theme_use("clam")  # Usa un tema compatible

        style.configure("Buscar.TButton",
            font=("Segoe UI", 11, "bold"),
            foreground="white",
            background="#007acc",
            borderwidth=1,
            focusthickness=3,
            focuscolor='none',
            padding=6)

        style.map("Buscar.TButton",
            background=[("active", "#005f99"), ("pressed", "#004f80")],
            foreground=[("disabled", "gray")])

        # Botón de búsqueda

        btn_buscar = ttk.Button(self, text="Buscar dato", command=self.buscar_dato, style="Buscar.TButton")
        btn_buscar.grid(row=0, column=3, padx=5, pady=10, sticky="ew")

        # Dentro del __init__ de tu clase Frame:

        # Configurar que la fila donde está el Treeview ocupe todo el espacio disponible
        self.grid_rowconfigure(2, weight=1)  # Fila donde está frame_resultados
        self.grid_columnconfigure(0, weight=1)  # Columna principal

        # Frame para Treeview y Scrollbar
        self.frame_resultados = tk.Frame(self)
        self.frame_resultados.grid(row=2, column=0, columnspan=5, sticky="nsew")
        self.frame_resultados.columnconfigure(0, weight=1)  # Treeview
        self.frame_resultados.columnconfigure(1, weight=0)  # Scrollbar
        self.frame_resultados.rowconfigure(0, weight=1)     # Fila única

        # Crear Treeview y Scrollbar
        self.tree = None
        self.scroll_y = None
        self.crear_treeview([])  # Se inicializa vacío

    def obtener_areas(self):
        carpetas = []
        for item in os.listdir(CARPETA_EXCEL):
            path = os.path.join(CARPETA_EXCEL, item)
            if os.path.isdir(path):
                carpetas.append(item)
        return carpetas

    def crear_treeview(self, columnas):

        # Eliminar Treeview y scrollbar anteriores si existen
        if self.tree:
            self.tree.destroy()
        if self.scroll_y:
            self.scroll_y.destroy()

        # Crear Scrollbar
        self.scroll_y = ttk.Scrollbar(self.frame_resultados, orient="vertical")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        # Crear Treeview       

        self.tree = ttk.Treeview(self.frame_resultados,columns=columnas, show="headings", yscrollcommand=self.scroll_y.set)
        self.tree.grid(row=0, column=0, sticky="nsew")  # Se ajusta
        self.scroll_y.config(command=self.tree.yview)

        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="w", width=50)

    def buscar_dato(self):
        dato_busqueda = self.entry_busqueda.get().strip()
        carpeta_area = self.combo_area.get()
    
        if not dato_busqueda:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un dato para buscar.")
            return
        if not carpeta_area:
            messagebox.showwarning("Advertencia", "Seleccione un área para realizar la búsqueda.")
            return
    
        ruta_carpeta = os.path.join(CARPETA_EXCEL, carpeta_area)
        resultados = []
        columnas_resultado = None  # Para mantener orden
    
        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith((".xlsx", ".xls")):
                ruta_archivo = os.path.join(ruta_carpeta, archivo)
                try:
                    xls = pd.ExcelFile(ruta_archivo)
                    for hoja in xls.sheet_names:
                        df = xls.parse(hoja).astype(str)  # Todo como texto
                        coincidencias = df[df.apply(lambda row: row.str.contains(dato_busqueda, case=False, na=False).any(), axis=1)]
                        if not coincidencias.empty:
                            if columnas_resultado is None:
                                columnas_resultado = list(coincidencias.columns)  # Guardar orden
                            resultados.extend(coincidencias.values.tolist())
                except Exception as e:
                    print(f"Error al procesar {archivo}: {e}")
    
        if resultados and columnas_resultado:
            self.crear_treeview(columnas_resultado)
            for fila in resultados:
                self.tree.insert("", "end", values=fila)
        else:
            self.crear_treeview([])
            messagebox.showinfo("Sin resultados", "No se encontraron coincidencias.")

if __name__ == "__main__":
    app = Frame()
    app.mainloop()