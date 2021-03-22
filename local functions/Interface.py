from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from analagous import analagous
from RetrieveColorFromPhoto import colorFromPhoto
import os
import pymysql
import CreateMergedImage
from tkinter import messagebox
from TwitterBot import execute
import loadmenu
global favorites
global filename
from Monochrome import monochrome
from complimentary import comp
from PIL import Image, ImageTk
from SplitComplimentary import splitComplementary
from Tetriadic import tetradic
from CombinationFunctions import *
from Triadic import Triadic
from tkinter import filedialog
from tkinter import colorchooser

global c1
global c2

global printedcolors
darkmode = True
global isDarkMode
from ColorReturners import Blue

global mode
mode = True
# refereced tutorial https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
isDarkMode = False
# creating main tkinter window/toplevel
master = Tk()
master.title("Color  Coordinator")


# functions for calls

def changeColorSqures():
    if c1.instate(['selected']):
        patternchoosen = "cool colors only"

        var.set(0)
    if c2.instate(['selected']):
        patternchoosen = "warm colors only"
        var1.set(0)

    global mode
    global mycolors

    if mode == True:
        global selectedColor

        printedcolors = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff']
        patternTypes = ['Random', 'Monochrome',
                        'Complimentary',
                        'split complimentary',
                        'triadic']
        if (hexEntry.get() != ""):
            selectedColor = hexEntry.get()
            if selectedColor[0] != '#':
                messagebox.showerror("ERROR", "Hex Code must start with #")
                if (int(str(selectedColor), 16)) > 16777216:
                    messagebox.showerror("ERROR", "Invalid Hex Code")
            if (int(str(selectedColor)[1:], 16)) > 16777216:
                messagebox.showerror("ERROR", "Invalid Hex Code")

            # selectedColor= selectedColor[1]

        # if (patternchoosen.get() == "" && !c2.instate(['selected']) :
        #     messagebox.showerror("ERROR", "Please Select a Color Pattern Type")
        import CoolColors
        import WarmColors
        if isinstance(patternchoosen, str):
            if (patternchoosen == 'cool colors only'):
                printedcolors = CoolColors.coolColors()
            if (patternchoosen == 'warm colors only'):
                printedcolors = WarmColors.WarmColors()
        else:
            selectedColor = ""
            if (patternchoosen.get() == 'Random'):
                pattern = random.choice(patternTypes)
            else:
                pattern = patternchoosen.get()
            import WarmColors
            if (pattern == "Monochrome"):
                printedcolors = monochrome(selectedColor) + ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff',
                                                             '#ffffff']

            if (pattern == "Complimentary"):
                printedcolors = comp(selectedColor) + ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff']
            if (pattern == 'split complimentary'):
                printedcolors = splitComplementary(selectedColor) + ['#ffffff', '#ffffff', '#ffffff', '#ffffff',
                                                                     '#ffffff', '#ffffff']
            if (pattern == 'tetradic'):
                printedcolors = tetradic(selectedColor) + ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff',
                                                           '#ffffff']
            if (pattern == 'triadic'):
                printedcolors = Triadic(selectedColor) + ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff',
                                                          '#ffffff']
            if (pattern == 'analagous'):
                printedcolors = analagous(selectedColor) + ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff',
                                                            '#ffffff']
            global mycolors
            mycolors = printedcolors



    else:
        global fileimage

        printedcolors = colorFromPhoto(fileimage)
    mycolors = printedcolors
    color1 = Canvas(master, width=250, height=200)
    color1.create_rectangle(0, 0, 200, 200, fill=printedcolors[0], outline=printedcolors[0])
    color1.grid(row=3, column=0, sticky=W)

    color2 = Canvas(master, width=250, height=200)
    color2.create_rectangle(0, 0, 200, 200, fill=printedcolors[1], outline=printedcolors[1])
    color2.grid(row=3, column=1, sticky=W)

    color3 = Canvas(master, width=250, height=200)
    color3.create_rectangle(0, 0, 200, 200, fill=printedcolors[2], outline=printedcolors[2])
    color3.grid(row=3, column=2, sticky=W)

    color4 = Canvas(master, width=250, height=200)
    color4.create_rectangle(0, 0, 200, 200, fill=printedcolors[3], outline=printedcolors[3])
    color4.grid(row=3, column=3, sticky=W)

    color5 = Canvas(master, width=250, height=200)
    color5.create_rectangle(0, 0, 200, 200, fill=printedcolors[4], outline=printedcolors[4])
    color5.grid(row=3, column=4, sticky=W)


    color6 = Canvas(master, width=250, height=200)
    color6.create_rectangle(0, 0, 200, 200, fill=printedcolors[5], outline=printedcolors[5])
    color6.grid(row=3, column=5, sticky=W)
    selectedColor = ""
    hexEntry.delete(0, END)
    hexEntry.insert(0, "")
    l3.config(text=printedcolors[0])
    l4.config(text=printedcolors[1])
    L5.config(text=printedcolors[2])
    L6.config(text=printedcolors[3])
    L7.config(text=printedcolors[4])
    L8.config(text=printedcolors[5])


