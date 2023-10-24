#try:
import datetime
from tkinter.ttk import *
from tkinter import *
print("...........WELCOME TO HP GAS AGENCY.........")
print("...........GOLGHAR,NEAR PETROL PUMP,GORAKHPUR...")
from tkinter import messagebox
import mysql.connector as ms
cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
query=cursor.cursor()
query.execute("drop table if exists gas_agency")
query.execute("create table gas_agency(Account_number char(5) NOT NULL primary key ,Weight int NOT NULL,Phone_No char(10) NOT NULL,EMAILID varchar(30) NOT NULL check (EMAILID like '%@gmail.com'),Date_Of_Booking date NOT NULL,Mode_Of_Payment varchar(20),deliverydate varchar(20),deliveryboy varchar(30))")
query.execute('drop table if exists Customers')
query.execute('CREATE TABLE Customers(Fullname varchar(30),customerid int(5),Phone varchar(10),Email varchar(30),Gender varchar(10),branch varchar(20),cateogry varchar(10))')
query.execute('drop table if exists delivery')
query.execute('CREATE TABLE delivery(Fullname varchar(30),id int(5),Phone varchar(10),Email varchar(30),Gender varchar(10),branch varchar(20),charges varchar(10),status varchar(19))')

from tkinter.ttk import *
def menu():
            print("MENU")
            print("1:View order details")
            print("2:View employee details")
            print("3:Add new Employee details")
            print("4:update Employee details")
            print("5:delete Employee record")
            print("6:View all registered Customer")
            print("7:Exit to main menu")
            print("...........................................")
def menua():
            print('Menu:')
            print('1:View order details')
            print('2:View Delivery_Boy details')
            print('3:View Customer details')
            print('4:Add new Delivery_Boy detail')
            print('5:Update Delivery_Boy detail')
            print('6:Delete Delivery_Boy record')
            print('7:Assign delivery_boy to the orders')
            print('8:Exit to main menu')
query.execute("drop table if exists empl")
query.execute("create table empl(Ename varchar(18),Eid int(5),Esal int(20),EJob varchar(12),Eage int)")
while True:
    print("SELECT YOUR JOB")
    print("1:Administrator Login")
    print("2:Customer Login")
    print("3:Staff login")
    print("4:Exit")
    print(".................................................")
    q=(input("press now......."))
    if str(q).isalpha():
        print("ERROR INPUT.....^^~#@&^")
        print('Reedirecting again')
        print("..................................................")
    if q.isdigit():
        if int(q)==1:
            w=input("Enter Administrator Password:")
            if w=="123hp":
                print("..........SUCCESSFULLY LOGINED.....")
                print("MENU")
                print("1:View order details")
                print("2:View employee details")
                print("3:Add new Employee details")
                print("4:update Employee details")
                print("5:delete Employee record")
                print("6:View Customer details")
                print("7:Exit to main menu")
                while True:
                    print('Press 0 to see the menu..........')
                    print(".................................................................")
                    e=input("choose now.....")
                    if e.isalpha():
                        print('You have input a string....$ERROR$....')
                        print(".................................................................")
                    if e.isdigit():
                        if int(e)==1:
                            query=cursor.cursor()
                            query.execute("select * from gas_agency")
                            a=query.fetchall()
                            if len(a)==0:
                                print("No booking Yet")
                                print(".................................................................")
                            else:
                                print(": acc no. : weight : phone      : email                          : date       : mode                : delivery date     : delivery boy ")
                                for r in a:
                                 print(':',(r[0]),' '*(6-len(r[0])),':','  ',r[1],' :',r[2],':',r[3],' '*(28-len(r[3])),':',r[4],':',r[5],' '*(20-len(r[5])),":",r[6],':','   ',':',r[7]) 
                        if int(e)==2:
                            query=cursor.cursor()
                            query.execute("select * from empl")
                            a=query.fetchall()
                            if len(a)==0:
                                print("No Employee Exist in Your Firm")
                            else:
                                print("Emp.name          :Empl.Id :salary   : Emplyoee job  : Age")
                                for r in a:
                                        print(r[0],' '*(16-len(r[0])),':',r[1],":",'',r[2],' '*(6-len(str(r[2]))),':',r[3],' '*(12-len(r[3])),':',r[4])
                        if int(e)==3:
                            try:
                                query=cursor.cursor()
                                n=input("Enter Employee name:'")
                                i=int(input("Enter Employee Id(5 digits)"))
                                s=int(input("Enter Employee salary"))
                                j=input("Enter Emplyee job:")
                                age=int(input("Enter Emplyee age:"))
                                print(".................................................................")
                                if n.isalpha()==True and str(i).isdigit()==True and str(s).isdigit()==True and j.isalpha()==True and str(age).isdigit()==True and len(str(i))==5:
                                    query.execute("insert into empl values('%s',%s,%s,'%s',%s)"%(n,i,s,j,age))
                                    cursor.commit()
                                    print('ADDITION SUCCESSFUL')
                                    print(".................................................................")
                                else:
                                    print('.........WRONG INPUT...........' )
                                    print(".................................................................")
                            except:
                               print('.........WRONG INPUT...........' )
                        if int(e)==4:
                            n=input('Enter employee Name....:')
                            query=cursor.cursor()
                            query.execute('select * from empl')
                            y=query.fetchall()
                            a=0
                            for l in range(len(y)):
                                if y[l][0]==n or y[l][0]==n.upper() or (y[l][0]).upper()==n:
                                    a=+1
                                    print('''1:EMLOYEE NAME
2:EMPLOYEE ID
3:EMPLOYEE SALARY
4:EMPLOYEE JOB
5:EMPLOYEE AGE''')
                                    print(".................................................................")
                                    try:
                                        f=int(input('What do you want to update:'))
                                        D={1:'Ename',2:'Eid',3:'Esal',4:'EJob',5:'Eage'}
                                        u=D[f]
                                        print('Set New',u,':')
                                        if f==1:
                                         g=input()
                                         query.execute("Update empl set Ename='{}' where Ename='{}'".format(g,n))
                                        if f==2:
                                         g=int(input())
                                         query.execute("Update empl set Eid={} where Ename='{}'".format(g,n))
                                        if f==3:
                                         g=int(input())
                                         query.execute("Update empl set Esal={} where Ename='{}'".format(g,n))
                                        if f==4:
                                         g=input()
                                         query.execute("Update empl set EJob='{}' where Ename='{}'".format(g,n))
                                        if f==5:
                                         g=int(input())
                                         query.execute("Update empl set Eage={} where Ename='{}'".format(g,n))
                                        cursor.commit()
                                        print('........UPDATE SUCCESSFUL..........')
                                    except:
                                      print('YOU HAVE ENTERED A STRING....REEDIRECTING AGAIN')
                                      print(".................................................................")
                            if a==0:
                              print('The employee does not exists')
                              print(".................................................................")
                        if e=='5':
                            try:
                                z=input('Enter the Employee Name for deleting:')
                                query=cursor.cursor()
                                query.execute('select * from empl')
                                y=query.fetchall()
                                a=0
                                for l in range(len(y)):
                                    if y[l][0]==z or y[l][0]==z.upper() or (y[l][0]).upper()==z:
                                        a=+1
                                        query.execute("delete from empl where Ename='{}'".format(z))
                                        print('...........DELETED SUCCESSFULLY...........')
                                        cursor.commit()
                                if a==0:
                                    print('The employee does not exists')
                                       
                            except:
                                print('''................EMPLOYEE DID NOT EXISTS.......
............................................''')
                        if e=='7':
                            print('.........SUCCESSFULLY ADMIN LOGOUT............')
                            break
                        if e=='0':
                            menu()
                        if e=='6':
                            cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                            query=cursor.cursor()
                            query.execute("select * from Customers")
                            a=query.fetchall()
                            #print(a)
                            if len(a)==0:
                                print("No Customers Yet")
                                print(".................................................................")
                            else:
                                #Fullname varchar(30),customerid int(5),Phone varchar(10),Email varchar(30),Gender varchar(10),branch varchar(10),cateogry varchar(10)
                                 print(":CUSTOMER NAME    :    _ID_   :   PHONE    :  EMAIL                        :  GENDER  : BRANCH         : CATEOGRY ")
                                 for r in a:
                                  print(':',(r[0]),' '*(14-len(r[0])),':','  ',r[1],' :',r[2],':',r[3],' '*(28-len(r[3])),':',r[4],' '*(7-len(r[4])),':',r[5],' '*(14-len(r[5])),":",r[6],':')
                        elif int(e) not in[0,1,2,3,4,5,6,7]:
                            print('''WRONG INPUT...../!!!
REDIRECTING AGAIN.........:)..
..........................................''')
            else:
                print('''MAKE SURE YOU KNOW YOU YOUR PASSWD......
    Quiting to main menu....:)
    .........................................''')
        if int(q)==2:
                print("......HP Gas agency welcomes you.....")
                while True:
                    print("MENU")
                    print('''1:BOOK YOUR GAS CYLIDER
2:CANCEL YOUR ORDER
3:COMPLAIN FOURUM
4:TRACK YOUR ORDER
5:UPDATE YOUR ORDER
6:REGISTER YOURSELF
7:EXIT
...............................''')
                    s=int(input("choose now"))
                    #try:
                    if s==1:
                                from tkinter import *
                                from tkinter.ttk import *
                                root=Tk()
