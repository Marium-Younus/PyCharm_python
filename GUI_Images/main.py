from operator import le
from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.geometry("800x700")
window.title("Slide Image")
#-------------------Leftpanel
leftpanel = Canvas(window,width="250",height="650",bg="black")
leftpanel.place(x=10,y=10)


#-------------------rightpanel
rightpanel = Canvas(window,width="490",height="450",bg="pink")
rightpanel.place(x=250,y=100)
#
# l1 = Label(rightpanel,text="Table",font=("comic sans ms",20,"bold"),bg="pink")
# l1.place(x=10,y=40)
# ----------------------------- 1.
def one():
    # table=0
    # a=5
    # i = 1
    # while i <= 5:
    #     table = a , "x" , i , "=" ,(a * i)
    #     i = i + 1
    previous = 0
    for number in range(10):
        temp = previous + (number, "x" , i , "=" ,(a * i))
        previous = temp
    l1 = Label(rightpanel, text=temp, font=("comic sans ms", 20, "bold"), bg="pink")
    l1.place(x=10,y=40)

#------------------------------- 1

a = Image.open('images/1.png')
b = a.resize((90, 90),)
c = ImageTk.PhotoImage(b)
btn1=Button(
    leftpanel,
    image=c,
    command=one
)
btn1.place(x=70,y=20)

#------------------------------- 2
x = Image.open('images/2.png')
y = x.resize((90, 90))
z = ImageTk.PhotoImage(y)
btn2=Button(
    leftpanel,
    image=z,
    command=one
)
btn2.place(x=70,y=150)

#------------------------------- 3
i = Image.open('images/3.png')
j = i.resize((90, 90))
k = ImageTk.PhotoImage(j)
btn3=Button(
    leftpanel,
    image=k,
    command=one
)
btn3.place(x=70,y=280)

#------------------------------- 4
m = Image.open('images/4.png')
n = m.resize((90, 90))
o = ImageTk.PhotoImage(n)
btn4=Button(
    leftpanel,
    image=o,
    command=one
)
btn4.place(x=70,y=410)

#------------------------------- 5
p = Image.open('images/5.png')
q = p.resize((90, 90))
r = ImageTk.PhotoImage(q)
btn5=Button(
    leftpanel,
    image=r,
    command=one
)
btn5.place(x=70,y=540)





window.mainloop()