from tkinter import *
root = Tk()
root.title("Menu")
root.geometry("500x500")
menubar = Menu(root)
def frame1():
    hide_all_frames()
    newframe1.pack(fill="both",expand=1)
    Label(newframe1,text="I am Frame1",bg="yellow").pack()
def frame2():
    hide_all_frames()
    newframe2.pack(fill="both", expand=1)
    Label(newframe2,text="I am Frame2", bg="pink").pack()
def hide_all_frames():
    newframe1.pack_forget()
    newframe2.pack_forget()
#----------------------------------------------------------------
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="Frame 1",command=frame1)
file.add_command(label="Open")
file.add_command(label="Exit", command=root.quit)
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Frame2",command=frame2)
#------------------------------------------------------------------
newframe1 = Frame(root,width=200,height=200,bg="red")
newframe2 = Frame(root,width=200,height=200,bg="blue")
root.config(menu=menubar)
root.mainloop()

