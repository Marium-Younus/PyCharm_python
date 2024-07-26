from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window = Tk()
window.geometry("500x500")
#------------------------------------ variables
fn=StringVar()
ln=StringVar()
dob=StringVar()
country = StringVar()
p1 = IntVar()
p2 = IntVar()
gen =IntVar()
#-==============================================exit
def quit():
    exit()

def register():
    if (p1.get() == 1) & (p2.get() == 0):
        checkval='I Like Python '
    elif (p1.get() == 0) & (p2.get() == 1):
        checkval='I Like C++'
    elif (p1.get() == 0) & (p2.get() == 0):
        checkval='I do not like anything'
    else:
        checkval='I Like both'
    if (gen.get()==1):
        gender = 'Male'
    else:
        gender = 'Female'
    info=   "Username : "+fn.get()+" "+ln.get()+"\nDate of Birth : "+dob.get()+"\nCountry is : "+country.get()+"\nLanguages is : "+checkval+"\nGender is : "+gender

    MsgBox = messagebox.askquestion('Register Info','Do you want to save this information\n\n'+info , icon='warning')
    if MsgBox == 'yes':
        messagebox.showinfo('Return', 'Registeration Complete 😊')
    else:
        window.destroy()

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
c1 = Checkbutton(window, text='Python', variable=p1, onvalue=1)
c1.place(x=235,y=285)
c2 = Checkbutton(window, text='C++', variable=p2, onvalue=1)
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
img = Button(window, image=login_btn, borderwidth=0,command=register)
img.place(x=90,y=350)
#----------------------------------------Button  exit
q_btn= Image.open("exit.png")
resized_image= q_btn.resize((120,45))
exit_btn = ImageTk.PhotoImage(resized_image)
q_btn = Button(window, image=exit_btn, borderwidth=0,command=quit)
q_btn.place(x=330,y=350)
window.mainloop()