# color1.config(fill=printedcolors[0])
printedcolors = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff']


def convertToBinaryData():
    # Convert digital data to binary format
    with open("myImage.png", 'rb') as file:
        binaryData = file
    return binaryData


# this will create a label widget
var = IntVar()
var1 = IntVar()
l1 = Label(master, text=" 1) Choose a color pattern type: ", font=1000)
c1 = ttk.Checkbutton(master, text='cool colors ', command=changeColorSqures, variable=var)
c2 = ttk.Checkbutton(master, text='warm colors', command=changeColorSqures, variable=var1)
lKailee = Label(master, text="OR pick one of these:")
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
rgb = '#%02X%02X%02X' % (r, g, b)
hexEntry = Entry(master, text=rgb)
c1.grid(row=1, column=1, sticky=W, pady=2)
c2.grid(row=1, column=2, sticky=W, pady=2)
lKailee.grid(row=1, column=0, sticky=W, pady=2)
hexLabel = Label(master, text=" 2) enter your own hex code Here:", font=880)
hexLabel.grid(row=2, column=0, sticky=W, pady=2)
hexEntry.grid(row=2, column=1, sticky=W, pady=2)

l1.grid(row=0, column=0, sticky=W, pady=2)


def switchModes():
    master.config(background="#2c2f33")
    global l3, l4, L5, L6, L7, L8
    l1.config(background="#2c2f33", foreground="#99aab5")
    l2.config(background="#2c2f33", foreground="#99aab5")
    l3.config(background="#2c2f33", foreground="#99aab5")
    l4.config(background="#2c2f33", foreground="#99aab5")
    L5.config(background="#2c2f33", foreground="#99aab5")
    L7.config(background="#2c2f33", foreground="#99aab5")
    L6.config(background="#2c2f33", foreground="#99aab5")
    L8.config(background="#2c2f33", foreground="#99aab5")
    global photoslice

    photoslice.destroy()


global fileimage


def lightModes():
    master.config(background="#ffffff")
    global l1
    l1.config(background="#ffffff", foreground="#000000")
    l3.config(background="#ffffff", foreground="#000000")
    l4.config(background="#ffffff", foreground="#000000")
    L5.config(background="#ffffff", foreground="#000000")
    L7.config(background="#ffffff", foreground="#000000")
    L6.config(background="#ffffff", foreground="#000000")
    L8.config(background="#ffffff", foreground="#000000")
    global photoslice
    photoslice.destroy()
    image = Image.open(r"C:\Users\kailuu\Pictures\wheelofgod.png")
    photo = ImageTk.PhotoImage(image)
    photoslice = Label(master, image=photo)
    photoslice.image = photo
    photoslice = Button(master, image=photo, command=colorpicker)
    photoslice.grid(row=0, column=2,
                    columnspan=2, rowspan=2, padx=5, pady=5)


