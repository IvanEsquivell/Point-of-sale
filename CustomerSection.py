import mysql.connector
from Database import *

def sales():
    
    
    def customerMenu(self):
        print("Welcome, you're in Customers section \n")
        print("--------------------------------------")
        while True:
            try:
                print("\n1. Login ")
                print("2. Create account ")
                print("3. Products catalog ")
                print("4. Finalize purchase ")
                print("5. Write suggestions ")
                print("6. Go back ")
                opc = int(input("Option: "))
                
                if opc == 1:
                    pass
                
                elif opc == 2:
                    pass
                
                elif opc == 3:
                    pass
                
                elif opc == 4:
                    pass
                
                elif opc == 5:
                    pass
                
                elif opc == 6:
                    break
                
                elif opc < 1 or opc > 5:
                    print("Wrong option, try again \n")
                    
            except ValueError:
                print("Wrong data, try again \n")
    
