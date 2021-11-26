import mysql.connector
from Database import *


class Administrator():
    
    def __init__(self):
        pass
    
    
    def validateAdmin(self):
        
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        adminQuery = Database()
        conexion = adminQuery.connection()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT email_admin FROM administrator")
        for data in cursor.fetchone():
            if email == data:
                break
            
    
    def adminMenu(self):
        print("=============MENU=================")
    
    def manage_accounts(self):
        pass
    
    
    def consult_sales(self):
        pass
    
    
    def read_suggestions(self):
        pass
    

