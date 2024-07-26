
from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")
lbl_1 = Label(window,text="Welcome to tkinter",font=("algerian",16,"bold"),relief="solid",bg="yellow")
lbl_1.pack(fill="both",pady=2,padx=2)
btn1 = Button(window,text="Click",bg="#00004C",fg="#fff",relief=RAISED,font=("arial",14,"bold"))
btn1.place(x=110,y=90)                                 #GROOVE,RIDGE,SUNKEN,RAISED
window.mainloop()




