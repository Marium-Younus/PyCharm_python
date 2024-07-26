from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
w = Label(root, text='Dialog Box', font="50")
w.pack()
def msg_box():
    messagebox.showinfo("showinfo", "Information")
def war_box():
    messagebox.showwarning("showwarning", "Warning")
def error_box():
    messagebox.showerror("showerror", "Error")
def qust_box():
    messagebox.askquestion("askquestion", "Are you sure?")
def can_box():
    messagebox.askokcancel("askokcancel", "Want to continue?")
def ask_box():
    messagebox.askyesno("askyesno", "Find the value?")
def try_box():
    messagebox.askretrycancel("askretrycancel", "Try again?")
Button(root,text="Alert",bg="#00004C",fg="#fff",font=("arial",14,"bold"),command=msg_box).place(x=110,y=30)
Button(root,text="Warning",bg="#00004C",fg="#fff",font=("arial",14,"bold"),command=war_box).place(x=110,y=80)
Button(root,text="Error",bg="#00004C",fg="#fff",font=("arial",14,"bold"),command=error_box).place(x=110,y=130)
Button(root,text="Question",bg="#00004C",fg="#fff",font=("arial",14,"bold"),command=qust_box).place(x=110,y=180)
Button(root,text="Cancel",bg="#00004C",fg="#fff",font=("arial",14,"bold"),command=can_box).place(x=110,y=230)
Button(root,text="Yes/No",bg="#00004C",fg="#fff",font=("arial",14,"bold"),command=ask_box).place(x=110,y=290)
Button(root,text="Try",bg="#00004C",fg="#fff",font=("arial",14,"bold"),command=try_box).place(x=110,y=330)
root.mainloop()

