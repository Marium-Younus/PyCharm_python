
from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Working with Button")
btn1 = Button(window,text="RIDGE",bg="#00004C",fg="#fff",relief=RIDGE,font=("arial",14,"bold"))
btn1.place(x=110,y=30)
btn2 = Button(window,text="GROOVE",bg="#00004C",fg="#fff",relief=GROOVE,font=("arial",14,"bold"))
btn2.place(x=110,y=80)
btn3 = Button(window,text="SUNKEN",bg="#00004C",fg="#fff",relief=SUNKEN,font=("arial",14,"bold"))
btn3.place(x=110,y=130)
btn4 = Button(window,text="RAISED",bg="#00004C",fg="#fff",relief=RAISED,font=("arial",14,"bold"))
btn4.place(x=110,y=190)
window.mainloop()




