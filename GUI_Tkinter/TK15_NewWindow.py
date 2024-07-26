from tkinter import *
window1 = Tk()
# window1.geometry("+300+300")
window1.attributes('-fullscreen', TRUE)
window1.title("Pag1")

#----------------------------------------------------------------------------------------------------
def login_page():
    window2 = Tk()
    window2.geometry("+300+300")
    window2.title("Page2")
    def quit():
      window2.destroy()
    btn2= Button(window2, text="Exit", bg="#ff0000", fg="#fff", font=("arial", 12, "bold"), command=quit)
    btn2.place(x=60, y=60)
#----------------------------------------------------------------------------------------------------
btn1 = Button(window1,text="New Window",bg="#00004C",fg="#fff",font=("arial",12,"bold"),command=login_page)
btn1.place(x=60,y=60)

window1.mainloop()
