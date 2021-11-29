import mysql.connector

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'dropdead51182'
        self.database = 'PuntoDeVenta'
        
        
    #METODO PARA CONECTARSE A LA BASE DE DATOS NECESARIO  
    def connection(self):
        conexion = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        
        return conexion     
        
