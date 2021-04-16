from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image
from loadmenu import e1
import pymysql

#
#
# master = Tk()
#
# master.title("Color  Coordinator")
#
# w = Scrollbar ( master )
# w.pack()
# img= PhotoImage(file="img1.png")
# sampleColors = [1,2,3,4,5,6,7,8,9]
#
# for i in range(0, len(sampleColors)):
#     image=Label(master, text="Upload File", image=img)
#     image.pack()
#
#
# mainloop()


root = Tk()

root.title("Color  Coordinator")
w = Label(root, text='Favorites',
          font="50")
favorites=[]
w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT,
                fill=Y)

mylist = Listbox(root,
                 yscrollcommand=scroll_bar.set)
img= PhotoImage(file="../build/Images needed to Run/img1.png")
conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                               password="Eeliak99.", database="capstone")

c = conn.cursor()
sql = "INSERT INTO `favorites` (`username`, `image`) VALUES (%s, %s)"
c.execute(sql, (e1.get(), img))
conn.commit()
sql = "SELECT * FROM `favorites`"
c.execute(sql)
result = c.fetchall()
favorites= result

sampleColors = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
for i in range(0, len(sampleColors)):
    text= "HELLO", i
    mylist.insert(i,text)


mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()