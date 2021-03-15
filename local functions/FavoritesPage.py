from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image



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

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT,
                fill=Y)

mylist = Listbox(root,
                 yscrollcommand=scroll_bar.set)
img= PhotoImage(file="img1.png")
sampleColors = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
for i in range(0, len(sampleColors)):
    text= "HELLO", i
    mylist.insert(i,text)


mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()