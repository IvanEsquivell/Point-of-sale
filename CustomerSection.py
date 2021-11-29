import mysql.connector
from Database import *

class Customer():
    
    def __init__(self):
        pass
    
    #METHOD VALIDATE CUSTOMER ACCOUNT
    def validateCustomer(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
    
    
    #METHOD CUSTOMERS'S MENU 
    def customerMenu(self):
        
        print("===========================================")
        print("Welcome, you're in Customers section")
        while True:
            try:
                print("\n1. Login ")
                print("2. Create account ")
                print("3. Products catalog ")
                print("4. Finalize purchase ")
                print("5. Customer support")
                print("6. Go back ")
                opc = int(input("Option: "))
                
                if opc == 1:
                    return 1
                
                elif opc == 2:
                    return 2
                
                elif opc == 3:
                    return 3
                
                elif opc == 4:
                    return 4
                
                elif opc == 5:
                    return 5
                
                elif opc == 6:
                    return 6
                
                elif opc < 1 or opc > 6:
                    print("Wrong option, try again \n")
                    
            except ValueError:
                print("Wrong data, try again \n")
    
    def login(self):
        print("================= Login =======================")
        
    
    def createAccount(self):
        print("============== Create account =================")
        
    
    def productsCatalog(self):
        print("============= Products catalog =================")
        
        
    def finalizePurchase(self):
        print("============= Finalize Purchase ================")
        
        
    def customerSupport(self):
        print("============= Customer support =================")