from tkinter import *
window = Tk()
window.geometry("300x200")
window.title("Welcome")

fn=StringVar()
ln=StringVar()

#=================================================================================
l1=Label(window,text="First Name:",width=20,font=("calibri",12,"bold"))
l1.place(x=5,y=30)
box1=Entry(window,textvar= fn)
box1.place(x=130,y=30)
#==================================================================================
l2=Label(window,text="Last Name:",width=20,font=("calibri",12,"bold"))
l2.place(x=5,y=60)
box2=Entry(window,textvar= ln)
box2.place(x=130,y=60)
#=================================================================================
def funct():
    fullname = "Welcome "+fn.get()+" "+ ln.get()
    res=Label(window, text=fullname, font=("calibri", 12, "bold"),fg="Green")
    res.place(x=60, y=130)
#==================================================================================
btn1 = Button(window,text=" Submit ",bg="#00004C",fg="#fff",font=("arial",12,"bold"),command=funct)
btn1.place(x=175,y=90)

window.mainloop()


