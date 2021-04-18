import random
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
global favorites
global filename
from analagous import analagous
from RetrieveColorFromPhoto import colorFromPhoto
import os
import smtplib, ssl
import base64
import Constants
import pymysql
import CreateMergedImage
from tkinter import messagebox
from ausxillaryFunctions import lastsix, nextsix
from TwitterBot import execute
from Monochrome import monochrome
from complimentary import comp
from PIL import Image, ImageTk
from SplitComplimentary import splitComplementary
from Tetriadic import tetradic
from Triadic import Triadic
from tkinter import filedialog
from tkinter import colorchooser

#import to start



# refereced tutorial https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
class mainInterface:


    def __init__(self, master):
        from loadmenu import retrieveUser
        self.menubar = Menu(master)
        self.username= retrieveUser()
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Settings', menu=self.file)
        self.menubar.add_cascade(label='Favorites', command=  self.goToFaves)
        self.menubar.add_cascade(label='Upload to Gallery', command=self.createUpload)
        self.menubar.add_cascade(label='how to', command=self.helpWindow)
        self.menubar.add_cascade(label="acknowledgement", command=self.acknowledgement)
        self.submenu = Menu(self.file)
        self.filename= ""
        self.submenu.add_command(label="Dark Mode", command=self.switchModes)
        self.submenu.add_command(label="Light Mode", command=self.lightModes)
        self.file.add_cascade(label='Visual Settings', menu= self.submenu, underline=0)
        # mode.add_command(label ='Dark Mode', command =mainInterface.switchModes)
        master.config(menu=self.menubar)
        self.lastindex = 6
        self.encrypter= ""
        self.printedcolors = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff']
        self.one= Label(text= "no")
        self.two=Label(text= "no")
        self.three=Label(text= "no")
        self.four=Label(text= "no")
        self.five=Label(text= "no")
        self.six=Label(text= "no")
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.imageUplaoded=""
        self.b = random.randint(0, 255)
        self.rgb = '#%02X%02X%02X' % (self.r, self.g, self.b)

        self.var = IntVar()
        self.var1 = IntVar()
        self.l1 = Label(master, text=" 1) Choose a color pattern type: ")
        self.l1.grid(row=0, column=0, sticky=W, pady=2)

        self.c1 = ttk.Button(master, text='cool colors ', command=self.coolColors)
        self.c2 = ttk.Button(master, text='warm colors', command=self.warmColors)
        self.c1.grid(row=2, column=1, sticky=W, pady=2)
        self.c2.grid(row=2, column=2, sticky=W, pady=2)

        self.lKailee = Label(master, text="OR pick one of these:")
        self.lKailee.grid(row=2, column=0, sticky=W, pady=2)

        self.hexEntry = Entry(master, text="")
        self.hexEntry.grid(row=1, column=1, sticky=W, pady=2)
        self.user= Constants.setUser()
        self.hexLabel = Label(master, text=" 2) enter your own hex code Here:")
        self.hexLabel.grid(row=1, column=0, sticky=W, pady=2)

        self.mode = True
        self.isDarkMode = False
        self.favorite= ""


        self.patternchoosen = ttk.Combobox(master, width=27, )
        self.patternchoosen['values'] = ('Random', 'Monochrome',
                                    'Complimentary',
                                    'split complimentary',
                                    'triadic',
                                    'tetradic', 'analagous',)
        self.patternchoosen.grid(row=0, column=1, pady=2)


        self.image = Image.open(self.resource_path("wheelofgod.png"))
        self.photo = ImageTk.PhotoImage(self.image)

        self.my_text = "click here to pick colors from a photo: "



        self.photoslice = Button(master, text="Upload File", image=self.photo, command=self.colorpicker)
        self.photoslice.grid(row=0, column=2,
                        columnspan=2, rowspan=2, padx=5, pady=5)
        self.color1 = Canvas(master, width=250, height=200)

        self.color1.create_rectangle(0, 0, 200, 200, fill=self.printedcolors[0], outline=self.printedcolors[0])
        self.color1.grid(row=3, column=0, sticky=W)

        self.color2 = Canvas(master, width=250, height=200)
        self.color2.create_rectangle(0, 0, 200, 200, fill=self.printedcolors[1], outline=self.printedcolors[1])
        self.color2.grid(row=3, column=1, sticky=W)

        self.color3 = Canvas(master, width=250, height=200)
        self.color3.create_rectangle(0, 0, 200, 200, fill=self.printedcolors[2], outline=self.printedcolors[2])
        self.color3.grid(row=3, column=2, sticky=W)

        self.color4 = Canvas(master, width=250, height=200)
        self.color4.create_rectangle(0, 0, 200, 200, fill=self.printedcolors[3], outline=self.printedcolors[3])
        self.color4.grid(row=3, column=3, sticky=W)

        self.color5 = Canvas(master, width=250, height=200)
        self.color5.create_rectangle(0, 0, 200, 200, fill=self.printedcolors[4], outline=self.printedcolors[4])
        self.color5.grid(row=3, column=4, sticky=W)

        self.color6 = Canvas(master, width=250, height=200)
        self.color6.create_rectangle(0, 0, 200, 200, fill=self.printedcolors[5], outline=self.printedcolors[5])
        self.color6.grid(row=3, column=5, sticky=W)

        self.l3 = Label(master, font=1000, text=str(self.printedcolors[0]))
        self.l3.grid(row=4, column=0, sticky=W)

        self.l4 = Label(master, font=1000, text=str(self.printedcolors[1]))
        self.l4.grid(row=4, column=1, sticky=W)

        self.L5 = Label(master, font=1000, text=str(self.printedcolors[2]))
        self.L5.grid(row=4, column=2, sticky=W)

        self.L6 = Label(master, font=1000, text=str(self.printedcolors[3]))
        self.L6.grid(row=4, column=3, sticky=W)

        self.L7 = Label(master, font=1000, text=str(self.printedcolors[4]))
        self.L7.grid(row=4, column=4, sticky=W)

        self.L8 = Label(master, font=1000, text=str(self.printedcolors[5]))
        self.L8.grid(row=4, column=5, sticky=W)

        self.uploadButton = Button(master, text="Upload File", image=self.photo, command= self.uploadfile)

        self.favoritedImages = []
        ttk.Style().configure('green/black.TButton', foreground='green', background='black')
        self.b1 = Button(master,text="Generate Pallete", style='green/black.TButton', command=self.changeColorSqures)


        self.b1.grid(row=2, column=3, sticky=W)


        self.b2 = Button(master, text="Post to Twitter", command=self.post)
        self. b2.grid(row=2, column=4, sticky=W)

        self.b3 = Button(master, text="Add to Favorites", command=self.addToFaves)
        self.b3.grid(row=0, column=4, sticky=W)
        self.c = ttk.Checkbutton(master, text='click here to pick colors from a photo: ', command=self.switchInputForPhoto)
        self.c.grid(row=2, column=5, sticky=W)
        self.mycolors= self.printedcolors


    def colorfromphoto(self):
        printedcolors = colorFromPhoto(self.fileimage)
        self.mycolors = printedcolors
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
        self.hexEntry.delete(0, END)
        # self.hexEntry.se
        self.hexEntry.insert(0, "")
        self.l3.config(text=printedcolors[0])
        self.l4.config(text=printedcolors[1])
        self.L5.config(text=printedcolors[2])
        self.L6.config(text=printedcolors[3])
        self.L7.config(text=printedcolors[4])
        self.L8.config(text=printedcolors[5])
    def colorpicker(self):
        color_code = colorchooser.askcolor(title="Choose color")

        selectedColor = color_code
        self.hexEntry.delete(0, END)
        self.hexEntry.insert(0, selectedColor[1])

        self.l1.grid(row=0, column=0, sticky=W, pady=2)

    def goToFaves(self):
        global photo3, photo1, photo2, photo4, photo5, photo6
        global one, two, three, four, five, six
        rooter =Toplevel()

        rooter.title("Color  Coordinator")
        w = Label(rooter, text='Favorites',
                  font="50")
        w.grid(row=0, column=1,columnspan=2 )
        conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                               password="Eeliak99.", database="capstone")
        checker = conn.cursor()
        CreateMergedImage.createwhite()
        sql = "INSERT INTO `favoriteImages` (`username`, `image`) VALUES (%s, %s)"
        checker.execute("SELECT * FROM favoriteImages")
        record = checker.fetchall()
        self.favorite = record
        print("record", record)
        print("lnght of f" ,len(self.favorite))
        self.favorites=[]
        for i in range(0,len(self.favorite)):
            if self.favorite[i][0] == self.user:
                self.favorites.append(self.favorite[i])
                print("done this")

        print("LEN",len(self.favorites))
        self.lastindex= 4
        self.lastindex = nextsix(self.lastindex, rooter, self.favorites, self.favorite)

        goforward = Button(rooter, text="view next", command= lambda: self.lastIndexBack(rooter,self.favorites))
        goforward.grid(row=4, column=2)

        goback = Button(rooter, text="view previous", command= lambda: self.lastIndexForward(rooter,self.favorites))
        goback.grid(row=4, column=1)


        rooter.grid_columnconfigure(0, weight=1)
        rooter.grid_columnconfigure(1, weight=1)
        rooter.grid_columnconfigure(2, weight=1)
        rooter.grid_columnconfigure(3, weight=1)
        rooter.grid_columnconfigure(4, weight=1)
        rooter.grid_columnconfigure(5, weight=1)
        rooter.grid_columnconfigure(6, weight=1)
        rooter.grid_rowconfigure(0, weight=1)
        rooter.grid_rowconfigure(1, weight=1)
        rooter.grid_rowconfigure(2, weight=1)
        rooter.grid_rowconfigure(3, weight=1)
        rooter.grid_rowconfigure(4, weight=1)
        rooter.grid_rowconfigure(5, weight=1)
        rooter.grid_rowconfigure(6, weight=1)
        rooter.grid_rowconfigure(7, weight=1)
        rooter.grid_columnconfigure(6, weight=1)
        rooter.grid_columnconfigure(7, weight=1)

    def lastIndexForward(self,rooter,favorites):
        self.lastindex= lastsix(self.lastindex,rooter,favorites,self.favorite)

        print(self.lastindex)
    def lastIndexBack(self,rooter,favorites):
        self.lastindex= nextsix(self.lastindex,rooter,favorites,self.favorite)
        print(self.lastindex)
    def acknowledgement(self):
        root = Tk()

        root.title("Color  Coordinator")
        w = Label(root, text='thanks to everyone who helped me stay sane during development (Eric)',
                  font="50")


        w.pack()

    def uploadfile(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File"
                                              )
        name, extension = os.path.splitext(filename)
        print(extension)
        if (".PNG") != extension:
            messagebox.showerror("ERROR", "File must be a .PNG type")
        else:
            image = Image.open(filename)

            self.fileimage = image.resize((200, 200))
            photo = ImageTk.PhotoImage(self.fileimage)

            photoslice = Label(master, image=photo)
            photoslice.image = photo
            photoslice = Button(master, image=photo, command= self.uploadfile)
            photoslice.grid(row=0, column=2,
                            columnspan=2, rowspan=1, padx=5, pady=5)

    def post(self,master):

        item2 = Tk()
        item2.wm_title("Window")
        item2.geometry("200x200")
        l = Label(item2, text="What Text do you want your tweet to say?")
        e1 = Entry(item2)
        e1.grid(row=1, column=0)
        l.grid(row=0, column=0)
        b = Button(item2, text="Submit", command=self.executer)
        b.grid(row=2, column=0)
        self.b2.grid(row=3, column=0)

    def createUpload(self):
        self.masterthis= Toplevel()
        self.masterthis.title("upload artwork")


        self.masterthis.attributes("-topmost", True)
        image = Image.open(self.resource_path("downloadphoto.png"))
        photo= ImageTk.PhotoImage(image)
        uploader = Button(self.masterthis, image=photo)
        uploader.image = photo
        uploader = Button(self.masterthis,image= photo, command=self.click)
        uploader.grid(row=0, column=1)
        global uploadname
        self.userEmail= Entry(self.masterthis)
        self.userPassword= Entry(self.masterthis)
        self.userPassLabel = Label(self.masterthis, text="your email password here")
        self.userPassLabel.grid(row=2, column=2)
        self.userEmailLabel= Label(self.masterthis,text= "your email address here")
        self.userEmailLabel.grid(row=2, column=0)
        self.userPassword.grid(row=2, column = 3)
        self.userEmail.grid(row=2, column= 1)
        self.uploadname = Entry(self.masterthis)
        self.uploadname.grid(row=1, column=1)
        label = Label(self.masterthis, text="Enter the artwork's name here: ")
        label.grid(row=1, column=0)
        # uploader = Button(masterthis, text="upload file", command=self.click)
        # uploader.grid(row=0, column=1)
        self.uploadname = Entry(self.masterthis)
        # self.uploadname.grid(row=1, column=3)
        label = Label(self.masterthis, text="Enter the artwork's name here: ")
        label.grid(row=1, column=0)
        sumbitButton = Button(self.masterthis, text="submit", command= lambda: self.submitImage())
        sumbitButton.grid(row=3, column=1)

    def submitImage(self):
        #used this source to learn email work: https://realpython.com/python-send-email/
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email =self.userEmail.get()
        receiver_email = "capstone498colorcoordinator@gmail.com"
        password = self.userPassword.get()

        message = MIMEMultipart("alternative")
        message["Subject"] = "Artwork Submission"
        message["From"] = sender_email
        message["To"] = receiver_email


        text = "\n the title is: "+ self.uploadname.get() + \
               "the artist is: "+ self.username+ "my submission is: "+ str(self.encrypter)

        part1 = MIMEText(text, "plain")

        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def click(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File"
                                              )
        name, extension = os.path.splitext(self.filename)
        self.masterthis.lift()
        if (".PNG") != extension:
            messagebox.showerror("ERROR", "File must be a .PNG type")
        else:
            self.imageUplaoded = Image.open(self.filename)
            messagebox.showinfo("success", "successfully uploaded image")



    def submit(self):
        conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                               password="Eeliak99.", database="capstone")
        checker = conn.cursor()
        checker.execute("SELECT * FROM slideshow")
        sql = "INSERT INTO `slideshow` (`username`, `img`, `title`) VALUES (%s, %s, %s)"
        checker.execute(sql, (self.userEmail, self.imageUplaoded, self.uploadname.get()))
        conn.close()


    def clickUpload(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select a File"
                                                   )
        self.uploadedimage = Image.open(self.filename)
        self.encrypter= base64.b64encode(open(self.filename, "rb").read())



    def executer(self):
        execute(self.mycolors[0], self.mycolors[1], self.mycolors[2], self.mycolors[3], self.mycolors[4], self.mycolors[5], self.e1.get())
        self.item2.destroy()

    def addToFaves(self):
        CreateMergedImage.create(self.mycolors[0], self.mycolors[1], self.mycolors[2], self.mycolors[3], self.mycolors[4], self.mycolors[5])
        conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                               password="Eeliak99.", database="capstone")
        img = Image.open(self.resource_path("myImageColor.png"))

        c = conn.cursor()
        import base64
        converted_string = base64.b64encode(open("myImageColor.png", "rb").read())
        sql = "INSERT INTO `favoriteImages` (`username`, `image`) VALUES (%s, %s)"
        c.execute(sql, (self.username, converted_string))
        conn.commit()
        sql = "SELECT * FROM favoriteImages"
        c.execute(sql)
        record = c.fetchall()
        self.favorites = record
        print("record", record)



    def switchInputForPhoto(self):


        if self.c.cget("text") == "click here to pick colors from a photo: ":
            self.b1.config(command= lambda: self.colorfromphoto())
            self.lKailee.destroy()
            self.c1.destroy()
            self.c2.destroy()

            mode = False
            my_text = "click her to pick colors from photo"
            self.c.config(text=my_text)

            self.photoslice.destroy()

            self.hexEntry.destroy()
            self.hexLabel.destroy()

            self.l1.destroy()
            self.l1.destroy()

            self.patternchoosen.destroy()
            image = Image.open(self.resource_path("downloadphoto.png"))
            photo = ImageTk.PhotoImage(image)
            photoslice = Label(master, image=photo)
            photoslice.image = photo
            photoslice = Button(master, image=photo, command=self.uploadfile)
            photoslice.grid(row=0, column=2,
                            columnspan=2, rowspan=2, padx=5, pady=5)


        else:
            my_text = "click here to pick colors from a photo: "
            self.lKailee = Label(master, text="OR pick one of these:")
            self.lKailee.grid(row=2, column=0, sticky=W, pady=2)
            self.c1 = ttk.Button(master, text='cool colors ', command=self.coolColors)
            self.c2 = ttk.Button(master, text='warm colors', command=self.warmColors)
            self.c1.grid(row=2, column=1, sticky=W, pady=2)
            self.c2.grid(row=2, column=2, sticky=W, pady=2)
            self.c.config(text=my_text)

            image = Image.open(self.resource_path("wheelofgod.png"))
            photo = ImageTk.PhotoImage(image)
            photoslice = Label(master, image=photo)
            photoslice.image = photo
            photoslice = Button(master, image=photo, command= self.colorpicker)
            photoslice.grid(row=0, column=2,
                            columnspan=2, rowspan=2, padx=5, pady=5)
            self.l1 = Label(master, text="1) color pattern type: ")
            mode = True
            self.l1.grid(row=0, column=0, sticky=W, pady=2)
            self.hexEntry = Entry(master, text= "")
            self.hexLabel = Label(master, text="2) enter your own hex code Here:")
            self.hexLabel.grid(row=1, column=0, sticky=W, pady=2)
            self.hexEntry.grid(row=1, column=1, sticky=W, pady=2)

            self.patternchoosen = ttk.Combobox(master, width=27, )
            self.patternchoosen['values'] = ('Random', 'Monochrome',
                                        'Complimentary',
                                        'split complimentary',
                                        'triadic',
                                        'tetradic', 'analagous',)

            # this will arrange entry widgets
            self.patternchoosen.grid(row=0, column=1, pady=2)

            # button widget

    def lightModes(self):
        master.config(background="#ffffff")

        self.l1.config(background="#ffffff", foreground="#000000")
        self.l3.config(background="#ffffff", foreground="#000000")
        self.l4.config(background="#ffffff", foreground="#000000")
        self.L5.config(background="#ffffff", foreground="#000000")
        self.L7.config(background="#ffffff", foreground="#000000")
        self.L6.config(background="#ffffff", foreground="#000000")
        self.L8.config(background="#ffffff", foreground="#000000")

        self.photoslice.destroy()
        image = Image.open(self.resource_path("wheelofgod.png"))
        photo = ImageTk.PhotoImage(image)
        photoslice = Label(master, image=photo)
        photoslice.image = photo
        photoslice = Button(master, image=photo, command= self.colorpicker)
        photoslice.grid(row=0, column=2,
                        columnspan=2, rowspan=2, padx=5, pady=5)
    def changeColorSqures(self):
        if self.mode == True:
            printedcolors = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff']
            patternTypes = ['Random', 'Monochrome',
                            'Complimentary',
                            'split complimentary',
                            'triadic']
            if (self.hexEntry.get()!= ""):
                selectedColor = self.hexEntry.get()

                if selectedColor[0] != '#':
                    messagebox.showerror("ERROR", "Hex Code must start with #")
                    if (int(str(selectedColor), 16)) > 16777216:
                        messagebox.showerror("ERROR", "Invalid Hex Code")
                if (int(str(selectedColor)[1:], 16)) > 16777216:
                    messagebox.showerror("ERROR", "Invalid Hex Code")

                # selectedColor= selectedColor[1]

            # if (patternchoosen.get() == "" && !c2.instate(['selected']) :
            #    messagebox.showerror("ERROR", "Please Select a Color Pattern Type")
            import CoolColors
            import WarmColors

            # selectedColor = ""
            if (self.patternchoosen.get() == 'Random'):
                pattern = random.choice(patternTypes)
            else:
                pattern = self.patternchoosen.get()

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

                self.mycolors = self.printedcolors
                print("MY VOLORS",str(self.mycolors))

        else:
            printedcolors = colorFromPhoto(self.fileimage)
        self.mycolors = printedcolors
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
        self.hexEntry.delete(0, END)
        self.hexEntry.se
        self.hexEntry.insert(0, "")
        self.l3.config(text=printedcolors[0])
        self.l4.config(text=printedcolors[1])
        self.L5.config(text=printedcolors[2])
        self.L6.config(text=printedcolors[3])
        self.L7.config(text=printedcolors[4])
        self.L8.config(text=printedcolors[5])

    def warmColors(self):
        print("size", master.winfo_reqheight())
        print(master.winfo_reqwidth())
        import WarmColors
        printedcolors = WarmColors.WarmColors()
        self.mycolors = printedcolors
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

    def coolColors(self):
        import CoolColors
        printedcolors = CoolColors.coolColors()
        self.mycolors = printedcolors
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
    def helpWindow(self):

        item1 = Tk()
        item1.wm_title("Window")

        l90 = Label(item1,
                    text="To generate a pallete from photo \nclick the text box and then the file button. \nTo Generate a Pallete from a pattern you\nmust first select a pattern \nand color or else nothing will\nload besides white squares")
        l90.grid(row=0, column=0)
        self.b1.grid(row=1, column=0)

    def switchModes(self):
        master.config(background="#2c2f33")

        self.l1.config(background="#2c2f33", foreground="#99aab5")
        self.l2.config(background="#2c2f33", foreground="#99aab5")
        self.l3.config(background="#2c2f33", foreground="#99aab5")
        self.l4.config(background="#2c2f33", foreground="#99aab5")
        self.L5.config(background="#2c2f33", foreground="#99aab5")
        self.L7.config(background="#2c2f33", foreground="#99aab5")
        self.L6.config(background="#2c2f33", foreground="#99aab5")
        self.L8.config(background="#2c2f33", foreground="#99aab5")

        self.photoslice.destroy()

    def resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)



master = Tk()
Width = master.winfo_screenwidth()
Height = master.winfo_screenheight()

width= master.winfo_screenwidth()
height= master.winfo_screenheight()

master.geometry("%dx%d" % (width, height))
master.resizable(height=None, width=None)
master.title("Color  Coordinator")
mainInterface(master)

master.resizable(0, 0)
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




mainloop()
