from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog
import os
import pymysql

master = Tk()
master.title("Submissionn field")

def submit():
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")
    checker = conn.cursor()
    checker.execute("SELECT * FROM slideshow")
    sql = "INSERT INTO `favoriteImages` (`username`, `image`, `title`) VALUES (%s, %s, %s)"
    checker.execute(sql, user, imageUploaded, uploadname.get())
    conn.close()

def click():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File"
                                          )
    name, extension = os.path.splitext(filename)
    if (".PNG") != extension:
        messagebox.showerror("ERROR", "File must be a .PNG type")
    else:
        image = Image.open(r"C:\Users\kailuu\Pictures\wheelofgod.png")
        global imageUploaded
        imageUplaoded = Image.open(filename)





uploader = Button(master, text= "upload file", command= click)
uploader.grid(row=0,column=1)
global uploadname
uploadname = Entry(master)
uploadname.grid(row =1, column = 2)
label = Label(master, text= "Enter the artwork's name here: ")
label.grid(row=1, column = 0)
sumbitButton= Button(master,text= "submit", command= submit())
sumbitButton.grid(row=2, column= 1)



mainloop()