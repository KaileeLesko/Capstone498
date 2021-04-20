
import os
from PIL import  ImageTk
import PIL.Image
import sqlite3
conn = sqlite3.connect('ColorCoordinator.db')
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pymysql
import re
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def resource_path( relative_path):

    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def  submissionfield():
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")
    c = conn.cursor()
    sql = "SELECT * FROM `users`"
    c.execute(sql)
    records = c.fetchall()
    users = records
    entry = False
    for i in range(0, len(users)):
        if f_username.get() in users[i]:
            entry = True
    if (entry == False):
        if (len(f_password.get()) >= 6):
            if (f_name.get() != ""):
                if (f_last_name.get() != ""):
                    if (re.search(regex, f_username.get())):

                        conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                                               password="Eeliak99.", database="capstone")

                        c = conn.cursor()
                        sql = "INSERT INTO `users` (`username`, `first_name`, `last_name`, `password`) VALUES (%s, %s, %s, %s)"
                        c.execute(sql, (f_username.get(), f_name.get(), f_last_name.get(), f_password.get()))
                        conn.commit()
                        sql = "SELECT * FROM `users`"
                        c.execute(sql)
                        result = c.fetchall()
                        user = result
                        f_username.delete(0, END)
                        f_name.delete(0, END)
                        f_last_name.delete(0, END)
                        f_password.delete(0, END)

                        messagebox.showinfo("Success!", "Your account has been created!")
                        window.destroy()

                    else:
                        messagebox.showerror("ERROR", "This is not a valid email")
                else:
                    messagebox.showerror("ERROR", "Last name cannot be blank")
            else:
                messagebox.showerror("ERROR", "first name cannot be blank")
        else:
            messagebox.showerror("ERROR", "password must be 6 or more characters long")
    else:
        messagebox.showerror("ERROR", "This username is already in use")


def createWindow():
    global f_username, f_password, f_name, f_last_name, window
    userwindow = tk.Tk()

    userwindow.geometry("400x150")
    userwindow.title("Color  Coordinator- Create New User")
    FLabel = Label(userwindow, text= "Create a new account: ")
    FLabel.grid(row=0, column= 1, columnspan= 2)
    f_username= Entry(userwindow)
    f_username.grid(row=1, column= 1)

    L_username= Label(userwindow, text= "ENTER YOUR EMAIL HERE")
    L_username.grid(row=1, column= 0)

    f_name= Entry(userwindow)
    f_name.grid(row=2, column= 1)


    L_name= Label(userwindow, text= "ENTER YOUR NAME")
    L_name.grid(row=2, column= 0)


    f_last_name= Entry(userwindow)
    f_last_name.grid(row=3, column= 1)


    L_username= Label(userwindow, text= "ENTER YOUR LAST NAME HERE")
    L_username.grid(row=3, column= 0)


    f_password= Entry(userwindow)
    f_password.grid(row=4, column= 1)


    L_password= Label(userwindow, text= "ENTER A PASSOWORD HERE")
    L_password.grid(row=4, column= 0)


    submit = Button(userwindow, text= "Create",command=  submissionfield)
    submit.grid(row=5, column=1,  columnspan= 2)


    f_username= Entry(userwindow)
    f_username.grid(row=1, column= 1)






def launchnewuser():
    createWindow()


global e1
global answer


def retrieveUser():

    return answer


window = tk.Tk()
window.resizable(height=None, width=None)

window.title("Color  Coordinator")

TEST = PIL.Image.open(resource_path("Untitled_Artwork.png"))
photo = ImageTk.PhotoImage(TEST)

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

    global answer
    answer = e1.get()

    for i in range(0, len(users)):
        if e1.get() in users[i]:
            if e2.get() in users[i]:
                entry = True
    if entry == False:
        messagebox.showerror("ERROR", "This password or Username is incorrect")

    if entry == True:
        window.destroy()




b1 = Button(window, text="Log in ", command=launchWindow)
b2 = Button(window, text="Create Account ", command= launchnewuser)
b2.grid(row=7, column=2, columnspan=2)
b1.grid(row=6, column=2, columnspan=2)
# entry widgets, used to take entry from user
e1 = Entry(window, text="username")
e1.insert(END, 'Username')

e2 = Entry(window, text= "password",show="*")
e2.insert(END, 'Password')

e1.grid(row=2, column=2)
e2.grid(row=3, column=2)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)




mainloop()
