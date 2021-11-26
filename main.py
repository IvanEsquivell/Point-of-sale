from Administrator import *
from Products import *
from CustomerSection import *
import mysql.connector


while True:
    if __name__ == "__main__":
        try:
            print("================MENU=======================")
            print("1. Administrator")
            print("2. Manage products")
            print("3. Customer section")
            print("4. Close session")
            opc = int(input("Option: "))
            print("===========================================")
                
            if opc == 1:
                admin = Administrator()    
                admin.validateAdmin()
                    
            elif opc == 2:
                pass
                    
            elif opc == 3:
                pass
                    
            elif opc == 4:
                print("Closing session...")
                break
                    
            elif opc <= 0 or opc > 4:
                print("Wrong option, try again \n")
                    
        except ValueError:
            print("Wrong data, try again \n")
        

           