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
            
            #ADMINISTRATOR FUNCTIONS    
            if opc == 1:
                admin = Administrator()    
                admin.validateAdmin()
                value = admin.adminMenu()
                
                if value == 1:
                    admin.consult_accounts()
                    
                elif value == 2:
                    admin.consult_sales()
                    
                elif value == 3:
                    admin.read_suggestions()
                    
                    
            #PRODUCTS FUNCTIONS        
            elif opc == 2:
                product = Products() 
                product.validateAdmin()
                valueProd = product.productsMenu()
                
                if valueProd == 1:
                    product.addProducts()
                    
                elif valueProd == 2:
                    product.cancelProducts()
                  
                elif valueProd == 3:
                    product.modifyProducts()             
                    
                elif valueProd == 4:
                    product.checkStock()
                 
                elif valueProd == 5:
                    product.addStock()
                    
                            
            #CUSTOMER FUNCTIONS         
            elif opc == 3:
                customer = Customer()
                customer.validateCustomer()              
                valueCust = customer.customerMenu()
                
                if valueCust == 1:
                    customer.login()
                    
                elif valueCust == 2:
                    customer.createAccount()
                    
                elif valueCust == 3:
                    customer.productsCatalog()
                    
                elif valueCust == 4:
                    customer.finalizePurchase()
                    
                elif valueCust == 5:
                    customer.customerSupport()
                    
                    
            elif opc == 4:
                print("Closing session...")
                break
                    
            elif opc <= 0 or opc > 4:
                print("Wrong option, try again \n")
                    
        except ValueError:
            print("Wrong data, try again \n")
        

           