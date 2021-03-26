from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from analagous import analagous
from Monochrome import monochrome
from complimentary import comp
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import pymysql


def launchnewuser():
    import CreateUser


global e1
global answer


def retrieveUser():
    print("DING DING")
    print("answer", answer)
    return answer


window = tk.Tk()

window.title("Color  Coordinator")

imager = Image.open(r"C:\Users\kailuu\Pictures\untitled_artwork.png")
photo = ImageTk.PhotoImage(imager)

photoslice = Label(window, image=photo)
photoslice.image = photo
photoslice.grid(row=0, column=2,
                columnspan=2, rowspan=2, padx=5, pady=5)


def launchWindow():
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")

    c = conn.cursor()
    c.execute("SELECT* FROM users")
    records = c.fetchall()
    users = records
    entry = False
    print(str(users))
    print("entries", users[0][0], users[0][3])
    global answer
    answer = e1.get()
    print(e1.get(), e2.get())
    for i in range(0, len(users)):
        if e1.get() in users[i]:
            if e2.get() in users[i]:
                entry = True
    if entry == False:
        messagebox.showerror("ERROR", "This password or Username is incorrect")

    if entry == True:
        window.destroy()




b1 = Button(window, text="Log in ", command=launchWindow)
b2 = Button(window, text="Create Account ", command=launchnewuser)
b2.grid(row=7, column=2, columnspan=2)
b1.grid(row=6, column=2, columnspan=2)
# entry widgets, used to take entry from user
e1 = Entry(window, text="username")
e1.insert(END, 'Username')
e2 = Entry(window)
e2.insert(END, 'Password')

# this will arrange entry widgets
e1.grid(row=2, column=2, columnspan=2)
e2.grid(row=3, column=2, columnspan=2)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)


mainloop()
