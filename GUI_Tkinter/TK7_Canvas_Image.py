
#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("350x370")

#Create a canvas
canvas= Canvas(win, width= 150, height= 150,bg="pink")
canvas.place(x=100,y=50)

#Load an image in the script
img= (Image.open("sunflower.png"))

#Resize the Image using resize method
resized_image= img.resize((150,150), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(70,70, image=new_image)

win.mainloop()

