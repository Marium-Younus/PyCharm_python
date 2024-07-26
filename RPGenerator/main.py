from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import random
import string
import customtkinter

from PIL import ImageTk,Image,ImageDraw,ImageFont

# PASSWORD GENERATOR

#Splash Screen
splash_root = Tk()
splash_root.geometry("500x400+420+100")
splash_root.title("Password Generator")

# Hide title bar
splash_root.overrideredirect(True)


# Images
bg = PhotoImage(file="Images/splash.png")
my_label = Label(splash_root, image=bg)
my_label.pack()
# #canvas'
# my_canvas = Canvas(splash_root, width=500, height=350)
# my_canvas.pack(fill="both", expand=True)
# my_canvas.create_image(0,0, image = bg, anchor="nw")

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='dark green')
progress = Progressbar(splash_root, style="red.Horizontal.TProgressbar",
                       orient=HORIZONTAL,
                       length=270,
                       mode='determinate')
progress.place(x=125, y=300)
progress.start(22)



#PGenerator Start
def main_window():
    progress.stop()
    splash_root.destroy()

    root = Tk()
    root.resizable(0,0)
    root.geometry("500x400+420+100")
    root.title("Password Generator")


    bg = PhotoImage(file="Images/green3.png")
    # Show image using label
    # label1 = Label(root, image=bg)
    # label1.pack()

    # canvas'
    my_canvas = Canvas(root, width=500, height=350)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    ##### INITIAL VARIABLES
    title = StringVar()
    choice = IntVar()
    lengthlabel = StringVar()
    passlength = IntVar()
    symbols = """~`!§@#$%^&*()_-+={}[]:;"'<>,.?/"""
    poor = string.ascii_lowercase + string.digits
    average = string.ascii_uppercase + string.ascii_lowercase + string.digits
    advanced = poor + average + symbols

    # FUNCTIONS
    def selection():
        choice.get()

    # Password generation script - joins a random symbol to the string for how many times set in the spinbox
    view_pass = StringVar()

    def passgen():
        global password
        password = ""
        if choice.get() == 1:
            password = password.join(random.sample(poor, passlength.get()))
        elif choice.get() == 2:
            password = password.join(random.sample(average, passlength.get()))
        elif choice.get() == 3:
            password = password.join(random.sample(advanced, passlength.get()))
        view_pass.set(password)

    # passtext = passgen()

    # Copies the current password to the clipboard
    def copytoclipboard():
        global password
        print(password)
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

    ##### USER INTERFACE
    # my_canvas.create_text(250, 20, text="Welcome To The Password Generator", font=('Trajan Pro', 13, 'bold'))


    R1 = Radiobutton(root, text="POOR", fg="light green",
                     font=('Trajan Pro', 10, 'bold'),
                     variable=choice,
                     value=1,bg="#08482d",
                     command=selection).place(x=210,y=100)

    R2 = Radiobutton(root, text="AVERAGE", fg="blue",
                     font=('Trajan Pro', 10, 'bold'),
                     variable=choice,
                     value=2,bg="#08482d",
                     command=selection).place(x=290,y=100)

    R3 = Radiobutton(root, text="ADVANCE", fg="red",
                     font=('Trajan Pro', 10, 'bold'),
                     variable=choice,
                     value=3,bg="#08482d",
                     command=selection).place(x=390,y=100)


    lengthpass = Label(root, text="Password length: (8 to 24)",
                       font=('Arial', 10, 'bold'),
                       fg="white", bg="#08482d").place(x=250,y=150)

    pspinbox = Spinbox(root, from_=8, to_=24, textvariable=passlength, width=20).place(x=265,y=185)

    button = customtkinter.CTkButton(master=root,
                                     fg_color=("white"),
                                     text_color=("black"),
                                     text_font=('Calibri', 11, 'bold'),
                                     text="Generate",
                                     command=passgen,
                                     width=80,
                                     height=25,
                                     border_width=0,
                                     corner_radius=30)
    button.place(x=180,y=259)

    passwordlabel = Label(root, textvariable=view_pass,

                          font=('Arial', 20, 'bold'),fg="white",
                          bg="#08482d").place(relx=0.55,rely=0.9, anchor=CENTER)

    button = customtkinter.CTkButton(master=root,
                                     fg_color=("white"),
                                     text_color=("black"),
                                     text_font=('Calibri', 11, 'bold'),
                                     text="Copy To Clip",
                                     command=copytoclipboard,
                                     width=80,
                                     height=25,
                                     border_width=0,
                                     corner_radius=30)
    button.place(x=350, y=259)

    root.mainloop()

# def bar():
#     my_canvas.create_text(65, 220, text='Loading.....', font=('Trajan Pro', 10, 'bold'))
#
#
#     import time
#     r = 0
#     for i in range(100):
#         progress['value'] = r
#         splash_root.update_idletasks()
#         time.sleep(0.01)
#         r = r + 1
#
#     main_window()
#
# # Images
# bg = PhotoImage(file="Images/green1.png")
#
# #canvas'
# my_canvas = Canvas(splash_root, width=500, height=350)
# my_canvas.pack(fill="both", expand=True)
# my_canvas.create_image(0,0, image = bg, anchor="nw")
#
#
# s = ttk.Style()
# s.theme_use('clam')
# s.configure("red.Horizontal.TProgressbar", foreground='red', background='dark green')
# progress = Progressbar(splash_root, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=450, mode='determinate')
# progress.place(x=25, y=235)
#
#
# b1 = Button(splash_root, width=10, height=2, text='Get Started', command=bar, border=2, fg='black',bg='white')
# b1.place(x=200, y=160)
#
#
# my_canvas.create_text(180,80, text='Random', font=('Trajan Pro', 20, 'bold'))
#
#
# my_canvas.create_text(330,80, text='Password', font=('Trajan Pro', 20, 'bold'))
#
#
# my_canvas.create_text(180,110, text='Generator', font=('Trajan Pro', 13, 'bold'))

splash_root.after(3000,main_window)
splash_root.mainloop()