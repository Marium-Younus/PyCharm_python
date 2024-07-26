import tkinter as tk
import random
import pygame
from random import choice
from PIL import Image, ImageTk
from tkinter.messagebox import *

pygame.mixer.init()
# global
x = 0
tries = 3
global score
score = 0


# functions
def easy_start():
    global x
    if x == 0:
        start.destroy()
        x = x + 1
        pygame.mixer.music.load('easy.mp3')
        pygame.mixer.music.play(loops=1000)

    def check():
        global score
        global tries
        if entry1.get() == str1:
            showinfo("Congratulations", "You have guessed the word correctly")
            score += 10
            scorelabel.config(text="Your Score : " + str(score))
            resume()
        else:
            showerror("Sorry", "Please Try again , Tries Left:"+ str(tries-1))
            tries -= 1
            if tries == 0:
                pygame.mixer.music.stop()
                win.destroy()
                lose = tk.Tk()
                lose.geometry("520x500+500+100")
                lose.resizable(0, 0)
                lose.title("Word Finder The Game")
                can = tk.Canvas(lose, width=600, height=600)
                can.place(x=0, y=0)
                img = Image.open("lose.jpg")
                img_size = img.resize((600, 590))
                photo = ImageTk.PhotoImage(img_size)
                can.create_image((220, 220), image=photo)
                can.create_text(250,150, text="SORRY YOU LOSE", font=("algerian", 36, "bold italic"),fill='white')
                can.create_text(250,200, text="TO MANY TRIES", font=("algerian", 28, "bold italic"),fill='white')
                can.create_text(250,250, text="YOUR SCORE: "+str(score),font=("algerian", 20, "bold italic"), fill='white')
                lose.mainloop()

    def resume():
        win.destroy()
        easy_start()

    # colors
    colors = ["#FFF8DC", "#FFEBCD", "#FFE4C4", "#FFDEAD", "#F5DEB3", "#DEB887", "#D2B48C", "#BC8F8F", "#F4A460",
              "#DAA520", "#B8860B"
        , "#CD853F", "#D2691E", "#8B4513", "#A0522D", "#A52A2A", "#800000", "#00FFFF", "#E0FFFF", "#AFEEEE", "#7FFFD4",
              "#40E0D0"
        , "#48D1CC", "#00CED1", "#F59EA0", "#4682B4", "#B0C4DE", "#ADD8E6", "#87CEFA", "#00BFFF", "#1E90FF"
        , "#6495ED", "#7B68EE", "#4169E1", "#0000FF", "#0000CD", "#00008B", "#000080", "#191970", "#ADFF24", "#FFE4E1",
              "#00FF00"
        , "#9370DB", "#EE82EE", "#F0E68C", "#FFDAB9", "#FFE4D5", "#FFFF00", "#FFD700", "#FFA500", "#FF4500", "#FF1493",
              "#FF4444"
        , "#FFA07A", "#00FF00", "#9ACD32", "#00FF74", "#20B2AA", "#98FB98"]
    fg_colors = ["#000000", "#FFFFFF", "#FFFAFA", "#F0FFF0", "#F5FFFA", "#F0FFFF", "#F0F8FF", "#F8F8FF", "#F5F5F5",
                 "#FFF5EE", "#F5F5DC", "#FFFAF0"
        , "#FDF5E6", "#FFFFF0", "#FAEBD7", "#FAF0E6", "#FFF0F5", "#FFE4E1", "#FFE4E1", "#DCDCDC", "#D3D3D3", "#C0C0C0",
                 "#A9A9A9", "#808080"
        , "#696969", "#778899", "#708090", "#2F4F4F"]
    words = ["spice", "beast", "world", "motor", "empty", "word", "hairs", "years", "ears", "bottle", "facts", "front",
             "jump", "spoon", "plate", "sound", "glass", "face", "march", "giant", "bomb", "class", "minus", "long",
             "short", "tries", "tyre", "bike", "last", "rest", "peace", "piece", "please", "honor", "prize", "pick"]
    word = random.randint(0, (len(words) - 1))
    str1 = words[word]
    bg = choice(colors)
    fg = choice(fg_colors)
    s = ''.join(random.sample(str1, len(str1)))
    win = tk.Tk()
    win.geometry("520x500+500+100")
    win.resizable(0, 0)
    win.title("Jumble Word Game")
    can_easy = tk.Canvas(win, width=600, height=600)
    can_easy.place(x=0, y=0)
    img_easy = Image.open("easy.jpg")
    img_size_easy = img_easy.resize((600, 590))
    photo_easy = ImageTk.PhotoImage(img_size_easy)
    can_easy.create_image((220, 220), image=photo_easy)
    can_easy.create_text(250, 150,text=s, font=("algerian", 48, "bold italic"), fill='black')
    entry1 = tk.Entry(win, font=("Fixedsys", 28, "bold italic"), fg=fg, bg=bg, width=10)
    entry1.place(x=130,y=200)
    button1 = tk.Button(win, text="Submit", command=check, font=("Arial Black", 25, "bold"), fg="white", bg="black")
    button1.place(x=160,y=280)
    scorelabel = tk.Label(win, text="Your Score : " + str(score), font=("MS Sans Serif", 12, "bold"), bg="green",fg="white")
    scorelabel.place(x=180,y=380)
    win.mainloop()


