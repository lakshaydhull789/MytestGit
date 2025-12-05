    #Stock inventory management system
from stockfunction import*
while True:
    print("\n\t\tWelcome to Inventory and Stock Management System")
    print("\n\t\t1. Add Product")
    print("\t\t2. Update Product details")
    print("\t\t3. View all inventory")
    print("\t\t4. Show items which are out of stock")
    print("\t\t5. Want to see a specific product?")
    print("\t\t6. Delete a certain product out of Inventory")
    print("\t\t7. Create a text document file")
    print("\t\t8. Exit")
    a=input("\t\tPlease select the operation you want to perform: ")
    if a not in ['1','2','3','4','5','6','7','8']:
        print("\t\tPlease try again")
        continue
    a =int(a)
    if a==1:
        addprdt()
    if a==2:
        updtprdt()
    if a==3:
        viewall()
    if a==4:
        outstk()
    if a==5:
        spfprdt()
    if a==6:
        delprdt()
    if a==7:
        textdmt()
    if a==8:
        print("\t\tThank you for using our application")
        break
'''
    try :
        if not (1<=a<=8):
            print("\t\tInvalid input")
    except Exception as e :
        print("invalid . please try again")
        continue
 '''       
