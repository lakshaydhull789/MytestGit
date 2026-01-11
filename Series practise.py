from pandas import Series
a=int(input("\n\tPlease enter the number of student data you want to enter: "))
R=[]
N=[]
for i in range(1,a+1):
    r=int(input(f"\n\tPlease enter roll number of {i} student: "))
    n=input(f"\n\tPlease enter name of {i} student: ")
    R.append(r)
    N.append(n)
print(R)
print(N)
S=Series(data=N,index=R)
print(S)
while True:
    print("\n\tWelcome to series based DBMS")
    print("\n\t1.Show all data\t2.Update Data\n\t3.Delete data\t4.Add Data")
    print("\n\t5.Size of whole data\t6.Show specific number of data")
    print("\n\t7.Change Index of a data")
    a=int(input("\n\tPlease select the option which you want to perform: "))
    if a==4:
        a1=int(input("\n\tPlease enter the number of student data you want to enter: "))
        count=1
        while count<=a1:
            while True:
                r=int(input("\n\tPlease enter roll number: "))
                if r in S.index:
                    print("\n\tRoll number already exists\n\tPlease use a different roll number")
                    continue
                count+=1
                name=input("\n\tPlease enter name: ")
                S[r]=name
                break
        print("\n\tData added successfully")
        print("\n\t",S)
    if a==3:
        d=int(input("\n\tPlease enter the roll number of student who's data you want to delete"))
        if d in S.index:
            print(f"\n\tName of student with roll no {d} is: ",S[d])
            con=int(input("\n\t\t'Are you sure you want to delete this data'\n\t1.Yes \t2.No\n\tPlease select your option: "))
            S.pop(d)
            print("\n\tData deleted successfully")
            print(S)
        else:
            print("\n\t\t'No data exist with this roll number'")
    if a==2:
        u=int(input("\n\tWhat you want to update\n\t1.Roll No.\t2.Name\n\tPlease choose your option: "))
        if u==1:
            ur=int(input("\n\tPlease enter the which roll number you want to update: "))
            if ur in S.index:
                print(f"\n\tStudent with roll no '{ur}' is: ",S[ur])
                urr=int(input("\n\tPlease enter the updated roll no: "))
                A=S[ur]
                print(f"\n\told roll no. '{ur}', updated roll no '{urr}')")
                S[urr]=A
                S.pop(ur)
                print(S)
            else:
                print(f"\n\t\tNo data exist with '{ur}' roll no")
        if u==2:
            un=int(input("\n\tPlease enter the roll no for which you want to update the name: "))
            if un in S.index:
                print(f"\n\tStudent with roll no '{ur}' is: ",S[ur])
                urr=input("\n\tPlease enter the updated Name: ")
                S[ur]=urr
                print("\n\tData updated succesfully")
                print(S)
                