def helpWindow():
    global item1
    item1 = Tk()
    item1.wm_title("Window")

    l90 = Label(item1,
                text="To generate a pallete from photo \nclick the text box and then the file button. \nTo Generate a Pallete from a pattern you\nmust first select a pattern \nand color or else nothing will\nload besides white squares")
    l90.grid(row=0, column=0)
    b1.grid(row=1, column=0)


def goToFaves():
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
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")
    checker = conn.cursor()
    sql = "INSERT INTO `favoriteImages` (`username`, `image`) VALUES (%s, %s)"
    checker.execute("SELECT * FROM favoriteImages")
    record = checker.fetchall()
    print(type(record))
    favorites = []
    for i in record:
        favorites.append(i[1])
    import base64
    import io
    #
    for i in range(0, len(favorites)):
        if os.path.exists('hello.png'):
            os.remove('hello.png')
        decodeit = open('hello.png', 'wb')

        decodeit.write(base64.b64decode((favorites[i])))
        decodeit.close()
        img = Image.open('hello.png')
        img.show()

        #
       #  img= Image.open((base64.b64decode((favorites[i]))))
       #  img.show()
       #  #stream = io.BytesIO(favorites[i])
       # # img = Image.open(0x2A5783146A0).convert("RGBA")
       #  # stream.close()
       #  #image.show()
       #  print(favorites[i].size)






def acknowledgement():
    root = Tk()

    root.title("Color  Coordinator")
    w = Label(root, text='thanks to everyone who helped me stay sane during development (Eric)',
              font="50")

    w.pack()




menubar = Menu(master)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Settings', menu=file)
menubar.add_cascade(label='Favorites', command=goToFaves)
menubar.add_cascade(label='how to', command=helpWindow)
menubar.add_cascade(label="acknowledgement", command=acknowledgement)

submenu = Menu(file)
submenu.add_command(label="Dark Mode", command=switchModes)
submenu.add_command(label="Light Mode", command=lightModes)
file.add_cascade(label='Visual Settings', menu=submenu, underline=0)

# mode.add_command(label ='Dark Mode', command =switchModes)
master.config(menu=menubar)
patternchoosen = ttk.Combobox(master, width=27, )
patternchoosen['values'] = ('Random', 'Monochrome',
                            'Complimentary',
                            'split complimentary',
                            'triadic',
                            'tetradic', 'analagous',)

# this will arrange entry widgets
patternchoosen.grid(row=0, column=1, pady=2)

# checkbutton widget
image = Image.open(r"C:\Users\kailuu\Pictures\wheelofgod.png")
photo = ImageTk.PhotoImage(image)


def colorpicker():
    color_code = colorchooser.askcolor(title="Choose color")

    global selectedColor
    selectedColor = color_code
    hexEntry.delete(0, END)
    hexEntry.insert(0, selectedColor[1])

    l1.grid(row=0, column=0, sticky=W, pady=2)


photoslice = Button(master, text="Upload File", image=photo, command=colorpicker)
photoslice.grid(row=0, column=2,
                columnspan=2, rowspan=2, padx=5, pady=5)

# img = PhotoImage(file=r"C:\Users\kailuu\Pictures\wheelofgod.png")
# img1 = img.subsample(2, 2)
#
# # setting image with the help of label
# photo= Label(master, image=img1).grid(row=0, column=2,
#                           columnspan=2, rowspan=2, padx=5, pady=5)
my_text = "click here to pick colors from a photo: "


