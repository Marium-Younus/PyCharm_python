
from tkinter import *
from  tkinter import  ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import  mysql.connector

window = Tk()
window.geometry("820x600+100+100")
global name
global course
global fees
global hidebox
#----------Double click record get
def GetValue(event):
    name.delete(0, END)
    course.delete(0, END)
    fees.delete(0, END)
    hidebox.delete(0,END)
    row_id = listbox.selection()[0]
    select = listbox.set(row_id)
    print(select)
    hidebox.insert(0,select['Id'])
    name.insert(0,select['Name'])
    course.insert(0,select['Course'])
    fees.insert(0,select['Fee'])


#=============================================================Insert Record
def insert():
    stdname=name.get()
    stdcourse=course.get()
    stdfees=fees.get()
    connect = mysql.connector.connect(host="localhost",user="root",password="",database="tkinter_db")
    mycursor = connect.cursor()
    try:
        ins_query = "INSERT INTO student_tbl (std_name, std_course, std_fee) VALUES (%s, %s, %s)"
        val = (stdname,stdcourse,stdfees)
        mycursor.execute(ins_query,val)
        connect.commit()
        messagebox.showinfo("Information","Record inserted")
        name.delete(0,END)
        course.delete(0,END)
        fees.delete(0, END)
        name.focus_set()
    except Exception as e:
        print(e)
        connect.rollback()
        connect.close()
#=======================================================================Update Record
def update():
    u_name=name.get()
    u_course=course.get()
    u_fees=fees.get()
    u_id=hidebox.get()
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="tkinter_db")
    mycursor = connect.cursor()
    try:
        update_query = "UPDATE student_tbl set std_name = %s, std_course = %s, std_fee =%s WHERE  id = %s"
        val = (u_name, u_course, u_fees,u_id)
        mycursor.execute(update_query, val)
        connect.commit()
        messagebox.showinfo("Information", "Record Updated 👍")
        name.delete(0, END)
        course.delete(0, END)
        fees.delete(0, END)
        hidebox.delete(0,END)
        name.focus_set()

    except Exception as e:
        print(e)
        connect.rollback()
        connect.close()

#===========================================Delete
def delete():
    del_id=hidebox.get()
    print(del_id)
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="tkinter_db")
    mycursor = connect.cursor()
    try:
        delete_query = "DELETE FROM student_tbl WHERE id = %s"
        val = (del_id,)
        mycursor.execute(delete_query, val)
        connect.commit()
        messagebox.showinfo("Information", "Record Deleted 🥺")
        name.delete(0, END)
        course.delete(0, END)
        fees.delete(0, END)
        hidebox.delete(0, END)
        name.focus_set()

    except Exception as e:
        print(e)
        connect.rollback()
        connect.close()
# =======================================================================Show Record
def show():
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="tkinter_db")
    mycursor = connect.cursor()
    mycursor.execute("SELECT id,std_name,std_course,std_fee FROM student_tbl")
    records=mycursor.fetchall()
    print(records)
    for i ,(id,std_name,std_course,std_fee) in enumerate(records,start=1):
        listbox.insert("","end",values=(id,std_name,std_course,std_fee))
        connect.close()
l1=Label(window,text="Registeration form :  ",width=20,font=("Algerian",16,"bold"),fg="Blue")
l1.place(x=300,y=2)
#----------------------------------------------------------------------
l1=Label(window,text="Student Name :  ",width=20,font=("calibri",12,"bold"),fg="Blue")
l1.place(x=250,y=30)
name=Entry(window,width=30)
name.place(x=390,y=35)
#==================================================================================================hidden input
hidebox=Entry(window,width=2,bg="red",fg="#000",font=("calibri",30,"bold"))
hidebox.place(x=650,y=35)
#----------------------------------------------------------------------
l2=Label(window,text="Course Name  :  ",width=20,font=("calibri",12,"bold"),fg="Blue")
l2.place(x=250,y=60)
course=Entry(window,width=30)
course.place(x=390,y=60)
#----------------------------------------------------------------------
l3=Label(window,text="Fees               :",width=20,font=("calibri",12,"bold"),fg="Blue")
l3.place(x=250,y=90)
fees=Entry(window,width=30)
fees.place(x=390,y=90)
#------------------------------------------------------------------------------
img= Image.open("add.png")
resized_image= img.resize((64,64))
add_btn = ImageTk.PhotoImage(resized_image)
img = Button(window, image=add_btn, borderwidth=0,command=insert)
img.place(x=360,y=130)
#------------------------------------------------------------------------------
e_img= Image.open("update.png")
resized_image1= e_img.resize((64,64))
edit_btn = ImageTk.PhotoImage(resized_image1)
e_img = Button(window, image=edit_btn, borderwidth=0,command=update)
e_img.place(x=440,y=130)
#------------------------------------------------------------------------------
d_img= Image.open("delete.png")
resized_image2= d_img.resize((64,64))
del_btn = ImageTk.PhotoImage(resized_image2)
d_img = Button(window, image=del_btn, borderwidth=0,command=delete)
d_img.place(x=520,y=130)
#------------------------------------------------------------------------------List Box
cols = ('Id','Name','Course','Fee')
listbox= ttk.Treeview(columns=cols,show='headings')
for col in cols:
    listbox.heading(col,text=col)
    listbox.grid(row=1,column=0)
    listbox.place(x=10,y=210)

show()
listbox.bind('<Double-Button-1>',GetValue)

window.mainloop()