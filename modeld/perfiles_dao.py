from .conexion_db import ConexionDB
from .conexion_db import Conexion_libroDB
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

def crear_tabla():
    conexion = ConexionDB()

    sql = """CREATE TABLE Catastro_database(id_Catastro_database INTEGER PRIMARY KEY,
    denominacion TEXT,
    departamento TEXT,
    expediente TEXT,
    estado TEXT,
    caratula TEXT,
    ingreso TEXT,
    egreso TEXT,
    ultimo_movimiento TEXT,
    n_lote TEXT,
    minuta TEXT,
    plano TEXT,
    ficha TEXT,
    zona TEXT,
    caja TEXT,
    registro DATETIME DEFAULT CURRENT_TIMESTAMP)"""
    
    #PRIMARY KEY(id_busqueda AUTOINCREMENT
    try:

       conexion.cursor.execute(sql)
       conexion.cerrar()
       titulo = "Crear Registro"
       mensaje = "Se creo la tabla en la base de datos"
       messagebox.showinfo(titulo, mensaje)
    except:
    
       titulo = "Crear Registro"
       mensaje = "La tabla ya esta creada"
       messagebox.showwarning(titulo, mensaje)

def tabla_libro_actas():
    conexion_libro = Conexion_libroDB()

    sql = """CREATE TABLE IF NOT EXISTS Libro_de_actas_database (
                    id_Libro_database INTEGER PRIMARY KEY,
                    denominacion TEXT,
                    departamento TEXT,
                    expediente TEXT,
                    estado TEXT,
                    caratula TEXT,
                    ingreso TEXT,
                    egreso TEXT,
                    ultimo_movimiento TEXT,
                    n_lote TEXT,
                    minuta TEXT,
                    plano TEXT,
                    ficha TEXT,
                    zona TEXT,
                    caja TEXT,
                    registro DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
    #PRIMARY KEY(id_busqueda AUTOINCREMENT
    try:
       conexion_libro.cursor.execute(sql)
       conexion_libro.cerrar()
       titulo = "Crear Registro"
       mensaje = "Se creo la tabla en la base de datos"
       messagebox.showinfo(titulo, mensaje)
       
    except:    
       titulo = "Crear Registro"
       mensaje = "La tabla ya esta creada"
       messagebox.showwarning(titulo, mensaje)    

def crear_tabla_usuarios():
    conexion = ConexionDB()

    sql = """CREATE TABLE IF NOT EXISTS Usuarios_database(
    id_Usuarios_database INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    usuario TEXT UNIQUE,
    contrasena TEXT, 
    rol TEXT,
    nivel_de_seguridad TEXT,
    registro DATETIME DEFAULT CURRENT_TIMESTAMP)"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro de Usuarios"
        mensaje = "Se creó la tabla de USUARIOS en la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Registro de USUARIOS"
        mensaje = "La tabla de Registro de USUARIOS ya está creada"
        messagebox.showwarning(titulo, mensaje)

class Busqueda:
    def __init__(self, denominacion, departamento, expediente, estado, caratula, ingreso, egreso, ultimo_movimiento, n_lote, minuta, plano, ficha, zona, caja, registro):
        self.id_Catastro_database = None
        self.denominacion = denominacion
        self.departamento = departamento
        self.expediente = expediente
        self.estado = estado
        self.caratula = caratula
        self.ingreso = ingreso
        self.egreso = egreso
        self.ultimo_movimiento = ultimo_movimiento
        self.n_lote = n_lote
        self.minuta = minuta
        self.plano = plano
        self.ficha = ficha
        self.zona = zona
        self.caja = caja
        self.registro = None

    def __str__(self):
        return f"Busqueda[{self.denominacion}, {self.departamento}, {self.expediente},{self.estado}, {self.caratula},{self.ingreso},{self.egreso},{self.ultimo_movimiento},{self.n_lote},{self.minuta},{self.plano},{self.ficha},{self.zona},{self.caja},{self.registro}]"

from datetime import datetime

