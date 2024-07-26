
from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Event handling")
l1 = Label(window, text="Handle Button Click Event", bg="yellow", fg="Black", font=("Calibri", 14, "bold"))
l1.pack(fill="both", pady=2, padx=2)
def funct():
    Label(window, text="Welcome to my First GUI application",font=("arial", 12, "bold")).pack()
    # print("Welcome to my First GUI application")
def quit():
    exit()

btn1 = Button(window,text=" Check ",bg="#00004C",fg="#fff",relief=RAISED,font=("arial",14,"bold"),command=funct)
btn1.place(x=110,y=90)

btnexit = Button(window,text="   Quit   ",bg="#ff0000",fg="#fff",relief=RAISED,font=("arial",14,"bold"),command=quit)
btnexit.place(x=110,y=150)
window.mainloop()