##                                    style = Style()
##                                    style.theme_use('alt')
##                                    root.configure(background='#AEB6BF')
                                from tkinter import messagebox
                                from tkinter.ttk import *
                                import mysql.connector as ms
                                cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                query=cursor.cursor()
                                #query.execute("drop table if exists gas_agency")
                                #query.execute("create table gas_agency(Account_number char(5) NOT NULL primary key ,Weight int NOT NULL,Phone_No char(10) NOT NULL,EMAILID varchar(30) NOT NULL check (EMAILID like '%@gmail.com'),Date_Of_Booking date NOT NULL,Mode_Of_Payment varchar(20),deliverydate varchar(20))")
                                root.geometry("900x970")
                                photo=PhotoImage(file=r'u.png')
                                labelphoto=Label(root,image=photo)
                                labelphoto.place(x=640,y=190)
                                photo1=PhotoImage(file=r'uu.png')
                                labelphoto1=Label(root,image=photo1,relief=FLAT)
                                #labelphoto1.place(x=680,y=0)
                                ##photo2=PhotoImage(file=r'u.png')
                                ##labelphoto2=Label(root,image=photo2)
                                ##labelphoto2.place(x=9,y=4)
                                root.title(" HP Gas Booking")
                                Label(root,text="Welcome to HP Gas Agency",font="comicsansms 23 bold").place(x=180,y=40)
                                ac=Label(root,text="Account number:(5 digits)",font="comicsansms 13 bold").place(x=120,y=150)
                                weight=Label(root,text="Gas cylinder weight",font="comicsansms 13 bold").place(x=120,y=200)
                                phone=Label(root,text="Enter your phone number:",font="comicsansms 13 bold").place(x=120,y=250)
                                email=Label(root,text="Enter your email id:",font="comicsansms 13 bold").place(x=120,y=300)
                                date=Label(root,text='''Enter the date of booking:

(YYYY-MM-DD)''',font="comicsansms 13 bold").place(x=120,y=350)
                                mode=Label(root,text="Payment Mode",font="comicsansms 13 bold").place(x=120,y=480)
                                acvalue=StringVar()
                                phonevalue=StringVar()
                                emailvalue=StringVar()
                                datevalue=StringVar()
                                mode=IntVar()
                                weigh=IntVar()
                                acentry=Entry(root,textvariable=acvalue)
                                phoneentry=Entry(root,textvariable=phonevalue)
                                emailentry=Entry(root,textvariable=emailvalue)
                                dateentry=Entry(root,textvariable=datevalue)
                                acentry.place(x=400,y=150)
                                emailentry.place(x=400,y=300)
                                w1=Radiobutton(root,variable=weigh,value=0,text="10 kgs").place(x=400,y=200)
                                w2=Radiobutton(root,variable=weigh,value=1,text="15 kgs").place(x=480,y=200)
                                w3=Radiobutton(root,variable=weigh,value=2,text="20 kgs").place(x=560,y=200)
                                r1=Radiobutton(root,variable=mode,value=0,text="cash on delivery").place(x=120,y=510)
                                r1=Radiobutton(root,variable=mode,value=1,text="online payment").place(x=120,y=530)
                                phoneentry.place(x=400,y=250)
                                dateentry.place(x=400,y=350)
                                option1=IntVar()
                                optionvalue=Checkbutton(root,text="Want to confirm your booking....",variable=option1)
                                optionvalue.place(x=120,y=450)
                                query.execute("select curdate()")
                                hm=query.fetchone()
                                datevalue.set(str(hm[0]))
                                emailvalue.set("@gmail.com")
                                
                                def show():
                                   if option1.get()==1:
                                        answer=messagebox.askyesnocancel("Book","Do you want to CONFIRM your booking?")
                                        if answer==True:
                                            cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                            query=cursor.cursor()
                                            a=acvalue.get()
                                            b=weigh.get()
                                            m=emailvalue.get()
                                            w={0:10,1:20,2:30}
                                            z={0:"cash on delivery",1:"online payment"}
                                            c=datevalue.get()
                                            d=mode.get()
                                            o=str(z[d])
                                            e=int(w[b])
                                            p=phonevalue.get()
                                            query.execute("select curdate()")
                                            hm=query.fetchone()
                                            pop=datetime.timedelta(10)
                                            query.execute("select curtime()")
                                            tm=query.fetchone()
                                            lerry=cursor.cursor()
                                            lerry.execute("select * from Customers")
                                            fr=lerry.fetchall()
                                            regis=False
                                            name=0
                                            notr=1
                                            datevalue.set(str(hm[0]))
                                            for i in range(len(fr)):
                                                if str(fr[i][1])==a:
                                                    regis=True
                                                    name=i
                                                if str(fr[i][2])==(p) and fr[i][3]==m:
                                                    notr=0
                                            try:
                                                if regis==True:
                                                  if notr==0:
                                                     if len(a)==5 and len(p)==10 and m[::-1][:10:]=='moc.liamg@' and c==str(hm[0]) and d==0:
                                                        ter=pop+hm[0]
                                                        query.execute("insert into gas_agency values('%s',%s,'%s','%s','%s','%s','%s','%s')"%(a,e,p,m,c,o,ter,"NULL"))
                                                        cursor.commit()
                                                        print("CONGRATULATIONS! Booking Confirmed")
                                                        print("Cylinder booking date:",hm[0])
                                                        print("Tracking id mailed to your registered email id")
                                                        print("Booking time",tm[0])
                                                        print('............................................')
                                                        print('Booking Receipt')
                                                        print('Gas Cylinder Booked By:',fr[name][0])
                                                        print('Account Number:',int(a))
                                                        print('Weight of cylinder booked:',e,'kg')
                                                        print('payment mode:',o)
                                                        
                                                        print('Cylinder will be delivered by date:',pop+hm[0])
                                                        print('............................................')
                                                        print("THANKS FOR BOOKING YOUR GAS CYLINDER......:)")
                                                        root.destroy()
                                                     if len(a)==5 and len(p)==10 and m[::-1][:10:]=='moc.liamg@' and c==str(hm[0]) and d==1:
                                                        root.destroy()
                                                        #from tkinter.ttk import *
                                                        rooty=Tk()
                                                        global photos,photos2,photos3
                                                        global labelphotos
                                                        photos=PhotoImage(file=r'py.png')
                                                        labelphotos=Label(rooty,image=photos)
                                                        labelphotos.place(x=300,y=260)
                                                        photos2=PhotoImage(file=r'o.png')
                                                        labelphotos2=Label(rooty,image=photos2)
                                                        labelphotos2.place(x=100,y=260)
                                                        photos3=PhotoImage(file=r'p.png')
                                                        labelphotos3=Label(rooty,image=photos3)
                                                        labelphotos3.place(x=400,y=90)
                                                        rooty.geometry('600x500')
                                                        rooty.title(' ONLINE PAYMENT')
                                                        Label(rooty,text='CREDIT CARD PAYMENT',font='comicsansms 23 bold').place(x=90,y=53)
                                                        aj=Label(rooty,text='Credit card no:').place(x=80,y=130)
                                                        dj=Label(rooty,text='Expiry Date: (YYYY-MM)').place(x=68,y=180)
                                                        cj=Label(rooty,text='Enter CVV').place(x=70,y=230)
                                                        qj=StringVar()
                                                        wj=StringVar()
                                                        ej=StringVar()
                                                        rj=Entry(rooty,textvariable=qj)
                                                        lop=StringVar()
                                                        hop=StringVar()
                                                        hop.set("SELECT")
                                                        lop.set("SElECT")
                                                        list1 = [2020,2021,2022,2023,2024,2025]
                                                        list2=[1,2,3,4,5,6,7,8,9,10,11,12]
                                                        rj=Entry(rooty,textvariable=qj)
                                                        tj=OptionMenu(rooty,lop,*list1).place(x=240,y=180)
                                                        tj2=OptionMenu(rooty,hop,*list2).place(x=320,y=180)
                                                        yj=Entry(rooty,textvariable=ej)
                                                        rj.place(x=240,y=130)
                                                        progress = Progressbar(rooty, orient = HORIZONTAL, length = 600, mode = 'determinate') 
                                                        yj.place(x=235,y=230)
                                                        progress.place(x=0,y=480)
                                                        sas=StringVar()

                                                        sas.set("ready for online transaction")
                                                        has=Label(rooty,textvariable=sas,relief=SUNKEN,anchor="w")
                                                        has.place(x=0,y=460)
                                                        def showy():
                                                         sas.set("Connecting for online transaction")
                                                         import time 
                                                         progress['value'] = 10
                                                         rooty.update_idletasks() 
                                                         time.sleep(4) 
                                                         progress['value'] = 20
                                                         rooty.update_idletasks() 
                                                         time.sleep(1)
                                                         progress['value'] = 35
                                                         rooty.update_idletasks() 
                                                         time.sleep(1) 
                                                         progress['value'] = 50
                                                         rooty.update_idletasks() 
                                                         time.sleep(1)
                                                         mas=StringVar()
                                                         progress['value'] = 60
                                                         rooty.update_idletasks() 
                                                         time.sleep(1) 
                                                         progress['value'] = 80
                                                         rooty.update_idletasks() 
                                                         time.sleep(1) 
                                                         progress['value'] = 100
                                                         mas.set("Connected")
                                                         gas=Label(rooty,textvariable=mas,relief=SUNKEN,anchor="w")
                                                         gas.place(x=500,y=440)
                                                         has.update()
                                                         time.sleep(2)
                                                         sas.set("processing you transaction.............")
                                                         progress['value'] = 10
                                                         rooty.update_idletasks() 
                                                         time.sleep(4) 
                                                         progress['value'] = 20
                                                         rooty.update_idletasks() 
                                                         time.sleep(1) 
                                                         progress['value'] = 50
                                                         rooty.update_idletasks() 
                                                         time.sleep(1) 
                                                         progress['value'] = 60
                                                         rooty.update_idletasks() 
                                                         time.sleep(1) 
                                                         progress['value'] = 80
                                                         rooty.update_idletasks() 
                                                         time.sleep(1) 
                                                         progress['value'] = 100
                                                         time.sleep(6)
                                                         has.update()
                                                         sas.set("transaction failed")
                                                         allo=qj.get()



                                                         try:
                                                             if  allo.isdigit()==True  and len(allo)==16 and (ej.get()).isdigit()==True and len(ej.get())==3:
                                                                ter=pop+hm[0]
                                                                query.execute("insert into gas_agency values('%s',%s,'%s','%s','%s','%s','%s','%s')"%(a,e,p,m,c,o,ter,"NULL"))
                                                                cursor.commit()
                                                                print("CONGRATULATIONS! Booking Confirmed")
                                                                print("Cylinder booking date:",hm[0])
                                                                print("Tracking id mailed to your registered email id")
                                                                print('............................................')
                                                                print('Gas Cylinder Booked By:',fr[name][0])
                                                                print("Booking time",tm[0])
                                                                print('Booking Receipt')
                                                                print('Account Number:',int(a))
                                                                print('Weight of cylinder booked:',e,' kg')
                                                                print('payment mode:',o)
                                                                #k=str(hj[0])
                                                                print('Cylinder will be delivered by date:',hm[0]+pop)
                                                                print('............................................')
                                                                print("THANKS FOR BOOKING YOUR GAS CYLINDER......:)")
                                                                rooty.destroy()
                                                            
                                                             else:
                                                                 k=messagebox.askretrycancel("Booking FAILED!","Card number or CVV not valid")
                                                                 if k==False:
                                                                   rooty.destroy()
                                                         except:
                                                              k=messagebox.askretrycancel("Booking FAILED!","Booking has already been placed through this Id.")
                                                        Button(rooty,text='PAY NOW...',cursor="hand2",command=showy).place(x=300,y=450)
                                                     elif len(a)!=5 or len(p)!=10 or m[::-1][:10:]!='moc.liamg@' or c!=str(hm[0]):
                                                      k=messagebox.askretrycancel("Booking FAILED!","Please fill the form correctly")
                                                  else:
                                                      x=messagebox.showerror("INCOMPATIBLE SEARCH","ENTERED EMAIL OR PHONE NO. DOES NOT MATCH WITH THE REGISTERED PHONE NUMBER")
                                                else:
                                                    e=messagebox.showerror("SORRY","YOUR ID IS NOT REGISTERED WITH US")
                                         
                                            except:
                                                  k=messagebox.askretrycancel("Booking FAILED!","Booking has already been placed through this Id.")

                                        if answer==False:
                                            root.destroy()
                                            print("BOOKING WAS FAILED ... SORRY FOR INCONVIENIENCE ... YOU CAN REGISTER YOUR COMPLAIN...")

                                am=Button(root,image=photo1,cursor="hand2",command=show).place(x=360,y=410)
                                root.mainloop()
                    if s==2:
                        print("ENTER YOUR ID.....")
                        ID=input()
                        query=cursor.cursor()
                        query.execute('select * from gas_agency')
                        y=query.fetchall()
                        a=0
                        for l in range(len(y)):
                            if y[l][0]==ID:
                                a=+1
                                query.execute("delete from gas_agency where Account_number='{}'".format(ID))
                                print('...........BOOKING CANCELLED...........')
                                print('....Sorry for inconvinience.....Send your feedback.........')
                                cursor.commit()
                        if a==0:
                                    print('The order has not been placed through this number')
                    if s==6:
                        from tkinter import *
                        from tkinter import messagebox
                        import mysql.connector as ms
                        rooto = Tk()
                        rooto.geometry('500x900')
                        rooto.title("Registration Form")
                        global labelphotos69
                        photos69=PhotoImage(file=r'yi.png')
                        labelphotos69=Label(rooto,image=photos69)
                        labelphotos69.place(x=0,y=5)


                        Fullname=StringVar()
                        Email=StringVar()
                        var = IntVar()
                        c=StringVar()
                        var1= IntVar()
                        var2=StringVar()
                        vam=StringVar()
                        Email.set("@gmail.com")
                        def otpj():
                           import random
                           global otpg
                           otpg=random.randint(11111,99999)
                           z=messagebox.askyesno("OTP GENERATED",["YOUR OTP GENERATED IS",otpg,"CLICK YES TO CONFIRM"])
                           return otpg
                        def done():
                            if vam.get()==str(otpg):
                                     import mysql.connector as ms
                                     cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                     query=cursor.cursor()
                                     query.execute("INSERT INTO Customers values('%s',%s,'%s','%s','%s','%s','%s')"%(name1,new,phone,email,gender1[gender],branch1,cateogry1[cateogry]))
                                     cursor.commit()
                                     fd=messagebox.showinfo("Successful","REGISTRATION CONFIRMED")
                                     print("....REGISTERED DETAILS....")
                                     print("NAME :",name1)
                                     print("EMAIL :",email)
                                     print("GENDER :",gender1[gender])
                                     print("PHONE :",phone)
                                     print("BRANCH ASSOCIATED :",branch1)
                                     print("CATEOGRY :",cateogry1[cateogry])
                                     print("USER ID GENERATED FOR YOU........",new)
                                     rooto.destroy()
                            else:
                                    aq=messagebox.showerror("ERROR","OTP ENTERED WAS WRONG")
                                    rooto.destroy()
                                    print("YOUR REGISTRATION WAS UNSUCCESSFUL")
                        def database():
                           global name1,email,gender,branch1,new,phone,cateogry,cateogry1,gender1
                           name1=Fullname.get()
                           email=Email.get()
                           gender=var.get()
                           branch1=c.get()
                           cateogry=var1.get()
                           phone=var2.get()
                           gender1={0:"Male",1:"Female"}
                           cateogry1={0:"BPL",1:"UPL"}
                           import mysql.connector as ms
                           cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                           query=cursor.cursor()
                           query.execute("select * from Customers")
                           fr=query.fetchall()
                           new=11110+len(fr)
                           m=messagebox.askyesnocancel("CONFIRMATION INFORMATION","CLICK YES TO CONTINUE")
                           if m==True:
                              if name1.isalpha()==True and email[::-1][:10:]=='moc.liamg@' and phone.isdigit()==True and len(phone)==10 and branch1!='select your branch':
                                 otpj()
                                 entry6=Entry(rooto,textvariable=vam,width=7,font='comicsansms 19 bold').place(x=290,y=540)
                                 label_6=Label(rooto,text="Enter your OTP",width=20,font='comicsansms 13 bold').place(x=70,y=540)
                                 Button(rooto, text='Submit',width=20,bg='brown',fg='white',command=done).place(x=180,y=640)                                    
                              else: 
                                 k=messagebox.askretrycancel("REGISTRATION FAILED!","INPUT GIVEN ARE NOT VALID")
                                 if k==False:
                                    rooto.destroy()
                                    print("YOUR REGISTRATION WAS CANCELLED BY YOU")

                                     
                        label_0 = Label(rooto, text="Registration form",width=20,font='comicsansms 23 bold')
                        label_0.place(x=90,y=140)


                        label_1 = Label(rooto, text="Name",width=20,font='comicsansms 13 bold')
                        label_1.place(x=80,y=220)

                        entry_1 = Entry(rooto,textvar=Fullname)
                        entry_1.place(x=270,y=220)
                        label_5 = Label(rooto, text="Phone Number",width=20,font='comicsansms 13 bold')
                        label_5.place(x=80,y=280)

                        entry_5 = Entry(rooto,textvar=var2)
                        entry_5.place(x=270,y=280)
                        label_2 = Label(rooto, text="Email",width=20,font='comicsansms 13 bold')
                        label_2.place(x=68,y=330)

                        entry_2 = Entry(rooto,textvar=Email)
                        entry_2.place(x=270,y=330)

                        label_3 = Label(rooto, text="Gender",width=20,font='comicsansms 13 bold')
                        label_3.place(x=70,y=390)

                        Radiobutton(rooto, text="Male",padx = 5, variable=var, value=0,font='comicsansms 13').place(x=250,y=390)
                                                                                                                    
                        Radiobutton(rooto, text="Female",padx = 20, variable=var, value=1,font='comicsansms 13').place(x=320,y=390)

                        label_4 = Label(rooto, text="local address",width=20,font='comicsansms 13 bold')
                        label_4.place(x=70,y=440)

                        list1 = ['gorakhnath','bilandpur','daudpur','rustumpur','golghar','university','shahpur','medical_road', 'bargadwa'];

                        droplist=OptionMenu(rooto,c, *list1)
                        droplist.config(width=15,font='comicsansms 13')
                        c.set('Select your branch') 
                        droplist.place(x=250,y=440)

                        label_4 = Label(rooto, text="Cateogry",width=20,font='comicsansms 13 bold')
                        label_4.place(x=70,y=500)
                        Radiobutton(rooto, text="BPL", variable=var1,value=0,font='comicsansms 13').place(x=270,y=500)
                        Radiobutton(rooto, text="UPL", variable=var1,value=1,font='comicsansms 13').place(x=330,y=500)
                        Button(rooto, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=640)

                        rooto.mainloop()

                    if s==3:
                        from tkinter import *
                        from tkinter.ttk import *
                        roota=Tk()
                        from tkinter import messagebox

                        roota.geometry('600x285')
                        roota.title('Complaint Management')
                        roota.configure(background='#AEB6BF')
                        import mysql.connector as ms
                        #Style
                        style = Style()
                        style.theme_use('classic')
                        for elem in ['TLabel', 'TButton', 'TRadioutton']:
                                style.configure(
                                        elem, background='#AEB6BF')
                        #Gridx1353
                        labels = ['Full Name:','customer Id', 'Gender:', 'Comment:']
                        for i in range(4):
                                Label(roota, text=labels[i],font=('Arial', 14,'bold')).grid(row=i, column=0, padx=10, pady=10)

                        BuList = Button(roota, text='EXIT',command=roota.destroy)
                        BuList.grid(row=4, column=1)
                        def submit():
                            f=open(r'complain.txt',"a")
                            L=[Idval.get(),ful.get(),SpanGender.get(),coment.get(),'\n']
                            cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                            lerry=cursor.cursor()
                            lerry.execute("select * from Customers")
                            fk=lerry.fetchall()
                            regisa=False
                            for i in range(len(fk)):
                             if str(fk[i][1])==(Idval.get()):
                                regisa=True
                                name=i
                            if regisa==True:
                                if len(Idval.get())==5 and (ful.get()).isalpha()==True and (Idval.get()).isdigit()==True:
                                 
                                 f.writelines(L)
                                 f.flush()
                                 messagebox.askyesnocancel("COMPLAIN REGISTRATION","Do you want to REGISTER your complain?")
                                 roota.destroy()
                                 print("YOUR COMPLAIN HAS BEEN REGISTERED WITH US..WE WILL WORK ON IT....")
                                 print("SORRY FOR INCONVIENENCE Mr.",ful.get())
                                 print("YOUR REQUEST WILL SOON REACH OUR STAFF")
                                 print("THANK YOU")
                                else:
                                   messagebox.askretrycancel("ERROR","INPUT NOT GIVEN CORRECTLY....REDIECTING AGAIN")
                            else:
                                messagebox.showerror("NOT REGISTERED","SORRY YOU CAN NOT REGISTER YOUR COMPLAIN...YOU ARE NOT REGISTERED WITH US")
                        BuSubmit = Button(roota, text='Submit Now',command=submit)
                        BuSubmit.grid(row=4, column=2)
                        #Entries
                        Idval=StringVar()
                        ful=StringVar()
                        Id=Entry(roota,width=40, font=('Arial', 14,'bold'),textvariable=Idval)
                        Id.grid(row=1, column=1, columnspan=2)
                        fullname = Entry(roota, width=40, font=('Arial', 14),textvariable=ful)
                        fullname.grid(row=0, column=1, columnspan=2)
                        SpanGender = StringVar()
                        Radiobutton(roota, text='Male', value='male', variable=SpanGender).grid(row=2, column=1)
                        Radiobutton(roota, text='Female', value='female', variable=SpanGender).grid(row=2, column=2)
                        coment=StringVar()
                        comment = Entry(roota, width=35, font=('Arial', 14),textvariable=coment)
                        comment.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
                        roota.mainloop()

 
                    if s==4:
                        Id=input("Enter your id to track your order.......")
                        query=cursor.cursor()
                        query.execute('select * from gas_agency')
                        y=query.fetchall()
                        a=0
                        for l in range(len(y)):
                            if y[l][0]==Id:
                                a=+1
                                query.execute("select Date_Of_Booking,deliverydate,weight,Mode_Of_Payment,deliveryboy from gas_agency where Account_number='{}'".format(Id))
                                Date=query.fetchall()
                                print("Tracking details")
                                print("................")
                                print('DATE OF BOOKING :',Date[0][0])
                                print('DELIVERED BY DATE :',Date[0][1])
                                print('WEIGHT OF CYLINDER BOOKED :',Date[0][2],'kg')
                                print('Mode_Of_Payment :',Date[0][3])
                                print('DELIVERED BY :',Date[0][4])
                                print("................")
                                cursor.commit()
                        if a==0:
                                    print('The order has not been placed through this number')
                    if s==5:
                        n=input("ENTER YOUR BOOKING ID.:")
                        query=cursor.cursor()
                        query.execute('select * from gas_agency')
                        y=query.fetchall()
                        a=0
                        for l in range(len(y)):
                            if y[l][0]==n:
                                a=+1
                                print('''1:EMAIL ID
2:PHONE NUMBER REGISTERED
3:WEIGHT OF GAS CYLINDER''')
                                f=int(input('What do you want to update:(choose):'))
                                D={1:'Email to which order details had been sent',2:'Phone number registered',3:'weight of cylinder booked'}
                                u=D[f]
                                print('Set New',u,':')
                                if f==1:
                                 g=input()
                                 if g[::-1][:10:]=='moc.liamg@':
                                  query.execute("Update gas_agency set EMAILID='{}' where Account_number='{}'".format(g,n))
                                  print(".......UPDATION SUCCESSFULL.........")
                                  print(".......YOUR ORDER DETAILS WILL BE SENT TO YOUR NEW EMAIL ID.............")
                                 else:
                                     print(".......INPUT ERROR........!!!!!!!!")
                                if f==2:
                                 g=input()
                                 if len(g)==10:
                                  query.execute("Update gas_agency set Phone_No='{}' where Account_number='{}'".format(g,n))
                                  print(".......UPDATION SUCCESSFULL.........")
                                  print(".......YOUR ORDER DETAILS WILL BE SENT TO YOUR NEW PHONE NUMBER.............")
                                 else:
                                      print("....... ERROR.....PLEASE ENTER 10 DIGIT NUMBER........!!!!!!!!")
                                if f==3:
                                 g=input()
                                 if g in ['10','15','20']:
                                  query.execute("Update gas_agency set weight='{}' where Account_number='{}'".format(g,n))
                                  print(".......UPDATION SUCCESSFULL.........")
                                  print(".......YOUR ORDER DETAILS WILL BE SENT TO YOUR PHONE NUMBER.............")
                                 else:
                                      print("....ERROR.....PLEASE SELECT CORRECT WEIGHT........!!!!!!!!")
                                elif f not in [1,2,3]:
                                      print(".......INPUT ERROR...^&*.....!!!!!!!!")
                        if a==0:
                            print("......NO ORDER HAS BEEN PLACED THROUGH THIS ID.......")
                    if s==7:
                        break

                #except:
                        #
                        #print(".......INPUT ERROR.....&...!!!!!!!!")
        if int(q)==3:
         a=input('Enter Staff Password:')
         if a=='123shreyansh':
            print('.......SUCCESSFULLY LOGINED.......')
            print('Menu:')
            print('1:View order details')
            print('2:View Delivery_Boy details')
            print('3:View Customer details')
            print('4:Add new Delivery_Boy detail')
            print('5:Update Delivery_Boy detail')
            print('6:Delete Delivery_Boy record')
            print('7:Assign delivery_boy to the orders')
            print('8:Exit to main menu')
            while True:
                print('Press 0 to see the menu..........')
                print(".................................................................")
                e=input("choose now.....")
                if e.isalpha():
                    print('You have input a string....$ERROR$....')
                    print(".................................................................")
                if e.isdigit():
                    if int(e)==1:
                        query=cursor.cursor()
                        query.execute("select * from gas_agency")
                        a=query.fetchall()
                        if len(a)==0:
                            print("No booking Yet")
                            print(".................................................................")
                        else:
                            print(": acc no. : weight : phone      : email                         : date       : mode                : delivery date      : delivery boy ")
                            for r in a:
                                 print(':',(r[0]),' '*(6-len(r[0])),':','  ',r[1],' :',r[2],':',r[3],' '*(28-len(r[3])),':',r[4],':',r[5],' '*(20-len(r[5])),":",r[6],':','   ',':',r[7]) 
                    if int(e)==2:
                        import mysql.connector as ms
                        cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                        query=cursor.cursor()
                        query.execute("select * from delivery")
                        a=query.fetchall()
                        #print(a)
                        if len(a)==0:
                            print("No Delivery_boys Yet")
                            print(".................................................................")
                        else:
                            print(": NAME OF BOY            _ID_      phone       type                gender    branch              delivery charge        status ")
                            for r in a:
                             print(':',(r[0]),' '*(14-len(r[0])),':','  ',r[1],' :',r[2],':',r[3],' '*(18-len(r[3])),':',r[4],' '*(7-len(r[4])),':',r[5],' '*(20-len(r[5])),":",r[6],':',' '*(8-len(r[6])),"    ",r[7])
                    if int(e)==4:
                        from tkinter import *
                        from tkinter import messagebox
                        import mysql.connector as ms
                        rooto = Tk()
                        rooto.geometry('5000x6000')
                        rooto.title("Add Delivery_boys")
                        #Style
                        style = Style()
                        style.theme_use('classic')
                        global labelphotos6
                        photos6=PhotoImage(file=r'lp.png')
                        labelphotos6=Label(rooto,image=photos6)
                        labelphotos6.place(x=350,y=26)

                        Fullname=StringVar()
                        Email=IntVar()
                        var = IntVar()
                        c=StringVar()
                        var1= IntVar()
                        var2=StringVar()


                        def database():
                           name1=Fullname.get()
                           email=Email.get()
                           gender=var.get()
                           branch1=c.get()
                           cateogry=var1.get()
                           phone=var2.get()
                           gender1={0:"Male",1:"Female"}
                           cateogry1={0:"10 rupees",1:"50 rupees"}
                           email1={0:"FULL_TIME",1:"PART_TIME"}
                           import mysql.connector as ms
                           cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                           query=cursor.cursor()
                           query.execute("select * from delivery")
                           fr=query.fetchall()
                           new=34570+len(fr)
                           m=messagebox.askyesnocancel("CONFIRMATION INFORMATION","CLICK YES TO CONTINUE")
                           if m==True:
                              if name1.isalpha()==True and phone.isdigit()==True and len(phone)==10 and branch1!='delivery branch':
                                 import mysql.connector as ms
                                 cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                 query=cursor.cursor()
                                 query.execute("INSERT INTO delivery values('%s',%s,'%s','%s','%s','%s','%s','%s')"%(name1,new,phone,email1[email],gender1[gender],branch1,cateogry1[cateogry],"Free"))
                                 cursor.commit()
                                 fd=messagebox.showinfo("Successful","ADDITION CONFIRMED")
                                 print("....ADDED DETAILS....")
                                 print("NAME :",name1)
                                 print("TYPE :",email1[email])
                                 print("GENDER :",gender1[gender])
                                 print("PHONE :",phone)
                                 print("BRANCH ASSOCIATED :",branch1)
                                 print("AMOUNT GIVEN :",cateogry1[cateogry])
                                 print("STATUS :","FREE")
                                 print("USER ID GENERATED FOR DELIVERY_BOY........",new)
                                 rooto.destroy()
                              else: #name1.isalpha()==False and email[::-1][:10:]!='moc.liamg@' and phone.isdigit()==False and len(phone)!=10 and branch1=='select your branch':
                                 k=messagebox.askretrycancel("ADDITION FAILED!","INPUT GIVEN ARE NOT VALID")
                                 if k==False:
                                    rooto.destroy()
                                    print("ADDITION WAS CANCELLED")
                           
                                     
                        label_0 = Label(rooto, text="DELIVERY_BOY INFORMATION",width=29,font='comicsansms 23 bold')
                        label_0.place(x=90,y=53)


                        label_1 = Label(rooto, text="FullName",width=20,font='comicsansms 13 bold')
                        label_1.place(x=80,y=130)

                        entry_1 = Entry(rooto,textvar=Fullname)
                        entry_1.place(x=270,y=130)
                        label_5 = Label(rooto, text="Phone Number",width=20,font='comicsansms 13 bold')
                        label_5.place(x=80,y=180)

                        entry_5 = Entry(rooto,textvar=var2)
                        entry_5.place(x=270,y=180)
                        label_2 = Label(rooto, text="TYPE",width=20,font='comicsansms 13 bold')
                        label_2.place(x=68,y=230)

                        #entry_2 = Entry(rooto,textvar=Email)
                        #entry_2.place(x=270,y=230)

                        label_3 = Label(rooto, text="Gender",width=20,font='comicsansms 13 bold')
                        label_3.place(x=70,y=280)

                        Radiobutton(rooto, text="Male",padx = 5, variable=var, value=0,font='comicsansms 13').place(x=250,y=280)
                        Radiobutton(rooto, text="Female",padx = 20, variable=var, value=1,font='comicsansms 13').place(x=320,y=280)
                        Radiobutton(rooto, text="Full time",padx = 5, variable=Email, value=0,font='comicsansms 13').place(x=270,y=230)
                        Radiobutton(rooto, text="Part time",padx = 20, variable=Email, value=1,font='comicsansms 13').place(x=360,y=230)
                        label_4 = Label(rooto, text="Delivery area",width=20,font='comicsansms 13 bold')
                        label_4.place(x=70,y=330)

                        list1 = ['gorakhnath','bilandpur','daudpur','rustumpur','golghar','university','shahpur','medical_road', 'bargadwa'];

                        droplist=OptionMenu(rooto,c, *list1)
                        droplist.config(width=15,font='comicsansms 13')
                        c.set('delivery branch') 
                        droplist.place(x=250,y=320)

                        label_4 = Label(rooto, text="Delivery charges ",width=20,font='comicsansms 13 bold')
                        label_4.place(x=70,y=380)
                        Radiobutton(rooto, text="10 Rs", variable=var1,value=0,font='comicsansms 13').place(x=270,y=380)
                        Radiobutton(rooto, text="50 Rs", variable=var1,value=1,font='comicsansms 13').place(x=360,y=380)

                        Button(rooto, text='Submit',width=20,bg='blue',fg='white',command=database).place(x=180,y=440)

                        rooto.mainloop()
                    if int(e)==5:
                        n=input('Enter Delivery_boy Name....:')
                        query=cursor.cursor()
                        query.execute('select * from delivery')
                        y=query.fetchall()
                        a=0
                        for l in range(len(y)):
                            if y[l][0]==n or y[l][0]==n.upper() or (y[l][0]).upper()==n:
                                a=a+1
                                print('''1:DELIVERY BOY NAME
2:DELIVERY BOY ID
3:DELIVERY BOY PHONE NUMBER
4:DELIVERY BOY TYPE
5:DELIVERY BOY AREA
6:DELIVERY BOY CHARGES''')
                                print(".................................................................")
                                try:
                                    f=int(input('What do you want to update:'))
                                    D={1:'name',2:'id',3:'phone no.',4:'type',5:'delivery area',6:'delivery charges'}
                                    u=D[f]
                                    print('Set New',u,':')
                                    if f==1:
                                     g=input()
                                     query.execute("Update delivery set Fullname='{}' where Fullname='{}'".format(g,n))
                                    if f==2:
                                     g=int(input())
                                     query.execute("Update delivery set id={} where Fullname='{}'".format(g,n))
                                    if f==3:
                                     g=int(input())
                                     query.execute("Update delivery set Phone={} where Fullname='{}'".format(g,n))
                                    if f==4:
                                     g=input()
                                     query.execute("Update delivery set Email='{}' where Fullname='{}'".format(g,n))
                                    if f==5:
                                     g=input()
                                     query.execute("Update delivery set branch='{}' where Fullname='{}'".format(g,n))
                                    if f==6:
                                     g=input()
                                     x=g+" rupees"
                                     query.execute("Update delivery set charges='{}' where Fullname='{}'".format(x,n))
                                    cursor.commit()
                                    print('........UPDATE SUCCESSFUL..........')
                                except:
                                   print('YOU HAVE ENTERED A STRING....REEDIRECTING AGAIN')
                                   print(".................................................................")
                        if a==0:
                          print('The employee does not exists')
                          print(".................................................................")

                    if int(e)==6:
                        try:
                            z=input('Enter the delivery_boy Name for deleting:')
                            query=cursor.cursor()
                            query.execute('select * from delivery')
                            y=query.fetchall()
                            a=0
                            for l in range(len(y)):
                                if y[l][0]==z or y[l][0]==z.upper() or (y[l][0]).upper()==z:
                                    a=a+1
                                    query.execute("delete from delivery where Fullname='{}'".format(z))
                                    print('...........DELETED SUCCESSFULLY...........')
                                    cursor.commit()
                            if a==0:
                                print('The delivery_boy does not exists')
                                   
                        except:
                            print('''................DELIVERY_BOY DID NOT EXISTS.......
............................................''')
                    if int(e)==8:
                        print('.........SUCCESSFULLY STAFF LOGOUT............')
                        break
                    if int(e)==7:
                            import datetime
                            from tkinter.ttk import *
                            from tkinter import *
                            from tkinter import messagebox
                            import mysql.connector as ms
                            cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                            query=cursor.cursor()
                            rootp=Tk()
                            rootp.geometry("1000x1000")
                            rootp.title("DELIVERY BOY ASSIGNMENT")
                            photos691=PhotoImage(file=r'p.png')
                            labelphotos691=Label(rootp,image=photos691)
                            labelphotos691.place(x=820,y=500)
                            a=Label(rootp,text="DELIVER BOY ASSIGNMENT",font="comicsansms 23 bold").place(x=320,y=60)
                            a=Label(rootp,text="ACCOUNT NO.",font="comicsansms 13 bold").place(x=120,y=120)
                            a=Label(rootp,text="WEIGHT",font="comicsansms 13 bold").place(x=120,y=180)
                            a=Label(rootp,text="PHONE NO.",font="comicsansms 13 bold").place(x=120,y=240)
                            a=Label(rootp,text="EMAIL ID",font="comicsansms 13 bold").place(x=120,y=300)
                            a=Label(rootp,text="DATE OF BOOKING",font="comicsansms 13 bold").place(x=120,y=360)
                            a=Label(rootp,text="MODE OF PAYMENT",font="comicsansms 13 bold").place(x=120,y=420)
                            a=Label(rootp,text="DATE OF DELIVERY",font="comicsansms 13 bold").place(x=120,y=480)
                            a=Label(rootp,text="BRANCH ASSOCIATED",font="comicsansms 13 bold").place(x=120,y=540)
                            global b
                            b=StringVar()
                            c=StringVar()
                            d=StringVar()
                            ep=StringVar()
                            f=StringVar()
                            g=StringVar()
                            h=StringVar()
                            i=StringVar()
                            global lop
                            lop=StringVar()
                            JOB=StringVar()
                            e1=Entry(rootp,textvariable=b).place(x=420,y=120)
                            e2=Entry(rootp,textvariable=c).place(x=420,y=180)
                            e3=Entry(rootp,textvariable=d).place(x=420,y=240)
                            e4=Entry(rootp,textvariable=ep).place(x=420,y=300)
                            e5=Entry(rootp,textvariable=f).place(x=420,y=360)
                            e6=Entry(rootp,textvariable=g).place(x=420,y=420)
                            e7=Entry(rootp,textvariable=h).place(x=420,y=480)
                            e7=Entry(rootp,textvariable=i).place(x=420,y=540)
                                #Account_number char(5) NOT NULL primary key ,Weight int NOT NULL,Phone_No char(10) NOT NULL,EMAILID varchar(30) NOT NULL check (EMAILID like '%@gmail.com'),Date_Of_Booking date NOT NULL,Mode_Of_Payment varchar(20),deliverydate varchar(20))")
                            cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                            global queryq
                            queryq=cursor.cursor()
                            queryq.execute("select * from gas_agency where deliveryboy='NULL'")
                            def nextw():
                                m=queryq.fetchone()
                                if m!=None:
                                    bh=int(m[0])
                                    b.set(m[0])
                                    c.set(m[1])
                                    d.set(m[2])
                                    ep.set(m[3])
                                    f.set(m[4])
                                    g.set(m[5])
                                    h.set(m[6])
                                    cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                    query=cursor.cursor()
                                    query.execute(("select branch from Customers where customerid='%s'")%(bh))
                                    l=query.fetchone()
                                    i.set(l[0])
                                else:
                                    messagebox.showinfo("COMPLETED","NO MORE ORDERS TO BE ASSIGNED")
                            def clear():
                                b.set('')
                                c.set('')
                                d.set('')
                                ep.set('')
                                f.set('')
                                g.set('')
                                h.set('')
                                i.set('')
                            def search():
                                if b.get()=='':
                                    messagebox.showerror("error","FILL THE ID TO SEARCH")
                                else:
                                    cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                    query=cursor.cursor()
                                    query.execute(("select * from gas_agency where Account_number='%s'")%(b.get()))
                                    m=query.fetchone()
                                    #print(m)
                                    #b.set(m[0])
                                    if m!=None:
                                        c.set(m[1])
                                        d.set(m[2])
                                        ep.set(m[3])
                                        f.set(m[4])
                                        g.set(m[5])
                                        h.set(m[6])
                                        query.execute(("select branch from Customers where customerid='%s'")%(int(m[0])))
                                        l=query.fetchone()
                                        i.set(l[0])
                                    else:
                                        messagebox.showerror("error","NO BOOKING OF THIS ID")
                            def assign():
                                 cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                 query=cursor.cursor()
                                 query.execute(("select deliveryboy from gas_agency where Account_number='%s'")%((b.get())))
                                 dfrt=query.fetchone()

                                 if dfrt[0]=='NULL' or dfrt[0]=='Null':
                                    if lop.get()!="Select delivery boy":
                                     cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                     query=cursor.cursor()
                                     kow=lop.get().rstrip("',)")
                                     ko=kow.lstrip("('")
                                     li=b.get().rstrip(" ' '''''")
                                     #g=StringVar()
                                     query.execute(("update gas_agency set deliveryboy='%s' where Account_number='%s'")%(ko,(b.get())))
                                     cursor.commit()
                                     query.execute(("update delivery set status='BUSY' where Fullname='%s'")%(ko))
                                     cursor.commit()
                                     lop.set('')
                                     messagebox.showinfo("assign","DELIVERY BOY ASSIGNED")
                                     a=Label(rootp,text="                      ",font="comicsansms 23 bold").place(x=620,y=600)
                                     a=Label(rootp,text="                      ",font="comicsansms 23 bold").place(x=820,y=400)
                                     a=Label(rootp,text="                           ",font="comicsansms 23 bold").place(x=720,y=200)
                                     a=Label(rootp,text="                      ",font="comicsansms 23 bold").place(x=620,y=300)
                                     a=Label(rootp,text="                      ",font="comicsansms 23 bold").place(x=820,y=300)
                                    else:
                                        messagebox.showerror("SELECT","Please select the deliveryboy")
                                 else:
                                     messagebox.showerror("already done","DELIVERY BOY ALREADY ASSIGNED")
                            def searchd():
                                 if b.get()=='' and i.get()=='':
                                    messagebox.showerror("error","FILL THE ID TO SEARCH......ALSO MENTION THE BRANCH ASSOCIATED")
                                 else:
                                    cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                                    query=cursor.cursor()
                                    query.execute(("select deliveryboy from gas_agency where Account_number='%s'")%((b.get())))
                                    dfrt=query.fetchone()
                                    #print(dfrt)
                                    query.execute(("select * from gas_agency where Account_number='%s'")%(b.get()))
                                    m=query.fetchone()
                                    if m!=None:
                                     if dfrt[0]=='NULL' or dfrt[0]=='Null':
                                        query.execute(("select Fullname from delivery where status='FREE' and branch='%s'")%(i.get()))
                                        global me
                                        me=query.fetchall()
                                        list1=list(me)
                                        if len(me)==0:
                                            messagebox.showerror("ERROR","THERE IS NO DELIVERY BOY FREE OR ASSOSIATED WITH THE BARANCH")
                                        else:
                                            global tj
                                            a=Label(rootp,text="DELIVERY BOY",font="comicsansms 23 bold").place(x=720,y=200)
                                            a=Label(rootp,text="DELIVERY BOY",font="comicsansms 13 bold").place(x=620,y=300)
                                            #a=Label(rootp,text="DELIVERY BOY ID",font="comicsansms 13 bold").place(x=620,y=350)
                                            e8=Entry(rootp,textvariable=lop).place(x=820,y=300)
                                           # e8=Entry(rootp,textvariable=JOB).place(x=820,y=350)
                                            lop.set("Select delivery boy")
                                            tj=OptionMenu(rootp,lop,*list1).place(x=820,y=400)
                                            cf=Button(rootp,text="assign",command=assign,font="comicsansms 13 bold").place(x=620,y=600)
                                     else:
                                        messagebox.showinfo("placed","DELIVERY_BOY HAS BEEN ASSIGNED TO THIS ID")
                                    else:
                                        messagebox.showerror("error","NO BOOKING OF THIS ID")
                            qw=Button(rootp,text="search delivery boy",command=searchd,font="comicsansms 13 bold").place(x=420,y=600)        
                            qw=Button(rootp,text="clear",command=clear,font="comicsansms 13 bold").place(x=220,y=600)
                            qw=Button(rootp,text="search",command=search,font="comicsansms 13 bold").place(x=320,y=600)    
                            qw=Button(rootp,text="next",command=nextw,font="comicsansms 13 bold").place(x=120,y=600)


                            rootp.mainloop()
                    if int(e)==0:
                        menua()
                    if int(e)==3:
                        cursor=ms.connect(host="localhost",user="root",passwd="tiger",database="sakila")
                        query=cursor.cursor()
                        query.execute("select * from Customers")
                        a=query.fetchall()
                        #print(a)
                        if len(a)==0:
                            print("No Customers Yet")
                            print(".................................................................")
                        else:
                            #Fullname varchar(30),customerid int(5),Phone varchar(10),Email varchar(30),Gender varchar(10),branch varchar(10),cateogry varchar(10)
                             print(":CUSTOMER NAME    :    _ID_   :   PHONE    :  EMAIL                        :  GENDER  : BRANCH         : CATEOGRY ")
                             for r in a:
                              print(':',(r[0]),' '*(14-len(r[0])),':','  ',r[1],' :',r[2],':',r[3],' '*(28-len(r[3])),':',r[4],' '*(7-len(r[4])),':',r[5],' '*(14-len(r[5])),":",r[6],':')


                    elif int(e) not in[0,1,2,3,4,5,6,7,8]:
                        print('''WRONG INPUT...../!!!
REDIRECTING AGAIN.........:)..
..........................................''')
         else:
            print('''MAKE SURE YOU KNOW YOU YOUR PASSWD......
Quiting to main menu....:)
.........................................''')     

        if int(q)==4:
            print('..................../THANKS FOR CHOOSING OUR GAS AGENCY................./')
            break
        elif int(q) not in [1,2,3,4]:
             print('''WRONG INPUT...../!!!
      REDIRECTING AGAIN.........:)..''')
#except:
# print("QUITING OUT SOME ERROR OCCURRED")


