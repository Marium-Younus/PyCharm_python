#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk        # pip install pillow

window = Tk()                        #Create an instance of tkinter frame
window.geometry("300x300")
window.title("Working with Image")

img = Image.open("apple.png")        #Load an image in the script
resized_image= img.resize((100,100),Image.ANTIALIAS) #Resize the Image using resize method
new_image= ImageTk.PhotoImage(resized_image)
Label(window,image=new_image).place(x=100,y=50)

Label(window,text="Figure 1 : Apple Image",bg="yellow").place(x=100,y=160)
window.mainloop()

