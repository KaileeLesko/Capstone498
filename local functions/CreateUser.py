import sqlite3
conn = sqlite3.connect('ColorCoordinator.db')
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox




window= tk.Tk()

window.geometry("400x150")
window.title("Color  Coordinator- Create New User")

def submit():
    conn = sqlite3.connect('ColorCoordinator.db')
    c = conn.cursor()
    c.execute("select*, oid FROM users")
    records = c.fetchall()
    users = records

    conn = sqlite3.connect('ColorCoordinator.db')

    c = conn.cursor()
    entry= False
    for i in range(0, len(users)):
        if  f_username.get() in users[i]:
            entry = True

    #insert into table

    if (entry== False):
        c.execute("INSERT INTO users  Values(:username,:first_name,:last_name,:password)",
                  {
                      'username':f_username.get(),
                      'first_name': f_name.get(),
                      "last_name": f_last_name.get(),
                      "password": f_password.get() } )

        c.execute("select*, oid FROM users")
        records = c.fetchall()
        users = records
        f_username.delete(0,END)
        f_name.delete(0,END)
        f_last_name.delete(0,END)
        f_password.delete(0,END)
    else:
        messagebox.showerror("ERROR", "This username is already in use")


# c.execute("""CREATE TABLE users(
#     username text,
#     first_name text,
#     last_name text,
#     password text
#           )""")

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


submit = Button(window, text= "Create",command= submit)
submit.grid(row=5, column=1,  columnspan= 2)


f_username= Entry(window)
f_username.grid(row=1, column= 1)




c= conn.cursor()


conn.commit()

conn.close()



mainloop()