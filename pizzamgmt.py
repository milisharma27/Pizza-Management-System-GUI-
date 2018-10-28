from tkinter import *
from sqlite3 import *
from easygui import *

username=None
userid=None
email=None
db=connect('pizzadb.db')
print('Database connected')

import random
class Log:
    def destroyall(self):
    	if 'scr1' in locals():
    		self.scr1.destroy()
    	if 'scr' in locals():
    		self.scr.destroy()


    def loginv(self, user, pas, conn=db):
    	cur=conn.cursor()
    	try:
    		cur.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pas))
    		res=list(cur.fetchall())
    		if len(res)>0:
    			global username
    			username=res[0][1]
    			global userid
    			userid=res[0][0]
    			global email
    			email=res[0][4]
    			self.menu()
    		else:
    			msgbox('Sorry Wrong Username password', 'Error')
    	except:
    		msgbox('Sorry User is not found', 'error')


    def regi(self, conn, fname, lname, user, pas, email, mobile):
    	if fname.isalpha() and lname.isalpha():
    		if mobile.isnumeric() and len(mobile)==10:
    			try:
    				conn.execute("CREATE TABLE users (id integer primary key AUTOINCREMENT, username varchar(60) unique not null, lname varchar(60), fname varchar(60), email varchar(60), mobile int, password varchar(60) not null)")
    			except:
    				pass
    			try:
    				if conn.execute("INSERT INTO users (username, lname, fname, email, mobile, password) VALUES (?,?,?,?,?,?)", (user, lname, fname, email, mobile, pas)):
    					msgbox('User Created', 'Success')
    					conn.commit()
    					self.login()
    				else:
    					msgbox('Some error occured', 'Error')
    					return False
    			except:
    				msgbox('Some error occured', 'Error')
    				return False
    		else:
    			msgbox('Mobile should be 10 digit numeric value', 'Error')
    			return False
    	else:
    		msgbox('Name will only be Aplhabet', 'Error')
    		return False;




    def validate(self, v1,v2,v3,v4,v5,v6):
    	#print(v1)
    	#print(type(v1))
    	if (v1.isnumeric() or v1=='') and (v2.isnumeric() or v2=='') and (v3.isnumeric() or v3=='') and (v4.isnumeric() or v4=='') and (v5.isnumeric() or v5=='') and (v6.isnumeric() or v6==''):
    		self.order()
    	else:
    		msgbox('Please enter valid amount.', 'Error')


    def insertinto(self, v1, v2, v3, v4, v5, v6, sume, gst, total, conn=db):
    	try:
    		conn.execute("CREATE TABLE orders (id integer primary key AUTOINCREMENT, user_id integer, username varchar(60), items varchar(300), total integer, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
    	except:
    		pass
    	try:
    		lis='Veg Pizza('+v1+'), Deluxe Veggie('+v2+'), Veg Vaganza('+v3+'), Pepper Pizza('+v4+'), Margherita('+v5+'), Cold Drink('+v6+'),  SUM('+sume+'), GST('+gst+')'
    		conn.execute("INSERT INTO orders (user_id, username, items, total) VALUES (?,?,?,?)", (userid, username, lis, total))
    		conn.commit()
    	except:
    		msgbox('Sorry Some error occured', 'Error')


    def home(self):
        self.scr=Tk(className="Pizza Management Home")
        #self.scr1.destroy()
        self.scr.geometry("605x400")
        self.fr=Frame(self.scr,height=618,width=1366)
        self.scr.resizable(False, False)
        self.lab3=Label(self.fr,text="LOGIN",bg="white",font=("cooper black",20))
        self.lab3.place(x=160,y=30)
        self.lab1=Label(self.fr,text="Username",bg="white",font=("default",20))
        self.lab1.place(x=30,y=100)
        self.lab2=Label(self.fr,text="Password",bg="white",font=("default",20))
        self.lab2.place(x=30,y=150)
        self.user=Entry(self.fr,bg="white",font=("default",20))
        self.user.place(x=180,y=100)
        self.pasd=Entry(self.fr,bg="white",font=("default",20),show="*")
        self.pasd.place(x=180,y=150)
        self.fr=Frame(self.scr,bg="blue",height=618,width=1366)
        self.c=Canvas(self.fr,height=618,width=1366)
        self.c.pack()
        self.back=PhotoImage(file="pizzaback.png")
        self.c.create_image(300,200,image=self.back)
        #self.c.create_image(683,284,image=self.back)
        self.st=Button(self.fr,text="login",font=("default",20),command=self.login)
        self.st.place(x=265,y=100)
        self.si=Button(self.fr,text="Register",command=self.register,font=("default",20))
        self.si.place(x=245,y=200)
        self.fr.pack(fill=BOTH,expand=1)
        self.scr.mainloop()
    def register(self):
        self.scr.destroy()
        self.scr1=Tk(className="Pizza Management Register")
        self.fr=Frame(self.scr1,bg="DeepSkyBlue2",height=550,width=650)
        self.lab3=Label(self.fr,text="Customer Registration",bg="white",font=("default",20))
        self.lab3.place(x=250,y=50)

        self.lb1=Label(self.fr,text="First Name",bg="#d3ede6",font=("default",20))
        self.lb1.place(x=80,y=120)
        self.first=Entry(self.fr,bg="white",width=15,font=("default",20),bd=5)
        self.first.place(x=250,y=120)
        self.lab2=Label(self.fr,text="Last Name",bg="#d3ede6",font=("default",20))
        self.lab2.place(x=80,y=170)
        self.last=Entry(self.fr,bg="white",width=15,font=("default",20),bd=5)
        self.last.place(x=250,y=170)
        
        self.lab1=Label(self.fr,text="user name",bg="#d3ede6",font=("default",20))
        self.lab1.place(x=80,y=220)
        self.lab2=Label(self.fr,text="password",bg="#d3ede6",font=("default",20))
        self.lab2.place(x=80,y=270)
        self.user=Entry(self.fr,bg="white",font=("default",20),bd=5)
        self.user.place(x=250,y=220)
        self.pasd=Entry(self.fr,bg="white",font=("default",20),bd=5,show="*")
        self.pasd.place(x=250,y=270)

        self.lab5=Label(self.fr,text="Email ID",bg="#d3ede6",font=("default",20))
        self.lab5.place(x=80,y=320)
        self.email=Entry(self.fr,bg="white",width=15,font=("default",20),bd=5)
        self.email.place(x=250,y=320)
        self.lab6=Label(self.fr,text="Mobile No.",bg="#d3ede6",font=("default",20))
        self.lab6.place(x=80,y=370)
        self.mob=Entry(self.fr,bg="white",width=15,font=("default",20),bd=5)
        self.mob.place(x=250,y=370)
        self.st=Button(self.fr,text="submit",font=("default",20),command=lambda : self.regi(db, self.first.get(), self.last.get(), self.user.get(), self.pasd.get(), self.email.get(), self.mob.get()))
        self.st.place(x=200,y=450)
        #self.hm=Button(self.fr,text="Home",font=("default",20),command=self.login)how to return from function in tkinter button
        #self.hm.place(x=300, y=450)
        self.si=Button(self.fr,text="clear",command=self.clear,font=("default",20))
        self.si.place(x=380,y=450)        
        self.fr.pack(fill=BOTH,expand=1)
        self.scr.mainloop()
    def login(self):
        try:
        	self.scr.destroy()
        except:
        	pass
        try:
        	self.scr1.destroy()
        except:
        	pass
        self.scr1=Tk(className="Pizza Management Login")
        self.fr=Frame(self.scr1,bg="DeepSkyBlue2",height=400,width=600)
        self.lab3=Label(self.fr,text="Login",bg="white",font=("default",20))
        self.lab3.place(x=250,y=50)
        self.lab1=Label(self.fr,text="user name",bg="white",font=("default",20))
        self.lab1.place(x=80,y=120)
        self.lab2=Label(self.fr,text="password",bg="white",font=("default",20))
        self.lab2.place(x=80,y=170)
        self.user=Entry(self.fr,bg="white",font=("default",20))
        self.user.place(x=250,y=120)
        self.pasd=Entry(self.fr,bg="white",font=("default",20),show="*")
        self.pasd.place(x=250,y=170)
        self.st=Button(self.fr,text="submit",font=("default",20),command=lambda : self.loginv(self.user.get(), self.pasd.get()))
        self.st.place(x=200,y=250)
        self.si=Button(self.fr,text="clear",command=self.clear,font=("default",20))
        self.si.place(x=380,y=250)
        self.fr.pack(fill=BOTH,expand=1)
        self.scr.mainloop()        
    def menu(self):
            self.scr1.destroy()
            self.roo=Tk(className="MENU")
            self.roo.geometry("1000x1000")
            self.fra=Frame(self.roo,bg="DeepSkyBlue2",height=800,width=2000)
            self.roo.config(bg="DeepSkyBlue2")
            self.c=Canvas(self.fra,height=600,width=600)
            self.c.pack()
            self.roo.title("MENU")
            #self.widget = Label(self.fra, compound='top')
            #self.widget.pizza1 = PhotoImage(file="pizza1.jpg")
            #self.widget['image'] = widget.pizza1
            #self.widget.pack()
            self.v1=IntVar()
            self.v2=IntVar()
            self.v3=IntVar()
            self.v4=IntVar()
            self.v5=IntVar()
            self.v6=IntVar()
            self.labe=Label(self.fra,text="ITEM",bg="DeepSkyBlue2",font=("cooper black",20))
            self.labe.place(x=150,y=30)
            self.labe1=Label(self.fra,text="PRICE",bg="DeepSkyBlue2",font=("cooper black",20))
            self.labe1.place(x=350,y=30)
            self.labe2=Label(self.fra,text="Veg Pizza",bg="white",font=("default",16))
            self.labe2.place(x=140,y=85)
            self.labe3=Label(self.fra,text="₹250",bg="white",font=("default",16))
            self.labe3.place(x=365,y=85)
            self.labe2=Label(self.fra,text="Deluxe Veggie",bg="white",font=("default",16))
            self.labe2.place(x=125,y=115)
            self.labe3=Label(self.fra,text="₹250",bg="white",font=("default",16))
            self.labe3.place(x=365,y=115)
            self.labe2=Label(self.fra,text="Veg Vaganza",bg="white",font=("default",16))
            self.labe2.place(x=125,y=145)
            self.labe3=Label(self.fra,text="₹250",bg="white",font=("default",16))
            self.labe3.place(x=365,y=145)
            self.labe2=Label(self.fra,text="Pepper Pizza",bg="white",font=("default",16))
            self.labe2.place(x=125,y=175)
            self.labe3=Label(self.fra,text="₹250",bg="white",font=("default",16))
            self.labe3.place(x=365,y=175)
            self.labe2=Label(self.fra,text="Margherita",bg="white",font=("default",16))
            self.labe2.place(x=135,y=205)
            self.labe3=Label(self.fra,text="₹195",bg="white",font=("default",16))
            self.labe3.place(x=365,y=205)
            self.labe4=Label(self.fra,text="Cold Drink",bg="white",font=("default",16))
            self.labe4.place(x=135,y=235)
            self.labe5=Label(self.fra,text="₹40",bg="white",font=("default",16))
            self.labe5.place(x=365,y=235)
            self.labe6=Label(self.fra,text="Place your order here:",bg="DeepSkyBlue2",font=("Cooper black",16))
            self.labe6.place(x=155,y=280)
            self.lab7=Label(self.fra,text="Item",bg="white",font=("default",16))
            self.lab7.place(x=120,y=315)
            self.lab8=Label(self.fra,text="Quantity",bg="white",font=("default",16))
            self.lab8.place(x=280,y=315)
            self.lab9=Label(self.fra,text="Veg Pizza",bg="white",font=("default",16))
            self.lab9.place(x=90,y=350)
            self.v1=Entry(self.fra,bg="white",font=("default",16))
            self.v1.place(x=230,y=350)
            self.lab10=Label(self.fra,text="Deluxe Pizza",bg="white",font=("default",16))
            self.lab10.place(x=85,y=385)
            self.v2=Entry(self.fra,bg="white",font=("default",16))
            self.v2.place(x=230,y=385)
            self.lab11=Label(self.fra,text="Veg Vaganza",bg="white",font=("default",16))
            self.lab11.place(x=85,y=420)
            self.v3=Entry(self.fra,bg="white",font=("default",16))
            self.v3.place(x=230,y=420)
            self.lab12=Label(self.fra,text="Pepper Pizza",bg="white",font=("default",16))
            self.lab12.place(x=85,y=455)
            self.v4=Entry(self.fra,bg="white",font=("default",16))
            self.v4.place(x=230,y=455)
            self.lab13=Label(self.fra,text="Margherita",bg="white",font=("default",16))
            self.lab13.place(x=90,y=490)
            self.v5=Entry(self.fra,bg="white",font=("default",16))
            self.v5.place(x=230,y=490)
            self.lab14=Label(self.fra,text="Cold Drink",bg="white",font=("default",16))
            self.lab14.place(x=90,y=525)
            self.v6=Entry(self.fra,bg="white",font=("default",16))
            self.v6.place(x=230,y=525)
            self.to=Button(self.fra,text="Submit",font=("cooper black",20),bg="DeepSkyBlue3",fg="black",command=lambda: self.validate(self.v1.get(), self.v2.get(), self.v3.get(), self.v4.get(), self.v5.get(), self.v6.get()))
            self.to.place(x=250,y=565)
            self.to.pack(fill=BOTH,expand=1)
            self.fra.pack()
            self.roo.mainloop()
    def order(self):
        self.scr2=Tk(className="Place Order")
        self.scr2.geometry("450x300")
        self.scr2.resizable(False, False)
        self.scr2.title("Place Order")
        self.scr2.config(bg="DeepSkyBlue2")
        self.fram=Frame(self.scr2,height=618,width=1366,bg="DeepSkyBlue2")
        #self.v1.set("0")
        self.a=self.v1.get()
        self.b=self.v2.get()
        self.c=self.v3.get()
        self.d=self.v4.get()
        self.e=self.v5.get()
        self.f=self.v6.get()
        #print(self.a)
        if len(self.a)==0:
            self.a="0"
        #print(self.a)
        if len(self.b)==0:
            self.b="0"
        #print(self.b)
        if len(self.c)==0:
            self.c="0"
        #print(self.c)
        if len(self.d)==0:
            self.d="0"
        #print(self.d)
        if len(self.e)==0:
            self.e="0"
        #print(self.e)
        if len(self.f)==0:
            self.f="0"
        #print(self.f)
        #print(self.a)
        self.sum=int(self.a)*250+int(self.b)*250+int(self.c)*250+int(self.d)*250+int(self.e)*195+int(self.f)*40
        self.gst=(18/100)*int(self.sum)
        self.tot=int(self.gst)+int(self.sum)
        #self.tot="₹ "+str(int(((self.a)*250)+((self.b)*250)+((self.c)*250)+((self.d)*250)+((self.e)*195)+((self.f)*40)))
        #print(self.sum)
        self.labell=Label(self.fram,text="Total payable amount is ",bg="DeepSkyblue2",font=("default",16))
        self.label2=Label(self.fram,text="GST(18%) ",bg="DeepSkyblue2",font=("default",16))
        self.label3=Label(self.fram,text="Total: ",bg="DeepSkyblue2",font=("default",16))
        self.labell.place(x=90,y=110)
        self.label2.place(x=90,y=70)
        self.label3.place(x=90,y=30)
        #self.dis=Entry(self.fram,text="%s" %(self.tot),bg="white",font=("default",16))
        self.val=Label(self.fram,text=self.sum,bg="white",font=("default",16))
        self.val2=Label(self.fram,text=self.gst,bg="white",font=("default",16))
        self.val3=Label(self.fram,text=self.tot,bg="white",font=("default",16))
        self.insertinto(self.a, self.b, self.c, self.d, self.e, self.f, self.sum, self.gst, self.tot)
        self.val.place(x=320,y=110)
        self.val2.place(x=320,y=70)
        self.val3.place(x=320,y=30)
        self.fram.pack()
        self.scr.mainloop()

    def result(self):
        self.username=self.user.get()
        self.password=self.pasd.get()
        try:
            self.scr.destroy()
        except:
            try:
                self.scr1.destroy()
            except:
                pass
    def clear(self):
        self.user.delete(0,END)
        self.pasd.delete(0,END)
    def values(self):
        self.login()
        return self.username,self.password

a= Log()
a.home()
db.commit()
