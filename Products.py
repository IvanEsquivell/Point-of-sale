import mysql.connector
from Database import *

class Products():
    
    #METHOD VALIDATE ADMINISTRATOR ACCOUNT
    def validateAdmin(self):
        
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        adminQuery = Database()                 #instancia de clase Database
        conexion = adminQuery.connection()      
        cursor = conexion.cursor()
        
        cursor.execute("SELECT email_admin FROM administrator")
        for data in cursor.fetchone():
            if email == data:
                pass     
    
    
    #METHOD PRODUCTS MENU
    def productsMenu(self):
        
        print("==========================================")
        print("Welcome, you're in Manage products section")
        
        while True:
            print("1. Add products")
            print("2. Cancel products")
            print("3. Modify products")
            print("4. Check stock")
            print("5. Add stock")
            print("6. Go back")
            option = int(input("Option: "))
            
            if option == 1:
                return 1
            
            elif option == 2:
                return 2
            
            elif option == 3:
                return 3
            
            elif option == 4:
                return 4
            
            elif option == 5:
                return 5
        
            elif option == 6:
                print("Going back...")
                break
                
            elif option < 1 or option > 6:
                print("Wrong option, try again \n")
                
    
    def addProducts(self):
        print("============== Add products ======================")
    
    
    def cancelProducts(self):
        print("============== Cancel products ===================")
    
    
    def modifyProducts(self):
        print("============== Modify products ===================")
    
    
    def checkStock(self):
        print("================ Check stock =====================")
    
    
    def addStock(self):
        print("================= Add stock ======================")