def switchInputForPhoto():
    global my_text
    if c.cget("text") == "click here to pick colors from a photo: ":
        global mode
        mode = False
        my_text = "click her to pick colors from photo"
        c.config(text=my_text)
        global photoslice
        photoslice.destroy()
        global uploadButton
        global l1
        global hexEntry
        global hexLabel
        hexEntry.destroy()
        hexLabel.destroy()
        global l2
        l1.destroy()
        global patternchoosen
        patternchoosen.destroy()
        image = Image.open(r"C:\Users\kailuu\Pictures\downloadphoto.png")
        photo = ImageTk.PhotoImage(image)
        photoslice = Label(master, image=photo)
        photoslice.image = photo
        photoslice = Button(master, image=photo, command=uploadfile)
        photoslice.grid(row=0, column=2,
                        columnspan=2, rowspan=2, padx=5, pady=5)

    else:
        my_text = "click here to pick colors from a photo: "
        c.config(text=my_text)
        image = Image.open(r"C:\Users\kailuu\Pictures\wheelofgod.png")
        photo = ImageTk.PhotoImage(image)
        photoslice = Label(master, image=photo)
        photoslice.image = photo
        photoslice = Button(master, image=photo, command=colorpicker)
        photoslice.grid(row=0, column=2,
                        columnspan=2, rowspan=2, padx=5, pady=5)
        l1 = Label(master, text="1) color pattern type: ", font=880)
        mode = True
        l1.grid(row=0, column=0, sticky=W, pady=2)
        hexEntry = Entry(master, text=rgb)
        hexLabel = Label(master, text="enter your own hex code Here:", font=880)
        hexLabel.grid(row=2, column=0, sticky=W, pady=2)
        hexEntry.grid(row=2, column=1, sticky=W, pady=2)

        patternchoosen = ttk.Combobox(master, width=27, )
        patternchoosen['values'] = ('Random', 'Monochrome',
                                    'Complimentary',
                                    'split complimentary',
                                    'triadic',
                                    'tetradic', 'analagous',)

        # this will arrange entry widgets                         
        patternchoosen.grid(row=0, column=1, pady=2)

        # button widget


def uploadfile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File"
                                          )
    name, extension = os.path.splitext(filename)
    print(extension)
    if (".PNG") != extension:
        messagebox.showerror("ERROR", "File must be a .PNG type")
    else:
        image = Image.open(filename)
        global fileimage
        fileimage = image.resize((200, 200))
        photo = ImageTk.PhotoImage(fileimage)

        photoslice = Label(master, image=photo)
        photoslice.image = photo
        photoslice = Button(master, image=photo, command=uploadfile)
        photoslice.grid(row=0, column=2,
                        columnspan=2, rowspan=1, padx=5, pady=5)


color1 = Canvas(master, width=250, height=200)
color1.create_rectangle(0, 0, 200, 200, fill=printedcolors[0], outline=printedcolors[0])
color1.grid(row=3, column=0, sticky=W)

color2 = Canvas(master, width=250, height=200)
color2.create_rectangle(0, 0, 200, 200, fill=printedcolors[1], outline=printedcolors[1])
color2.grid(row=3, column=1, sticky=W)

color3 = Canvas(master, width=250, height=200)
color3.create_rectangle(0, 0, 200, 200, fill=printedcolors[2], outline=printedcolors[2])
color3.grid(row=3, column=2, sticky=W)

color4 = Canvas(master, width=250, height=200)
color4.create_rectangle(0, 0, 200, 200, fill=printedcolors[3], outline=printedcolors[3])
color4.grid(row=3, column=3, sticky=W)

color5 = Canvas(master, width=250, height=200)
color5.create_rectangle(0, 0, 200, 200, fill=printedcolors[4], outline=printedcolors[4])
color5.grid(row=3, column=4, sticky=W)

# master.configure(background='#2c2f33')

color6 = Canvas(master, width=250, height=200)
color6.create_rectangle(0, 0, 200, 200, fill=printedcolors[5], outline=printedcolors[5])
color6.grid(row=3, column=5, sticky=W)

