from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql

master = Tk()
master.title("Color Coordinator Gallery")
global images

def getImages():
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")
    checker = conn.cursor()
    checker.execute("SELECT * FROM slideshow")
    images = checker.fetchall()

    return images[0]


image_label = Label(image= getImages())
image_label.grid(row=0, column=0, columnspan = 3)

back = Button(master, text = "<--", state= DISABLED)
forward = Button(master, text = "-->",  command=lambda:forward(2))
back.grid(row=1, column= 0)
forward.grid(roow=1, column=2)


def foward(imageNumber):
    global image_label
    global forward
    global back

    image_label.grid_forget()
    image_label= Label(images(imageNumber-1)(1))
    back= Button(master, text= "<--", command= lambda: back(imageNumber-1))
    if imageNumber == len(images):
        forward = Button(master, text= "-->", state= DISABLED)
    else:
        forward = Button(master, text="-->", command= lambda: forward(imageNumber+1))
    image_label.grid(row=0, column=0, columnspan= 3)
    back.grid(row=1, column =0)
    forward.grid(row=1, column =2)


def back(imageNumber):
    global image_label
    global forward
    global back

    image_label.grid_forget()
    image_label= Label(images(imageNumber-1)(1))
    forward= Button(master, text= "-->", command= lambda: back(imageNumber+1))
    if imageNumber == 1:
        back= Button(master, text= "<--", state= DISABLED)
    else:
        back = Button(master, text="<--", command= lambda: back(imageNumber-1))
    image_label.grid(row=0, column=0, columnspan= 3)
    back.grid(row=1, column =0)
    forward.grid(row=1, column =2)




mainloop()