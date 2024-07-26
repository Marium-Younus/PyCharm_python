from tkinter import *
window = Tk()
window.geometry("300x200")
window.title("Welcome")

l1=Label(window,text="Select Country:",width=20,font=("calibri",12,"bold"))
l1.place(x=5,y=30)
country = StringVar()

list1 = ['Pakistan','India','Nepal','Canada','SriLanka']
dropdown= OptionMenu(window,country,*list1)
country.set("Select Country")
dropdown.config(width=15)
dropdown.place(x=150,y=30)
def funct():
    result="My Country Name is "+country.get()
    res = Label(window, text=result, font=("calibri", 12, "bold"), fg="blue")
    res.place(x=60, y=130)
#==================================================================================
btn1 = Button(window,text=" Submit ",bg="#00004C",fg="#fff",font=("arial",12,"bold"),command=funct)
btn1.place(x=175,y=90)
window.mainloop()

