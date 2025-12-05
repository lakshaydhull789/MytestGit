
#Functions of Stock inventory management
import mysql.connector as m
con=m.connect(host="localhost",user="root",password="",database="Inventory")
cur=con.cursor()
import tabulate as t1
def addprdt():
    
    while True:
    
        i=input("\t\tPlease enter product ID: ")
        cur.execute(f"select*from productdetails where ID='{i}'")
        data=cur.fetchall()
        if data==[]:
            n=input("\t\tPlease enter product Name: ")
            if len(n)>=3:
                print("('ELECTRONICS','MEDICINE','FOOD','TOY','STATIONARY','OTHERS')")
                t=input("\t\tPlease enter product type: ")
                if t.upper() in ['ELECTRONICS','MEDICINE','FOOD','TOY','STATIONARY','OTHERS']:
                    f=input("\t\tPlease enter product manufacturer: ")
                    if len(f)>1:
                        a=input("\t\tPlease enter manufacturer address: ")
                        q=input("\t\tPlease enter product Quantity: ")
                        if q<'0':
                            print("\t\tQuantity can not be negative")
                        elif q.isalpha():
                            print("\t\tQuantity can not contain Alphabets")
                        else:
                            k=input("\t\tPlease enter product key: ")
                            cur.execute(f"select*from productdetails where Product_key='{k}'")
                            data=cur.fetchall()
                            if data==[]:
                                cur.execute(f"\t\tinsert into productdetails values('{i}','{n}','{t}','{f}','{a}','{q}','{k}')")
                                con.commit()
                                print("\t\tProduct details added to inventory")
                                break
                            else:
                                print(f"\t\tProduct with key '{k}'already exists")
                    else:
                        print("\t\tManufacturer Name is too short")
                else:
                    print("\t\tInvalid Product Type")
            else:
                print("\t\tName is too short please enter proper name")
        else:
            print("\n\t\tProduct with this ID already exists below are the details of the product")
            cur.execute(f"select*from productdetails where ID='{i}'")
            data==cur.fetchall()
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="pretty"))
            u=int(input("\t\tPlease enter updated product quantity: "))
            cur.execute(f"update productdetails set quantity='{u}' where ID='{i}' ")
            con.commit()
            print(f"\t\tUpdate product detail with product ID: '{i}'")
            cur.execute(f"select*from productdetails where ID='{i}'")
            data=cur.fetchall()
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt='pretty'))
def viewall():
    print("\n\t\t\tIn which order you want to see your Inventory")
    print("\t\t1.By ID")
    print("\t\t2.By Name")
    print("\t\t3.By Type")
    print("\t\t4.By Manufacturer")
    print("\t\t5.By Quantity")
    print("\t\t6.View all data")
    vl=(input("\n\t\tPlease enter the operation number: "))
    if vl=='1':
        print("Do you want to see it in Asending or Descending order")
        print("1. In ASCENDING ORDER of ID")
        print("2. In DESCENDING ORDER of ID")
        ads=input("Please enter you prefered choice number: ")
        if ads=='1':
            cur.execute("select*from productdetails order by ID")
            data=cur.fetchall()
            print("\n\tData in Ascending order of Product ID;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        elif ads=='2':
            cur.execute("select*from productdetails order by ID desc")
            data=cur.fetchall()
            print("\n\tData in Desending order of Product ID;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        else:
            print("\n\t\tInvalid operation number selected")
    if vl=='2':
        print("Do you want to see it in Asending or Descending order")
        print("1. In ASCENDING ORDER of Name")
        print("2. In DESCENDING ORDER of Name")
        ads=input("Please enter you prefered choice number: ")
        if ads=='1':
            cur.execute("select*from productdetails order by Product_Name")
            data=cur.fetchall()
            print("\n\tData in Ascending order of Product Name;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        elif ads=='2':
            cur.execute("select*from productdetails order by Product_Name desc")
            data=cur.fetchall()
            print("\n\tData in Descending order of Product Name;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        else:
            print("\n\t\tInvalid operation number selected")
    if vl=='3':
        print("Do you want to see it in Asending or Descending order")
        print("1. In ASCENDING ORDER of Type")
        print("2. In DESCENDING ORDER of Type")
        ads=input("Please enter you prefered choice number: ")
        if ads=='1':
            cur.execute("select*from productdetails order by Product_type")
            data=cur.fetchall()
            print("\n\tData in Ascending order of Product Type;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        elif ads=='2':
            cur.execute("select*from productdetails order by Product_type desc")
            data=cur.fetchall()
            print("\n\tData in Descending order of Product Type;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        else:
            print("\n\t\tInvalid operation number selected")
    if vl=='4':
        print("Do you want to see it in Asending or Descending order")
        print("1. In ASCENDING ORDER of Manufacturer")
        print("2. In DESCENDING ORDER of Manufacturer")
        ads=input("Please enter you prefered choice number: ")
        if ads=='1':
            cur.execute("select*from productdetails order by Manufacturer")
            data=cur.fetchall()
            print("\n\tData in Ascending order of Manufacturer;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        elif ads=='2':
            cur.execute("select*from productdetails order by Manufacturer desc")
            data=cur.fetchall()
            print("\n\tData in Descending order of Manufacturer;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        else:
            print("\n\t\tInvalid operation number selected")
    if vl=='5':
        print("Do you want to see it in Asending or Descending order")
        print("1. In ASCENDING ORDER by Quantity")
        print("2. In DESCENDING ORDER by Quantity")
        ads=input("Please enter you prefered choice number: ")
        if ads=='1':
            cur.execute("select*from productdetails order by Quantity")
            data=cur.fetchall()
            print("\n\tData in Ascending order of Quantity;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        elif ads=='2':
            cur.execute("select*from productdetails order by Quantity desc")
            data=cur.fetchall()
            print("\n\tData in Descending order of Quantity;)\n")
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
        else:
            print("\n\t\tInvalid operation number selected")
    if vl=='6':
        cur.execute("select * from productdetails")
        data=cur.fetchall()
        print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if vl not in ['1','2','3','4','5','6']:
        print("\t\tInvalid option selected please try again")
'''
def updtprdt():
    print("\n\t\tWhich detail you want to update")
    print("\t\t1.Update ID")
    print("\t\t2.Update Name")
    print("\t\t3.Update Type")
    print("\t\t4.Update Manufacturer")
    print("\t\t5.Update Quantity")
    vl=input("\t\tPlease enter the operation number you want to perform")
    if vl==1:
        ne=input("\t\tPlease enter current ID of the product you want to update")
        cur.execute(f"select*from productdetails where ID='{ne}'")
'''        
def updtprdt():
    cur.execute(f"select*from productdetails")
    data=cur.fetchall()
    print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    vl=input("\n\t\tPleas enter Product key for which you want to update the details: ")
    cur.execute(f"select*from productdetails where Product_Key='{vl}'")
    data=cur.fetchall()
    print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    print("\n\t\tWhat you want to update")
    print("\t\t1. ID")
    print("\t\t2. Name")
    print("\t\t3. Type")
    print("\t\t4. Manufacturer")
    print("\t\t5. Quantity")
    uh=input("\t\tPlease select what you want to update: ")
    if uh=='1':
        up=input("\t\tPlease enter updated product ID: ")
        cur.execute(f"update productdetails set ID='{up}' where product_key='{vl}'")
        con.commit()
        cur.execute(f"select*from productdetails where Product_Key='{vl}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product with this product key")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if uh=='3':
        up=input("\t\tPlease enter updated product Type: ")
        cur.execute(f"update productdetails set product_type='{up}' where product_key='{vl}'")
        con.commit()
        cur.execute(f"select*from productdetails where Product_Key='{vl}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product with this product Key")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if uh=='4':
        up=input("\t\tPlease enter updated product Manufacturer: ")
        cur.execute(f"update productdetails set Manufacturer='{up}' where product_key='{vl}'")
        con.commit()
        cur.execute(f"select*from productdetails where Product_Key='{vl}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product with this product key")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if uh=='2':
        up=input("\t\tPlease enter updated product Name: ")
        cur.execute(f"update productdetails set Product_Name='{up}' where product_key='{vl}'")
        con.commit()
        cur.execute(f"select*from productdetails where Product_Key='{vl}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product with this product key")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if uh=='5':
        up=input("\t\tPlease enter updated product Quantity: ")
        cur.execute(f"update productdetails set Quantity='{up}' where product_key='{vl}'")
        con.commit()
        cur.execute(f"select*from productdetails where Product_Key='{vl}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product with this product key")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if uh not in ['1','2','3','4','5']:
        print("\t\tInvalid option selected please try again")
def outstk():
    print("\t\tThese are the product in inventory that are out of stock")
    cur.execute("select*from productdetails where quantity=0")
    data=cur.fetchall()
    if data==[]:
        print("There's no such product which is out of stock")
    else:
        print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
def delprdt():
    print("Do you want to delete a certain product or entire data\n\t\t1. Entire data\t2. Certain Product")
    pdk=input("\t\tPlease enter your choice: ")
    if pdk.upper() in ['1','YES']:
        cur.execute("select * from productdetails")
        data=cur.fetchall()
        if data==[]:
            print("There's no data in our Inventory")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
            dc=input("\t\tDo you want to delete the entire data. \n1.Yes \t2.No.\n\t\tPlease type your selected option: ")
            if dc=='1':
                cur.execute(f"delete from productdetails where product_key='{pk}'")
                con.commit()
                print("\t\t","*"*35)
                print(f"\t\t| Entire data deleted succesfully |")
                print("\t\t","*"*35)
            else:
                print("\t\tNo data deleted")
    if pdk.upper()in ['2','NO']:
        print("Do you know about product key of the product which you want to delete")
        print("\t\t1. Yes")
        print("\t\t2. No")
        dpk=input("\t\tPlease select an option: ")
        if dpk=='1':
            pk=input("\t\tPlease enter product key: ")
            cur.execute(f"select*from productdetails where product_key='{pk}'")
            data=cur.fetchall()
            if data==[]:
                print("There's no such product with this product key")
            else:
                print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
                dc=input("\t\tDo you want to delete this data. \n1.Yes \t2.No.\n\t\tPlease type your selected option: ")
                if dc=='1':
                    cur.execute(f"delete from productdetails where product_key='{pk}'")
                    con.commit()
                    print("\t\t","*"*60)
                    print(f"\t\t| Product with Product key: {pk} is deleted |")
                    print("\t\t","*"*60)
                else:
                    print("\t\tNo data deleted")
        else:       
            print("\t\tWhat detail do you know about your product")
            print("1. Name")
            print("2. ID")
            print("3. Type")
            print("4. Manufacturer")
            td=input("\t\tPlease select the option which you know about your Product: ")
            if td=='1':
                pn=input("\t\tPlease enter product name: ")
                cur.execute(f"select * from productdetails where Product_Name='{pn}'")
                data=cur.fetchall()
                if data==[]:
                    print("There's no such product with this Name")
                else:
                    print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
                    print("\t\tAre you sure you want to delete this data. \n\t\t1. Yes\t2. No.")
                    dc=input("\t\tPlease enter your choice: ")
                    if dc=='1':
                        cur.execute(f"delete from productdetails where product_name='{pn}'")
                        con.commit()
                        print("\t\t","*"*60)
                        print(f"\t\t| Product with Product Name: {pn} is deleted |")
                        print("\t\t","*"*60)
                    else:
                        print("\t\tNo data deleted")
            if td=='2':
                pn=input("\t\tPlease enter product ID: ")
                cur.execute(f"select * from productdetails where ID='{pn}'")
                data=cur.fetchall()
                if data==[]:
                    print("There's no such product with this ID")
                else:
                    print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
                    print("\t\tAre you sure you want to delete this data. \n\t\t1. Yes\t2. No.")
                    dc=input("\t\tPlease enter your choice: ")
                    if dc=='1':
                        cur.execute(f"delete from productdetails where ID='{pn}'")
                        con.commit()
                        print("\t\t","*"*60)
                        print(f"\t\t| Product with Product ID: {pn} is deleted |")
                        print("\t\t","*"*60)
                    else:
                        print("\t\tNo data deleted")
            if td=='3':
                pn=input("\t\tPlease enter product type: ")
                cur.execute(f"select * from productdetails where product_type='{pn}'")
                data=cur.fetchall()
                if data==[]:
                    print("There's no such product of this Type")
                else:
                    print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
                    print("\t\tAre you sure you want to delete this data. \n\t\t1. Yes\t2. No.")
                    dc=input("\t\tPlease enter your choice: ")
                    if dc=='1':
                        cur.execute(f"delete from productdetails where product_type='{pn}'")
                        con.commit()
                        print("\t\t","*"*60)
                        print(f"\t\t| Product with Product type: {pn} is deleted |")
                        print("\t\t","*"*60)
                    else:
                        print("\t\tNo data deleted")
            if td=='4':
                pn=input("\t\tPlease enter product Manufacturer: ")
                cur.execute(f"select * from productdetails where manufacturer='{pn}'")
                data=cur.fetchall()
                if data==[]:
                    print("There's no product by this Manufacturer")
                else:
                    print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
                    print("\t\tAre you sure you want to delete this data. \n\t\t1. Yes\t2. No.")
                    dc=input("\t\tPlease enter your choice: ")
                    if dc.upper in ['1','YES']:
                        cur.execute(f"delete from productdetails where manufacturer='{pn}'")
                        con.commit()
                        print("\t\t","*"*60)
                        print(f"\t\t| Product by Manufacturer: {pn} is/are deleted |")
                        print("\t\t","*"*60)
                    else:
                        print("\t\tNo data deleted")
            if td not in ['1','2','3','4']:
                print("\t\tInvalid option selected please try again")
        if pdk.upper() not in ['1','2','YES','NO']:
            print("Invalid option selected")

def spfprdt():
    print("\t\tWhat detail do you know about your product")
    print("1. Name")
    print("2. ID")
    print("3. Type")
    print("4. Manufacturer")
    td=input("\t\tPlease select the option which you know about your Product: ")
    if td=='1':
        pn=input("\t\tPlease enter product name: ")
        cur.execute(f"select * from productdetails where Product_Name='{pn}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product with this Name")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if td=='2':
        pn=input("\t\tPlease enter product ID: ")
        cur.execute(f"select * from productdetails where ID='{pn}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product with this ID")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))    
    if td=='3':
        pn=input("\t\tPlease enter product type: ")
        cur.execute(f"select * from productdetails where product_type='{pn}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no such product of this Type")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if td=='4':
        pn=input("\t\tPlease enter product Manufacturer: ")
        cur.execute(f"select * from productdetails where manufacturer='{pn}'")
        data=cur.fetchall()
        if data==[]:
            print("There's no product by this Manufacturer")
        else:
            print(t1.tabulate(data,headers=('ID','Name','Type','Manufacturer','address','Quantity','Product Key'),tablefmt="grid"))
    if td not in ['1','2','3','4']:
        print("\t\tInvalid option selected please try again")
def textdmt():
    flname=input("\t\tPlease enter file name: ")
    flname="C:\\Users\\Lakshay\\OneDrive\\Desktop\\python all codes\\File Handling\\"+flname+".txt"
    a=open(flname,"w")
    cur.execute("Select * from productdetails")
    data=cur.fetchall()
    if data==[]:
        print("\n\tNo records found")
    else:
        record=1
        for i in data:
            a.write(f"\t\t\tRecord Number= {record}\n")
            a.write(f"Id: {i[0]}|Name: {i[1]}|Type: {i[2]}|Manufacturer: {i[3]}|Address: {i[4]}|Quantity: {i[5]}|Key: {i[6]}\n")
            a.write("_________________________________________________________________________________________________________\n")
            record=record+1
        a.close()
        print(f"\n\tFile saved at Location: {flname}")