def medium_start():
    global x

    if x == 0:
        start.destroy()
        x = x + 1
        pygame.mixer.music.load('medium.mp3')
        pygame.mixer.music.play(loops=1000)

    def check():
        global score
        global tries
        if entry1.get() == str1:
            showinfo("Congratulations", "You have guessed the word correctly")
            score += 10
            scorelabel.config(text="Your Score : " + str(score))
            resume()
        else:
            showerror("Sorry", "Please Try again , Tries Left:"+str(tries-1))
            tries -= 1
            if tries == 0:
                pygame.mixer.music.stop()
                win.destroy()
                lose = tk.Tk()
                lose.geometry("520x500+500+100")
                lose.resizable(0, 0)
                lose.title("Word Finder The Game")
                can = tk.Canvas(lose, width=600, height=600)
                can.place(x=0, y=0)
                img = Image.open("lose.jpg")
                img_size = img.resize((600, 590))
                photo = ImageTk.PhotoImage(img_size)
                can.create_image((220, 220), image=photo)
                can.create_text(250,150, text="SORRY YOU LOSE", font=("algerian", 36, "bold italic"),fill='white')
                can.create_text(250,200, text="TO MANY TRIES", font=("algerian", 28, "bold italic"),fill='white')
                can.create_text(250,250, text="YOUR SCORE: "+str(score),font=("algerian", 20, "bold italic"), fill='white')
                lose.mainloop()

    def resume():
        win.destroy()
        medium_start()

    # colors
    colors = ["#FFF8DC", "#FFEBCD", "#FFE4C4", "#FFDEAD", "#F5DEB3", "#DEB887", "#D2B48C", "#BC8F8F", "#F4A460",
              "#DAA520", "#B8860B"
        , "#CD853F", "#D2691E", "#8B4513", "#A0522D", "#A52A2A", "#800000", "#00FFFF", "#E0FFFF", "#AFEEEE", "#7FFFD4",
              "#40E0D0"
        , "#48D1CC", "#00CED1", "#F59EA0", "#4682B4", "#B0C4DE", "#ADD8E6", "#87CEFA", "#00BFFF", "#1E90FF"
        , "#6495ED", "#7B68EE", "#4169E1", "#0000FF", "#0000CD", "#00008B", "#000080", "#191970", "#ADFF24", "#FFE4E1",
              "#00FF00"
        , "#9370DB", "#EE82EE", "#F0E68C", "#FFDAB9", "#FFE4D5", "#FFFF00", "#FFD700", "#FFA500", "#FF4500", "#FF1493",
              "#FF4444"
        , "#FFA07A", "#00FF00", "#9ACD32", "#00FF74", "#20B2AA", "#98FB98"]
    fg_colors = ["#000000", "#FFFFFF", "#FFFAFA", "#F0FFF0", "#F5FFFA", "#F0FFFF", "#F0F8FF", "#F8F8FF", "#F5F5F5",
                 "#FFF5EE", "#F5F5DC", "#FFFAF0"
        , "#FDF5E6", "#FFFFF0", "#FAEBD7", "#FAF0E6", "#FFF0F5", "#FFE4E1", "#FFE4E1", "#DCDCDC", "#D3D3D3", "#C0C0C0",
                 "#A9A9A9", "#808080"
        , "#696969", "#778899", "#708090", "#2F4F4F"]
    words = ["adventure", "journey", "letters", "alphabet", "cupboard", "universe", "pigeon", "global", "everything",
             "basketball", "technology", "watermelon", "television", "friendship", "restaurant", "university", "gratitude"
             , "magnitude", "magnet", "japanese", "bridges", "politics", "ambulance", "fracture", "stacked", "trickery", "cricket"]
    word = random.randint(0, (len(words) - 1))
    str1 = words[word]
    bg = choice(colors)
    fg = choice(fg_colors)
    s = ''.join(random.sample(str1, len(str1)))
    win = tk.Tk()
    win.geometry("520x500+500+100")
    win.resizable(0, 0)
    win.title("Jumble Word Game")
    can_medium = tk.Canvas(win, width=600, height=600)
    can_medium.place(x=0, y=0)
    img_medium = Image.open("medium.jpg")
    img_size_medium = img_medium.resize((600, 590))
    photo_medium = ImageTk.PhotoImage(img_size_medium)
    can_medium.create_image((220, 260), image=photo_medium)
    can_medium.create_text(250, 150,text=s, font=("algerian", 48, "bold italic"), fill='black')
    entry1 = tk.Entry(win, font=("Fixedsys", 28, "bold italic"), fg=fg, bg=bg, width=10)
    entry1.place(x=150, y=200)
    button1 = tk.Button(win, text="Submit", command=check, font=("Arial Black", 25, "bold"), fg="white", bg="black")
    button1.place(x=180, y=280)
    scorelabel = tk.Label(win, text="Your Score : " + str(score), font=("MS Sans Serif", 12, "bold"), bg="green",fg="white")
    scorelabel.place(x=180, y=380)
    win.mainloop()


