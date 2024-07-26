from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import  mysql.connector
from  tkinter import  ttk
window = Tk()
window.geometry("900x600")
#------------------------------------ variables
fn=StringVar()
ln=StringVar()
dob=StringVar()
country = StringVar()
lang1 = IntVar()
lang2 = IntVar()
gen =IntVar()
#-==============================================exit
def quit():
    exit()
#----------Double click record get
def GetValue(event):
    fname = fn.get()
    lname = ln.get()
    birthday = dob.get()
    row_id = listbox.selection()[0]
    select = listbox.set(row_id)
    print(select)
    fn.a
    ln.insert(0,select['LN'])
    dob.insert(0,select['DATE'])
#=============================================================Insert Record
def insert():
    fname=fn.get()
    lname=ln.get()
    birthday=dob.get()
    con= country.get()
    if (lang1.get() == 1) & (lang2.get() == 0):
        checkval = 'I Like Python '
    elif (lang1.get() == 0) & (lang2.get() == 1):
        checkval = 'I Like C++'
    elif (lang1.get() == 0) & (lang2.get() == 0):
        checkval = 'I do not like anything'
    else:
        checkval = 'I Like both'
    if (gen.get() == 1):
        gender = 'Male'
    else:
        gender = 'Female'
    connect = mysql.connector.connect(host="localhost",user="root",password="",database="person")

    mycursor = connect.cursor()
    try:
        ins_query = "INSERT INTO person (first_name, last_name, date,country,language,gender) VALUES (%s, %s, %s,%s, %s, %s)"
        val = (fname,lname,birthday,con,checkval,gender)
        mycursor.execute(ins_query,val)
        connect.commit()
        messagebox.showinfo("Information","Record inserted")
        fn.delete(0,END)
        ln.delete(0,END)
        dob.delete(0, END)
        fn.focus_set()
    except Exception as e:
        print(e)
        connect.rollback()
        connect.close()
# =======================================================================Show Record
def show():
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="person")
    mycursor = connect.cursor()
    mycursor.execute("SELECT id, first_name, last_name, date,country,language,gender FROM person")
    records=mycursor.fetchall()
    print(records)
    for i ,(id,first_name, last_name, date,country,language,gender) in enumerate(records,start=1):
        listbox.insert("","end",values=(id,first_name, last_name, date,country,language,gender))
        connect.close()
l1=Label(window,text="Registeration form :  ",width=20,font=("Algerian",16,"bold"),fg="Blue")
l1.place(x=300,y=2)

#-------------------------------------- logo
img = Image.open("logo.png")
resized_image= img.resize((100,100),Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
Label(window,image=new_image).place(x=200,y=10)
#-------------------------------------- title
l1 = Label(window,text="Registeration Form",font=("comic sans ms",16,"bold"),bg="#326FAD",fg="white")
l1.pack(fill="both",pady=120)
#----------------------------------------Firstname
l2=Label(window,text="First Name :",width=20,font=("calibri",14,"bold"),fg="#193756")
l2.place(x=70,y=160)
box1=Entry(window,textvar= fn)
box1.config(width=35)
box1.place(x=230,y=165)
#----------------------------------------lastname
l3=Label(window,text="Last Name :",width=20,font=("calibri",14,"bold"),fg="#193756")
l3.place(x=70,y=190)
box2=Entry(window,textvar= ln)
box2.config(width=35)
box2.place(x=230,y=195)
#----------------------------------------DOB
l4=Label(window,text="Date of Birth :",width=20,font=("calibri",14,"bold"),fg="#193756")
l4.place(x=60,y=220)
box3=Entry(window,textvar= dob)
box3.config(width=35)
box3.place(x=230,y=225)
#----------------------------------------country
list1 = ['Pakistan','India','Nepal','Canada','SriLanka']
l5=Label(window,text="Select Country :",width=20,font=("calibri",14,"bold"),fg="#193756")
l5.place(x=60,y=250)
dropdown = OptionMenu(window,country,*list1)
country.set("Select Country")
dropdown.config(width=29)
dropdown.place(x=227,y=250)
#----------------------------------------Select language
l6=Label(window,text="Select Language:",width=20,font=("calibri",14,"bold"),fg="#193756")
l6.place(x=60,y=280)
c1 = Checkbutton(window, text='Python', variable=lang1, onvalue=1)
c1.place(x=235,y=285)
c2 = Checkbutton(window, text='C++', variable=lang2, onvalue=1)
c2.place(x=300,y=285)
#----------------------------------------Select Gender
l7=Label(window,text="Select Gender:",width=20,font=("calibri",14,"bold"),fg="#193756")
l7.place(x=60,y=310)
r1 = Radiobutton(window,text="Male",variable=gen,value=1).place(x=235,y=315)
r2 = Radiobutton(window,text="Female",variable=gen,value=2).place(x=300,y=315)
#----------------------------------------Button login
img= Image.open("submit.png")
resized_image= img.resize((120,45))
login_btn = ImageTk.PhotoImage(resized_image)
img = Button(window, image=login_btn, borderwidth=0,command=insert)
img.place(x=90,y=350)
#----------------------------------------Button  exit
q_btn= Image.open("exit.png")
resized_image= q_btn.resize((120,45))
exit_btn = ImageTk.PhotoImage(resized_image)
q_btn = Button(window, image=exit_btn, borderwidth=0,command=quit)
q_btn.place(x=330,y=350)


#------------------------------------------------------------------------------List Box
cols = ('Id','FN','LN','DATE','COUNTRY','LANGUAGE','GENDER')
listbox= ttk.Treeview(columns=cols,show='headings')
for col in cols:
    listbox.heading(col,text=col)
    listbox.pack()


show()
listbox.bind('<Double-Button-1>',GetValue)
window.mainloop()