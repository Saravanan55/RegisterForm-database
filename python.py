from tkinter import *
import sqlite3

root=Tk()
root.geometry('500x500')
root.title("Register Form")


Fullname=StringVar()
Email=StringVar()
var=StringVar()
c=StringVar()
var1=StringVar()
#-----------------------------DATABASE----------------------------
def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn=sqlite3.connect("Form.db")
   with conn:
        cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,)) 
   conn.commit() 
#--------------------------------------------------------------- 
label_0=Label(root, text="Register form",width=20,font=("bold",20))
label_0.place(x=90,y=53)

label_1=Label(root, text="FullName",width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1=Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2=Label(root, text="Email",width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_2=Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3=Label(root, text="Gender",width=20,font=("bold",10))
label_3.place(x=70,y=230)

entry_3=Entry(root,textvar=var)
entry_3.place(x=240,y=230)
'''
var=StringVar()
Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=290,y=230)
'''
label_4=Label(root, text="country",width=20,font=("bold",10))
label_4.place(x=70,y=280)

entry_4=Entry(root,textvar=c)
entry_4.place(x=240,y=280)

'''
list1={'canada','India','UK','Iceland','Nepal'}
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240,y=280)
'''

label_4=Label(root, text="programming",width=20,font=("bold",10))
label_4.place(x=85,y=330)

entry_4=Entry(root,textvar=var1)
entry_4.place(x=240,y=330)
'''
var1=StringVar()
Checkbutton(root,text="java",variable=var1).place(x=235,y=330)
var2=StringVar()
Checkbutton(root,text="python",variable=var2).place(x=290,y=330)
'''

Button(root,text="Submit",width=20,bg='blue',fg="white",command=database).place(x=180,y=380)

root.mainloop()