def hard_start():
    global x

    if x == 0:
        start.destroy()
        x = x + 1
        pygame.mixer.music.load('hard.mp3')
        pygame.mixer.music.play(loops=1000)

    def check():
        global score
        global tries
        if entry1.get() == str1:
            showinfo("Congratulations", "You have guessed the word correctly")
            score += 10
            scorelabel.config(text="Your Score : " + str(score))
            resume()
        else:
            showerror("Sorry", "Please Try again , Tries Left:"+ str(tries-1))
            tries -= 1
            if tries == 0:
                pygame.mixer.music.stop()
                win.destroy()
                lose = tk.Tk()
                lose.geometry("520x500+500+100")
                lose.resizable(0, 0)
                lose.title("Word Finder The Game")
                can = tk.Canvas(lose, width=600, height=600)
                can.place(x=0, y=0)
                img = Image.open("lose.jpg")
                img_size = img.resize((600, 590))
                photo = ImageTk.PhotoImage(img_size)
                can.create_image((220, 220), image=photo)
                can.create_text(250,150, text="SORRY YOU LOSE", font=("algerian", 36, "bold italic"),fill='white')
                can.create_text(250,200, text="TO MANY TRIES", font=("algerian", 28, "bold italic"),fill='white')
                can.create_text(250,250, text="YOUR SCORE: "+str(score),font=("algerian", 20, "bold italic"), fill='white')
                lose.mainloop()

    def resume():
        win.destroy()
        hard_start()

    # colors
    colors = ["#FFF8DC", "#FFEBCD", "#FFE4C4", "#FFDEAD", "#F5DEB3", "#DEB887", "#D2B48C", "#BC8F8F", "#F4A460",
              "#DAA520", "#B8860B"
        , "#CD853F", "#D2691E", "#8B4513", "#A0522D", "#A52A2A", "#800000", "#00FFFF", "#E0FFFF", "#AFEEEE", "#7FFFD4",
              "#40E0D0"
        , "#48D1CC", "#00CED1", "#F59EA0", "#4682B4", "#B0C4DE", "#ADD8E6", "#87CEFA", "#00BFFF", "#1E90FF"
        , "#6495ED", "#7B68EE", "#4169E1", "#0000FF", "#0000CD", "#00008B", "#000080", "#191970", "#ADFF24", "#FFE4E1",
              "#00FF00"
        , "#9370DB", "#EE82EE", "#F0E68C", "#FFDAB9", "#FFE4D5", "#FFFF00", "#FFD700", "#FFA500", "#FF4500", "#FF1493",
              "#FF4444"
        , "#FFC0CV", "#FFA07A", "#00FF00", "#9ACD32", "#00FF74", "#20B2AA", "#98FB98"]
    fg_colors = ["#000000", "#FFFFFF", "#FFFAFA", "#F0FFF0", "#F5FFFA", "#F0FFFF", "#F0F8FF", "#F8F8FF", "#F5F5F5",
                 "#FFF5EE", "#F5F5DC", "#FFFAF0"
        , "#FDF5E6", "#FFFFF0", "#FAEBD7", "#FAF0E6", "#FFF0F5", "#FFE4E1", "#FFE4E1", "#DCDCDC", "#D3D3D3", "#C0C0C0",
                 "#A9A9A9", "#808080"
        , "#696969", "#778899", "#708090", "#2F4F4F"]
    words = ["strawberry", "application", "abbreviation", "commitments", "classification", "astronomical", "historical",
             "information", "personality", "subtraction", "anniversary", "forgiveness", "electricity",
             "celebration", "celebrity", "imagination", "photography", "responsible", "football", "basketball"]
    word = random.randint(0, (len(words) - 1))
    str1 = words[word]
    bg = choice(colors)
    fg = choice(fg_colors)
    s = ''.join(random.sample(str1, len(str1)))
    win = tk.Tk()
    win.geometry("520x500+500+100")
    win.resizable(0, 0)
    win.title("Jumble Word Game")
    can_hard = tk.Canvas(win, width=600, height=600)
    can_hard.place(x=0, y=0)
    img_hard = Image.open("hard.jpg")
    img_size_hard = img_hard.resize((600, 590))
    photo_hard = ImageTk.PhotoImage(img_size_hard)
    can_hard.create_image((220, 220), image=photo_hard)
    can_hard.create_text(250, 150,text=s, font=("algerian", 48, "bold italic"), fill='white')
    entry1 = tk.Entry(win, font=("Fixedsys", 28, "bold italic"), fg=fg, bg=bg, width=10)
    entry1.place(x=150, y=200)
    button1 = tk.Button(win, text="Submit", command=check, font=("Arial Black", 25, "bold"), fg="white", bg="black")
    button1.place(x=180, y=280)
    scorelabel = tk.Label(win, text="Your Score : " + str(score), font=("MS Sans Serif", 12, "bold"), bg="green",fg="white")
    scorelabel.place(x=180, y=380)
    win.mainloop()


