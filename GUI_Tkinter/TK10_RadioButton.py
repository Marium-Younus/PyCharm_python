from tkinter import *
window = Tk()
window.geometry("300x200")
window.title("Welcome")
gen =IntVar()
#===================================================================================
def funct():
    result="Gender is "+str(gen.get())
    res = Label(window, text=result, font=("calibri", 12, "bold"), fg="blue")
    res.place(x=60, y=130)
#==================================================================================
l1=Label(window,text="Select Gender:",width=20,font=("calibri",12,"bold"))
l1.place(x=5,y=30)

r1 = Radiobutton(window,text="Male",variable=gen,value=1,indicator = 0).place(x=140,y=30)
r2 = Radiobutton(window,text="Female",variable=gen,value=2,indicator = 0).place(x=190,y=30)
#==================================================================================
btn1 = Button(window,text=" Submit ",bg="#00004C",fg="#fff",font=("arial",12,"bold"),command=funct)
btn1.place(x=175,y=90)
window.mainloop()


