import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dropdead51182',
    db = 'PuntoDeVenta'    
)

cursor = conexion.cursor()
cursor.execute("SELECT email_admin FROM administrator")
for data in cursor.fetchall():
    print(data)
    

conexion.close()