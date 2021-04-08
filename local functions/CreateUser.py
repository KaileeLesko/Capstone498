import sqlite3
conn = sqlite3.connect('ColorCoordinator.db')
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pymysql
import re
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'



window= tk.Tk()

window.geometry("400x150")
window.title("Color  Coordinator- Create New User")

def submit():
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee', password= "Eeliak99.", database="capstone")
    c = conn.cursor()
    sql = "SELECT * FROM `users`"
    c.execute(sql)
    records = c.fetchall()
    users = records
    entry= False
    for i in range(0, len(users)):
        if  f_username.get() in users[i]:
            entry = True

    #insert into table

    if (entry== False):
        if (re.search(regex,f_username.get())):

                conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                                       password="Eeliak99.", database="capstone")

                c = conn.cursor()
                sql = "INSERT INTO `users` (`username`, `first_name`, `last_name`, `password`) VALUES (%s, %s, %s, %s)"
                c.execute(sql, (f_username.get(),f_name.get(), f_last_name.get(), f_password.get()))
                conn.commit()
                sql = "SELECT * FROM `users`"
                c.execute(sql)
                result = c.fetchall()
                user= result
                f_username.delete(0,END)
                f_name.delete(0,END)
                f_last_name.delete(0,END)
                f_password.delete(0,END)

                messagebox.showinfo("Success!", "Your account has been created!")
                window.destroy()
        else:
            messagebox.showerror("ERROR", "This is not a valid email, the window will now close")
            window.destroy()
    else:
        messagebox.showerror("ERROR", "This username is already in use")

FLabel = Label(window, text= "Create a new account: ")
FLabel.grid(row=0, column= 1, columnspan= 2)
f_username= Entry(window)
f_username.grid(row=1, column= 1)

L_username= Label(window, text= "ENTER YOUR EMAIL HERE")
L_username.grid(row=1, column= 0)

f_name= Entry(window)
f_name.grid(row=2, column= 1)


L_name= Label(window, text= "ENTER YOUR NAME")
L_name.grid(row=2, column= 0)


f_last_name= Entry(window)
f_last_name.grid(row=3, column= 1)


L_username= Label(window, text= "ENTER YOUR LAST NAME HERE")
L_username.grid(row=3, column= 0)


f_password= Entry(window)
f_password.grid(row=4, column= 1)


L_password= Label(window, text= "ENTER A PASSOWORD HERE")
L_password.grid(row=4, column= 0)


submit = Button(window, text= "Create",command=  submit)
submit.grid(row=5, column=1,  columnspan= 2)


f_username= Entry(window)
f_username.grid(row=1, column= 1)




c= conn.cursor()


conn.commit()

conn.close()



mainloop()