l3 = Label(master, font=1000, text=str(printedcolors[0]))
l3.grid(row=4, column=0, sticky=W)
l4 = Label(master, font=1000, text=str(printedcolors[1]))
l4.grid(row=4, column=1, sticky=W)
L5 = Label(master, font=1000, text=str(printedcolors[2]))
L5.grid(row=4, column=2, sticky=W)
L6 = Label(master, font=1000, text=str(printedcolors[3]))
L6.grid(row=4, column=3, sticky=W)
L7 = Label(master, font=1000, text=str(printedcolors[4]))
L7.grid(row=4, column=4, sticky=W)
L8 = Label(master, font=1000, text=str(printedcolors[5]))
L8.grid(row=4, column=5, sticky=W)


def post():
    global item2
    item2 = Tk()
    item2.wm_title("Window")
    item2.geometry("200x200")
    l = Label(item2, text="What Text do you want your tweet to say?")
    global e1
    e1 = Entry(item2)
    e1.grid(row=1, column=0)
    l.grid(row=0, column=0)
    b = Button(item2, text="Submit", command=executer)
    b.grid(row=2, column=0)
    b2.grid(row=3, column=0)


def executer():
    execute(mycolors[0], mycolors[1], mycolors[2], mycolors[3], mycolors[4], mycolors[5], e1.get())
    item2.destroy()


uploadButton = Button(master, text="Upload File", image=photo, command=uploadfile)


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    return f





global favoritedImages
favoritedImages = []


def addToFaves():
    # CHECK
    import Constants
    print("ENTRY" ,Constants.currentUser)
    print(mycolors[2])

    CreateMergedImage.create(mycolors[0], mycolors[1], mycolors[2], mycolors[3], mycolors[4], mycolors[5])
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")
    #imager = Image.open("myImage.png")
    img = Image.open("myImage.PNG")
    c = conn.cursor()
    import base64
    converted_string = base64.b64encode(open("myImage.png", "rb").read())
    sql = "INSERT INTO `favoriteImages` (`username`, `image`) VALUES (%s, %s)"
    c.execute(sql, (Constants.currentUser, converted_string))
    conn.commit()
    c.execute("SELECT * FROM favoriteImages where username="+ str(Constants.currentUser))
    record = c.fetchall()
    print(type(record))

    favorites = record
    print(str(favorites))




b1 = Button(master, text="Generate Pallete", command=changeColorSqures)

b2 = Button(master, text="Post to Twitter", command=post)
b3 = Button(master, text="Add to Favorites", command=addToFaves)
c = ttk.Checkbutton(master, text='click here to pick colors from a photo: ', command=switchInputForPhoto)

# arranging button widgets
b1.grid(row=2, column=2, sticky=W)
b2.grid(row=2, column=3, sticky=W)
c.grid(row=2, column=5, sticky=W)
b1.grid(row=2, column=2, sticky=W)
b2.grid(row=2, column=3, sticky=W)
b3.grid(row=2, column=4, sticky=W)
b1.grid(row=2, column=2, sticky=W)
b2.grid(row=2, column=3, sticky=W)

master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)
master.grid_columnconfigure(2, weight=1)
master.grid_columnconfigure(3, weight=1)
master.grid_columnconfigure(4, weight=1)
master.grid_columnconfigure(5, weight=1)
master.grid_columnconfigure(6, weight=1)
master.grid_rowconfigure(0, weight=1)
master.grid_rowconfigure(1, weight=1)
master.grid_rowconfigure(2, weight=1)
master.grid_rowconfigure(3, weight=1)
master.grid_rowconfigure(4, weight=1)
master.grid_rowconfigure(5, weight=1)
master.grid_rowconfigure(6, weight=1)
master.grid_rowconfigure(7, weight=1)
master.grid_columnconfigure(6, weight=1)
master.grid_columnconfigure(7, weight=1)

# infinite loop which can be terminated
# by keyboard or mouse interrupt 
mainloop()