def guardar(Catastro_database):
    conexion = ConexionDB()

    # Agrega la fecha y hora al objeto Busqueda
    Catastro_database.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = f"""INSERT INTO Catastro_database (denominacion, departamento, expediente, estado,
    caratula, ingreso, egreso, ultimo_movimiento, n_lote, minuta, plano, ficha, zona, caja, registro)
    VALUES('{Catastro_database.denominacion}', 
    '{Catastro_database.departamento}', 
    '{Catastro_database.expediente}', 
    '{Catastro_database.estado}', 
    '{Catastro_database.caratula}', 
    '{Catastro_database.ingreso}', 
    '{Catastro_database.egreso}', 
    '{Catastro_database.ultimo_movimiento}', 
    '{Catastro_database.n_lote}', 
    '{Catastro_database.minuta}', 
    '{Catastro_database.plano}', 
    '{Catastro_database.ficha}',
    '{Catastro_database.zona}', 
    '{Catastro_database.caja}',
    '{Catastro_database.registro}')"""

    try:
       conexion.cursor.execute(sql)
       conexion.cerrar()
    except:
       titulo = "Conexion al Registro"
       mensaje = "La tabla Catastro_database no está creada en la base de datos"
       messagebox.showerror(titulo, mensaje)

from datetime import datetime

def guardar(Catastro_database):
    conexion = ConexionDB()

    # Agrega la fecha y hora al objeto Busqueda
    Catastro_database.registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = f"""INSERT INTO Catastro_database (denominacion, departamento, expediente, estado,
    caratula, ingreso, egreso, ultimo_movimiento, n_lote, minuta, plano, ficha, zona, caja, registro)
    VALUES('{Catastro_database.denominacion}', 
    '{Catastro_database.departamento}', 
    '{Catastro_database.expediente}', 
    '{Catastro_database.estado}', 
    '{Catastro_database.caratula}', 
    '{Catastro_database.ingreso}', 
    '{Catastro_database.egreso}', 
    '{Catastro_database.ultimo_movimiento}', 
    '{Catastro_database.n_lote}', 
    '{Catastro_database.minuta}', 
    '{Catastro_database.plano}', 
    '{Catastro_database.ficha}',
    '{Catastro_database.zona}', 
    '{Catastro_database.caja}',
    '{Catastro_database.registro}')"""

    try:
       conexion.cursor.execute(sql)
       conexion.cerrar()
    except:
       titulo = "Conexion al Registro"
       mensaje = "La tabla Catastro_database no está creada en la base de datos"
       messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()

    lista_Catastro_database = []

    sql = "SELECT * FROM Catastro_database"

    try:
        conexion.cursor.execute(sql)
        lista_Catastro_database = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "Crea la tabla en la Base de datos"
        messagebox.showwarning(titulo, mensaje)

    return lista_Catastro_database

def editar(Catastro_database, id_Catastro_database):
    conexion = ConexionDB()

    sql = f"""UPDATE Catastro_database 
    SET denominacion = '{Catastro_database.denominacion}', 
    departamento = '{Catastro_database.departamento}', 
    expediente = '{Catastro_database.expediente}', 
    estado = '{Catastro_database.estado}',
    caratula = '{Catastro_database.caratula}', 
    ingreso = '{Catastro_database.ingreso}', 
    egreso = '{Catastro_database.egreso}', 
    ultimo_movimiento = '{Catastro_database.ultimo_movimiento}', 
    n_lote = '{Catastro_database.n_lote}', 
    minuta = '{Catastro_database.minuta}', 
    plano = '{Catastro_database.plano}', 
    ficha = '{Catastro_database.ficha}',
    zona = '{Catastro_database.zona}', 
    caja = '{Catastro_database.caja}'

    WHERE id_Catastro_database = {id_Catastro_database}"""    

    try:
       print(sql)
       conexion.cursor.execute(sql)
       conexion.cerrar()
      
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        titulo = "Edicion de datos"
        mensaje = "No se a podido editar este registro"
        messagebox.showerror(titulo, mensaje)

def eliminar(id_Catastro_database):
    conexion = ConexionDB()
    sql = f"DELETE FROM Catastro_database WHERE id_Catastro_database = {id_Catastro_database}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Eliminar Datos"
        mensaje = "No se pudo eliminar el registro"
        messagebox.showerror(titulo, mensaje)