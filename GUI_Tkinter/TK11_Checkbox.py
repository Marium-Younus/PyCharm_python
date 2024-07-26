from tkinter import *
window = Tk()
window.title('My Window')
window.geometry('300x200')
#===========================================================
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not anything')
    else:
        l.config(text='I love both')
#===========================================================
var1 = IntVar()
var2 = IntVar()

c1 = Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
l = Label(window, bg='yellow', width=20, text='',relief='solid')
l.pack(fill="both",pady=2,padx=2)
window.mainloop()

