
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root = Tk()
root.geometry("200x200")

def msg_box():
    messagebox.showinfo("Alert", "Login Successfully 😊")

img= Image.open("submit.png")
resized_image= img.resize((120,60))
login_btn = ImageTk.PhotoImage(resized_image)
#--------------------------------------------------Create button and image
img = Button(root, image=login_btn, borderwidth=0,command=msg_box)
img.place(x=35,y=50)

root.mainloop()