# Main Page
start = tk.Tk()
start.geometry("520x500+500+100")
start.resizable(0, 0)
start.title("Word Finder The Game")
can = tk.Canvas(start, width=600, height=600)
can.place(x=0, y=0)
img = Image.open("main.jpg")
img_size = img.resize((600, 590))
photo = ImageTk.PhotoImage(img_size)
can.create_image((220, 220), image=photo)

tk.Button(start, text="Easy", bg="#D3AA6D", fg="#75531F", font=("Forte", 25, "bold italic"), relief=tk.RAISED,
          anchor='center', width=8, activebackground="white", activeforeground="green", command=easy_start).place(x=50,y=125)
tk.Button(start, text="Medium", bg="#D3AA6D", fg="#75531F", font=("Forte", 25, "bold italic"), relief=tk.RAISED,
          anchor='center', width=8, activebackground="white", activeforeground="#FFD800", command=medium_start).place(x=320,y=125)
tk.Button(start, text="Hard", bg="#D3AA6D", fg="#75531F", font=("Forte", 25, "bold italic"), relief=tk.RAISED,
          anchor='center', width=8, activebackground="white", activeforeground="red", command=hard_start).place(x=50,y=250)
tk.Button(start, text="QUIT", bg="#D3AA6D", fg="#75531F", font=("Forte", 25, "bold bold"), relief=tk.RAISED,
          anchor='center', width=8, activebackground="maroon", activeforeground="blue", command=exit).place(x=320,y=250)
tk.Label(start,text="WORD JUMBLE", bg="red", fg="white", font=("Trebuchet MS", 48, "bold")).place(x=50, y=180)
start.mainloop()
