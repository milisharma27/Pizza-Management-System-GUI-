from tkinter import *
from sqlite3 import *
import tkinter
#from ttk import *
#import tkMessageBox
import random
class Log:
    def home(sf):
        sf.scr=Tk(className="Pizza Management Home")
        sf.scr.geometry("605x400")
        sf.fr=Frame(sf.scr,height=618,width=1366)
        sf.scr.resizable(False, False)
        sf.lab3=Label(sf.fr,text="LOGIN",bg="white",font=("cooper black",20))
        sf.lab3.place(x=160,y=30)
        sf.lab1=Label(sf.fr,text="Username",bg="white",font=("default",20))
        sf.lab1.place(x=30,y=100)
        sf.lab2=Label(sf.fr,text="Password",bg="white",font=("default",20))
        sf.lab2.place(x=30,y=150)
        sf.user=Entry(sf.fr,bg="white",font=("default",20))
        sf.user.place(x=180,y=100)
        sf.pasd=Entry(sf.fr,bg="white",font=("default",20),show="*")
        sf.pasd.place(x=180,y=150)
        sf.fr=Frame(sf.scr,bg="blue",height=618,width=1366)
        sf.c=Canvas(sf.fr,height=618,width=1366)
        sf.c.pack()
        sf.back=PhotoImage(file="pizzaback.png")
        sf.c.create_image(300,200,image=sf.back)
        #sf.c.create_image(683,284,image=sf.back)
        sf.st=Button(sf.fr,text="login",font=("default",20),command=sf.login)
        sf.st.place(x=265,y=100)
        #sf.st.place(x=625,y=220)
        #sf.st.place(x=80,y=220)
        sf.si=Button(sf.fr,text="Register",command=sf.register,font=("default",20))
        sf.si.place(x=245,y=200)
        #sf.si.place(x=600,y=330)
        #sf.si.place(x=200,y=220)
        sf.fr.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def register(sf):
        sf.scr.destroy()
        sf.scr1=Tk(className="Pizza Management Register")
        sf.fr=Frame(sf.scr1,bg="DeepSkyBlue2",height=550,width=650)
        sf.lab3=Label(sf.fr,text="Customer Registration",bg="white",font=("default",20))
        sf.lab3.place(x=250,y=50)

        sf.lb1=Label(sf.fr,text="First Name",bg="#d3ede6",font=("default",20))
        sf.lb1.place(x=80,y=120)
        sf.first=Entry(sf.fr,bg="white",width=15,font=("default",20),bd=5)
        sf.first.place(x=250,y=120)
        sf.lab2=Label(sf.fr,text="Last Name",bg="#d3ede6",font=("default",20))
        sf.lab2.place(x=80,y=170)
        sf.last=Entry(sf.fr,bg="white",width=15,font=("default",20),bd=5)
        sf.last.place(x=250,y=170)
        
        sf.lab1=Label(sf.fr,text="user name",bg="#d3ede6",font=("default",20))
        sf.lab1.place(x=80,y=220)
        sf.lab2=Label(sf.fr,text="password",bg="#d3ede6",font=("default",20))
        sf.lab2.place(x=80,y=270)
        sf.user=Entry(sf.fr,bg="white",font=("default",20),bd=5)
        sf.user.place(x=250,y=220)
        sf.pasd=Entry(sf.fr,bg="white",font=("default",20),bd=5,show="*")
        sf.pasd.place(x=250,y=270)

        sf.lab5=Label(sf.fr,text="Email ID",bg="#d3ede6",font=("default",20))
        sf.lab5.place(x=80,y=320)
        sf.email=Entry(sf.fr,bg="white",width=15,font=("default",20),bd=5)
        sf.email.place(x=250,y=320)
        sf.lab6=Label(sf.fr,text="Mobile No.",bg="#d3ede6",font=("default",20))
        sf.lab6.place(x=80,y=370)
        sf.mob=Entry(sf.fr,bg="white",width=15,font=("default",20),bd=5)
        sf.mob.place(x=250,y=370)
        
        sf.st=Button(sf.fr,text="submit",font=("default",20),command=sf.login)
        sf.st.place(x=200,y=450)
        sf.si=Button(sf.fr,text="clear",command=sf.clear,font=("default",20))
        sf.si.place(x=380,y=450)        
        sf.fr.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def login(sf):
        sf.scr.destroy()
        sf.scr1=Tk(className="Pizza Management Login")
        sf.fr=Frame(sf.scr1,bg="DeepSkyBlue2",height=400,width=600)
        sf.lab3=Label(sf.fr,text="Login",bg="white",font=("default",20))
        sf.lab3.place(x=250,y=50)
        sf.lab1=Label(sf.fr,text="user name",bg="white",font=("default",20))
        sf.lab1.place(x=80,y=120)
        sf.lab2=Label(sf.fr,text="password",bg="white",font=("default",20))
        sf.lab2.place(x=80,y=170)
        sf.user=Entry(sf.fr,bg="white",font=("default",20))
        sf.user.place(x=250,y=120)
        sf.pasd=Entry(sf.fr,bg="white",font=("default",20),show="*")
        sf.pasd.place(x=250,y=170)
        sf.st=Button(sf.fr,text="submit",font=("default",20),command=sf.menu)
        sf.st.place(x=200,y=250)
        sf.si=Button(sf.fr,text="clear",command=sf.clear,font=("default",20))
        sf.si.place(x=380,y=250)
        sf.fr.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()        
    def menu(sf):
            sf.scr1.destroy()
            sf.roo=Tk(className="MENU")
            sf.roo.geometry("1000x1000")
            sf.fra=Frame(sf.roo,bg="DeepSkyBlue2",height=800,width=2000)
            sf.roo.config(bg="DeepSkyBlue2")
            sf.c=Canvas(sf.fra,height=600,width=600)
            sf.c.pack()
            sf.roo.title("MENU")
            sf.v1=IntVar()
            sf.v2=IntVar()
            sf.v3=IntVar()
            sf.v4=IntVar()
            sf.v5=IntVar()
            sf.v6=IntVar()
            sf.labe=Label(sf.fra,text="ITEM",bg="DeepSkyBlue2",font=("cooper black",20))
            sf.labe.place(x=150,y=30)
            sf.labe1=Label(sf.fra,text="PRICE",bg="DeepSkyBlue2",font=("cooper black",20))
            sf.labe1.place(x=350,y=30)
            sf.labe2=Label(sf.fra,text="Veg Pizza",bg="white",font=("default",16))
            sf.labe2.place(x=140,y=85)
            sf.labe3=Label(sf.fra,text="₹250",bg="white",font=("default",16))
            sf.labe3.place(x=365,y=85)
            sf.labe2=Label(sf.fra,text="Deluxe Veggie",bg="white",font=("default",16))
            sf.labe2.place(x=125,y=115)
            sf.labe3=Label(sf.fra,text="₹250",bg="white",font=("default",16))
            sf.labe3.place(x=365,y=115)
            sf.labe2=Label(sf.fra,text="Veg Vaganza",bg="white",font=("default",16))
            sf.labe2.place(x=125,y=145)
            sf.labe3=Label(sf.fra,text="₹250",bg="white",font=("default",16))
            sf.labe3.place(x=365,y=145)
            sf.labe2=Label(sf.fra,text="Pepper Pizza",bg="white",font=("default",16))
            sf.labe2.place(x=125,y=175)
            sf.labe3=Label(sf.fra,text="₹250",bg="white",font=("default",16))
            sf.labe3.place(x=365,y=175)
            sf.labe2=Label(sf.fra,text="Margherita",bg="white",font=("default",16))
            sf.labe2.place(x=135,y=205)
            sf.labe3=Label(sf.fra,text="₹195",bg="white",font=("default",16))
            sf.labe3.place(x=365,y=205)
            sf.labe4=Label(sf.fra,text="Cold Drink",bg="white",font=("default",16))
            sf.labe4.place(x=135,y=235)
            sf.labe5=Label(sf.fra,text="₹40",bg="white",font=("default",16))
            sf.labe5.place(x=365,y=235)
            sf.labe6=Label(sf.fra,text="Place your order here:",bg="DeepSkyBlue2",font=("Cooper black",16))
            sf.labe6.place(x=155,y=280)
            sf.lab7=Label(sf.fra,text="Item",bg="white",font=("default",16))
            sf.lab7.place(x=120,y=315)
            sf.lab8=Label(sf.fra,text="Quantity",bg="white",font=("default",16))
            sf.lab8.place(x=280,y=315)
            sf.lab9=Label(sf.fra,text="Veg Pizza",bg="white",font=("default",16))
            sf.lab9.place(x=90,y=350)
            sf.v1=Entry(sf.fra,bg="white",font=("default",16))
            sf.v1.place(x=230,y=350)
            sf.lab10=Label(sf.fra,text="Deluxe Pizza",bg="white",font=("default",16))
            sf.lab10.place(x=85,y=385)
            sf.v2=Entry(sf.fra,bg="white",font=("default",16))
            sf.v2.place(x=230,y=385)
            sf.lab11=Label(sf.fra,text="Veg Vaganza",bg="white",font=("default",16))
            sf.lab11.place(x=85,y=420)
            sf.v3=Entry(sf.fra,bg="white",font=("default",16))
            sf.v3.place(x=230,y=420)
            sf.lab12=Label(sf.fra,text="Pepper Pizza",bg="white",font=("default",16))
            sf.lab12.place(x=85,y=455)
            sf.v4=Entry(sf.fra,bg="white",font=("default",16))
            sf.v4.place(x=230,y=455)
            sf.lab13=Label(sf.fra,text="Margherita",bg="white",font=("default",16))
            sf.lab13.place(x=90,y=490)
            sf.v5=Entry(sf.fra,bg="white",font=("default",16))
            sf.v5.place(x=230,y=490)
            sf.lab14=Label(sf.fra,text="Cold Drink",bg="white",font=("default",16))
            sf.lab14.place(x=90,y=525)
            sf.v6=Entry(sf.fra,bg="white",font=("default",16))
            sf.v6.place(x=230,y=525)
            sf.to=Button(sf.fra,text="Submit",font=("cooper black",20),bg="DeepSkyBlue3",fg="black",command=sf.order)
            sf.to.place(x=250,y=565)
            sf.to.pack(fill=BOTH,expand=1)
            sf.fra.pack()
            sf.roo.mainloop()
    def order(sf):
        sf.scr2=Tk(className="Place Order")
        sf.scr2.geometry("450x300")
        sf.scr2.resizable(False, False)
        sf.scr2.title("Place Order")
        sf.scr2.config(bg="DeepSkyBlue2")
        sf.fram=Frame(sf.scr2,height=618,width=1366,bg="DeepSkyBlue2")
        #sf.v1.set("0")
        sf.a=sf.v1.get()
        sf.b=sf.v2.get()
        sf.c=sf.v3.get()
        sf.d=sf.v4.get()
        sf.e=sf.v5.get()
        sf.f=sf.v6.get()
        #print(sf.a)
        if len(sf.a)==0:
            sf.a="0"
        #print(sf.a)
        if len(sf.b)==0:
            sf.b="0"
        #print(sf.b)
        if len(sf.c)==0:
            sf.c="0"
        #print(sf.c)
        if len(sf.d)==0:
            sf.d="0"
        #print(sf.d)
        if len(sf.e)==0:
            sf.e="0"
        #print(sf.e)
        if len(sf.f)==0:
            sf.f="0"
        #print(sf.f)
        #print(sf.a)
        sf.sum=int(sf.a)*250+int(sf.b)*250+int(sf.c)*250+int(sf.d)*250+int(sf.e)*195+int(sf.f)*40
        #sf.tot="₹ "+str(int(((sf.a)*250)+((sf.b)*250)+((sf.c)*250)+((sf.d)*250)+((sf.e)*195)+((sf.f)*40)))
        #print(sf.sum)
        sf.labell=Label(sf.fram,text="Total payable amount is ",bg="DeepSkyblue2",font=("default",16))
        sf.labell.place(x=90,y=110)
        #sf.dis=Entry(sf.fram,text="%s" %(sf.tot),bg="white",font=("default",16))
        sf.val=Label(sf.fram,text=sf.sum,bg="white",font=("default",16))
        sf.val.place(x=320,y=110)
        sf.fram.pack()
        sf.scr.mainloop()
##    def sum(sf):
##        sf.a=sf.v1.get()
##        sf.b=sf.v2.get()
##        print(sf.a)
##        print(sf.b)
    def result(sf):
        sf.username=sf.user.get()
        sf.password=sf.pasd.get()
        try:
            sf.scr.destroy()
        except:
            try:
                sf.scr1.destroy()
            except:
                pass
    def clear(sf):
        sf.user.delete(0,END)
        sf.pasd.delete(0,END)
    def values(sf):
        sf.login()
        return sf.username,sf.password


        
        
