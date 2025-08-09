import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos = "database/Datcorr.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()     

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()


class Conexion_libroDB:
    def __init__(self):
        self.base_datos = "C:\Libro de Actas\Libro_de_actas.db"
        self.conexion = sqlite3.connect(self.base_datos_libro)
        self.cursor = self.conexion.cursor()     

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
