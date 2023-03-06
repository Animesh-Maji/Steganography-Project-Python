from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

#Backend Code

def openImage():
    global f
    f = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All file", "*.txt")))
    img = Image.open(f)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width= 250, height=250)
    lbl.image = img

def saveImage():
    secret.save("secret.png")

def hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(f), message)
    
def show():
    reveal_msg = lsb.reveal(f)
    text1.delete(1.0, END)
    text1.insert(END, reveal_msg)


root = Tk()
root.title("Steganography project")
root.geometry("700x500+300+80")
root.resizable(False, False)
root.configure(bg="#65cfc4")

# setting the icon for the app
icon = PhotoImage(file='.\\assets\\appIcon.png')        #icon path
root.iconphoto(False, icon)

# setting the heading
topImg = Image.open(".\\assets\\topIcon.png")
resize_img = topImg.resize((80, 80))
img = ImageTk.PhotoImage(resize_img)
Label(image=img, bg="#65cfc4").place(x=-10, y=-10)

Label(root, text="Hidden Text", bg="#65cfc4", fg="#fff", font="arial 25 bold").place(x=70, y=3)

# First Frame

frame1 = Frame(root, bd=3, bg="#000", height=280, width=340, relief=GROOVE)
frame1.place(x=10, y=80)

lbl = Label(frame1, bg="#000")
lbl.place(x=40, y=10)

# Second Frame

frame2 = Frame(root, bd=3, bg="#282828", height=280, width=340)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 20", bg="#282828", fg="#fff", relief=FLAT, wrap=WORD)
text1.place(x=7, y=7, width=320, height=295)

text_Scrollbar = Scrollbar(frame2)
text_Scrollbar.place(x=320, y=-3, height=300)
text_Scrollbar.configure(command=text1.yview)
text1.configure(yscrollcommand=text_Scrollbar.set)

# Third Frame

frame3 = Frame(root, bd=3, bg="#65cfc4", width=340, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=openImage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=saveImage).place(x=180, y=30)
Label(frame3, text="Process Image File...", bg="#65cfc4", fg="#000", font="arial 10 bold").place(x=20, y=5)

# Fourth Frame 

frame4 = Frame(root, bd=3, bg="#65cfc4", width=340, height=100, relief=GROOVE)
frame4.place(x=350, y=370)

Button(frame4, text="Hide Text", width=10, height=2, font="arial 14 bold", command=hide).place(x=20, y=30)
Button(frame4, text="Show Text", width=10, height=2, font="arial 14 bold", command=show).place(x=180, y=30)
Label(frame4, text="Encryption/Decryption...", bg="#65cfc4", fg="#000", font="arial 10 bold").place(x=20, y=5)


root.mainloop()
