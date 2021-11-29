import mysql.connector
from Database import *


class Administrator():
    
    def __init__(self):
        pass
    
    
    #METHOD VALIDATE ADMINISTRATOR ACCOUNT
    def validateAdmin(self):
        
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        adminQuery = Database()                 #instancia de clase Database
        conexion = adminQuery.connection()      #conectando a base de datos
        cursor = conexion.cursor()              
        
        cursor.execute("SELECT email_admin FROM administrator")
        for data in cursor.fetchone():
            if data == email:
                print("Correct email")
                    
    
    #METHOD MENU
    def adminMenu(self):
        while True:
            try:
                print("\n================MENU=======================")
                print("1. Consult accounts")
                print("2. Consult sales")
                print("3. Read suggestions")
                print("4. Go back")
                option = int(input("Option: "))
                
                if option == 1:
                    return 1

                if option == 2:
                    return 2
                
                if option == 3:
                    return 3
                
                if option == 4:
                    print("Going back...")
                    break
                                    
                elif option <= 0 or option > 4:
                    print("Wrong option, try again \n")
                    
            except ValueError:
                print("Wrong data, try again \n")
                
                
    #METHOD MANAGE ACCOUNTS
    def consult_accounts(self):
        print("============= Consult Accounts ==============")
        
        while True:
            print("1. Consult administrator accounts")
            print("2. Consult customers accounts")
            opc = int(input("Option: "))
            
            if opc == 1:
                adminQuery = Database()
                conexion = adminQuery.connection()
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM administrator")
                for data in cursor.fetchall():
                    print(data)
                break
            
            elif opc == 2:
                customerQuery = Database()
                conexion = customerQuery.connection()
                cursor = conexion.cursor()
                cursor.execute("SELECT email_customer FROM customer")
                for data in cursor.fetchall():
                    print(data)
                break
            
            elif opc < 1 or opc > 2:
                print("Wrong option, try again \n")
        
    
    
    #METHOD CONSULT SALES
    def consult_sales(self):
        print("============= Consult Sales =================")
    
    
    #METHOD READ SUGGESTIONS
    def read_suggestions(self):
        print("============ Read Suggestions ==============")
    

