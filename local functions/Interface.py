import random
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
global favorites
global filename
from auxsillaryFunctions import isHex
from auxsillaryFunctions import resource_path
from analagous import analagous
from RetrieveColorFromPhoto import colorFromPhoto
import os
import smtplib, ssl
import base64
import Constants
import pymysql
import CreateMergedImage
from tkinter import messagebox
from auxsillaryFunctions import lastsix, nextsix
from TwitterBot import execute
import TwitterBot
from Monochrome import monochrome
from complimentary import comp
from PIL import Image, ImageTk
from SplitComplimentary import splitComplementary
from Tetriadic import tetradic
from Triadic import Triadic
from tkinter import filedialog
from tkinter import colorchooser

#import to start



# refereced tutorial(s)
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
# https://realpython.com/python-send-email/
# https://realpython.com/twitter-bot-python-tweepy/

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
        self.menubar.add_command(label="Create New Log In", command=self.createLogIn)
        self.menubar.add_cascade(label= "change accounts", command= self.changeLogIn)
        self.submenu.add_command(label="Light Mode", command=self.lightModes)
        self.file.add_cascade(label='Visual Settings', menu= self.submenu, underline=0)
        # mode.add_command(label ='Dark Mode', command =mainInterface.switchModes)
        master.config(menu=self.menubar)
        self.lastindex = 6
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

        self.optionLabel = Label(master, text="OR pick one of these:")
        self.optionLabel.grid(row=2, column=0, sticky=W, pady=2)

        self.hexEntry = Entry(master, text="")
        self.hexEntry.grid(row=1, column=1, sticky=W, pady=2)
        self.username= Constants.setUser()
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

        self.squareOne = Label(master, font=1000, text=str(self.printedcolors[0]))
        self.squareOne.grid(row=4, column=0, sticky=W)
        self.squareTwo = Label(master, font=1000, text=str(self.printedcolors[1]))
        self.squareTwo.grid(row=4, column=1, sticky=W)
        self.squareThree = Label(master, font=1000, text=str(self.printedcolors[2]))
        self.squareThree.grid(row=4, column=2, sticky=W)
        self.squareFour = Label(master, font=1000, text=str(self.printedcolors[3]))
        self.squareFour.grid(row=4, column=3, sticky=W)
        self.squareFive = Label(master, font=1000, text=str(self.printedcolors[4]))
        self.squareFive.grid(row=4, column=4, sticky=W)
        self.squareSix = Label(master, font=1000, text=str(self.printedcolors[5]))
        self.squareSix.grid(row=4, column=5, sticky=W)
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
        self.checkentered = self.getEntered(master)

    def getEntered(self,window):
        if len(self.username) ==0:
            window.destoy()
    def colorfromphoto(self):
        printedcolors = colorFromPhoto(self.fileimage)
        self.printedcolors= printedcolors
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
        self.squareOne.destroy()
        self.squareTwo.destroy()
        self.squareThree.destroy()
        self.squareFour.destroy()
        self.squareFive.destroy()
        self.squareSix.destroy()
        self.squareOne = Label(master, font=1200, text=str(printedcolors[0]))
        self.squareOne.grid(row=4, column=0, sticky=W)
        self.squareTwo = Label(master, font=1200, text=str(printedcolors[1]))
        self.squareTwo.grid(row=4, column=1, sticky=W)
        self.squareThree = Label(master, font=1200, text=str(printedcolors[2]))
        self.squareThree.grid(row=4, column=2, sticky=W)
        self.squareFour = Label(master, font=1200, text=str(printedcolors[3]))
        self.squareFour.grid(row=4, column=3, sticky=W)
        self.squareFive = Label(master, font=1200, text=str(printedcolors[4]))
        self.squareFive.grid(row=4, column=4, sticky=W)
        self.squareSix = Label(master, font=1200, text=str(printedcolors[5]))
        self.squareSix.grid(row=4, column=5, sticky=W)
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
        print("I AM HERE" ,self.username)
        self.favorites=[]
        for i in range(0,len(self.favorite)):
            if self.favorite[i][0] == self.username:
                print(self.username)
                self.favorites.append(self.favorite[i])
        if (len(self.favorites) == 0):
            print("no favorites")
            self.favorites= []



        self.lastindex= 4
        self.lastindex = nextsix(self.lastindex, rooter, self.favorites, self.favorite, self.username)
        print(str(self.favorites))
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
        self.lastindex= lastsix(self.lastindex,rooter,favorites,self.favorite,self.username)

    def lastIndexBack(self,rooter,favorites):
        self.lastindex= nextsix(self.lastindex,rooter,favorites,self.favorite,self.username)

    def acknowledgement(self):
        acknowledgements = Tk()
        acknowledgements .resizable(0, 0)
        acknowledgements .title("Color  Coordinator")
        w = Label(acknowledgements , text='thanks to everyone who helped me stay sane during development (Eric, Liz, Bobby, Dani, nicholas, Kat, Dr Kreider)',
                  font="50")
        w.pack()

    def uploadfile(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File"
                                              )
        name, extension = os.path.splitext(filename)

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
                            columnspan=2, rowspan=2, padx=5, pady=5)

    def post(self):

        self.twitterWindow = Tk()
        self.twitterWindow.resizable(0, 0)
        self.twitterWindow.wm_title("Post to Twitter")
        self.twitterWindow.geometry("200x200")
        l = Label(self.twitterWindow, text="What Text do you want your tweet to say?")
        self.e1 = Entry(self.twitterWindow)
        self.e1.grid(row=1, column=0)
        l.grid(row=0, column=0)
        b = Button(self.twitterWindow, text="SubmitImage", command=self.executer)
        b.grid(row=2, column=0)

    def createUpload(self):
        self.uploadWindow= Toplevel()
        self.uploadWindow.title("upload artwork")
        self.uploadWindow.resizable(0, 0)

        self.uploadWindow.attributes("-topmost", True)
        image = Image.open(self.resource_path("downloadphoto.png"))
        photo= ImageTk.PhotoImage(image)
        uploader = Button(self.uploadWindow, image=photo)
        uploader.image = photo
        uploader = Button(self.uploadWindow,image= photo, command=self.clickUpload)

        uploader.grid(row=0, column=1)

        self.userEmail= Entry(self.uploadWindow)
        self.userPassword= Entry(self.uploadWindow,show= "*")
        self.userPassLabel = Label(self.uploadWindow, text="your email password here")
        self.userPassLabel.grid(row=2, column=2)
        self.userEmailLabel= Label(self.uploadWindow,text= "your email address here")
        self.userEmailLabel.grid(row=2, column=0)
        self.userPassword.grid(row=2, column = 3)
        self.userEmail.grid(row=2, column= 1)
        self.uploadname = Entry(self.uploadWindow)
        self.uploadname.grid(row=1, column=1)
        label = Label(self.uploadWindow, text="Enter the artwork's name here: ")
        label.grid(row=1, column=0)

        label = Label(self.uploadWindow, text="Enter the artwork's name here: ")
        label.grid(row=1, column=0)
        sumbitButton = Button(self.uploadWindow, text="submit", command= lambda: self.submitImage())
        sumbitButton.grid(row=3, column=1)

    def submitImage(self):
        #used this source to learn email work: https://realpython.com/python-send-email/
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        self.sender_email =self.userEmail.get()
        receiver_email = "capstone498colorcoordinator@gmail.com"
        password = self.userPassword.get()

        message = MIMEMultipart("alternative")
        message["Subject"] = "Artwork Submission"
        message["From"] = self.sender_email
        message["To"] = receiver_email


        text = "\n the title is: "+ self.uploadname.get() + \
               " the artist is: "+ self.userEmail.get()+ " my submission is: "+ str(self.encrypter)

        part1 = MIMEText(text, "plain")

        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, password)
            server.sendmail(
                self.sender_email, receiver_email, message.as_string()

            )
        self.uploadWindow.destroy()

    def click(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File"
                                              )
        name, extension = os.path.splitext(self.filename)
        self.uploadWindow.lift()
        if (".PNG") != extension:
            messagebox.showerror("ERROR", "File must be a .PNG type")
        else:
            self.imageUplaoded = Image.open(self.filename)
            messagebox.showinfo("success", "successfully uploaded image")


    def clickUpload(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select a File"
                                                   )
        self.uploadedimage = Image.open(self.filename)
        self.encrypter= base64.b64encode(open(self.filename, "rb").read())



    def executer(self):
        execute(self.mycolors[0], self.mycolors[1], self.mycolors[2], self.mycolors[3], self.mycolors[4], self.mycolors[5], self.e1.get())
        self.twitterWindow.destroy()

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




    def switchInputForPhoto(self):


        if self.c.cget("text") == "click here to pick colors from a photo: ":
            self.b1.config(command= lambda: self.colorfromphoto())
            self.optionLabel.destroy()
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
            self.optionLabel = Label(master, text="OR pick one of these:")
            self.optionLabel.grid(row=2, column=0, sticky=W, pady=2)
            self.c1 = ttk.Button(master, text='cool colors ', command=self.coolColors)
            self.c2 = ttk.Button(master, text='warm colors', command=self.warmColors)
            self.c1.grid(row=2, column=1, sticky=W, pady=2)
            self.c2.grid(row=2, column=2, sticky=W, pady=2)
            self.c.config(text=my_text)
            self.b1.destroy()
            self.b1 = Button(master, text="Generate Pallete", style='green/black.TButton',
                             command=self.changeColorSqures)
            self.b1.grid(row=2, column=3, sticky=W)
            image = Image.open(self.resource_path("wheelofgod.png"))
            photo = ImageTk.PhotoImage(image)
            photoslice = Label(master, image=photo)
            photoslice.image = photo
            photoslice = Button(master, image=photo, command=self.colorpicker)
            photoslice.grid(row=0, column=2,
                            columnspan=2, rowspan=2, padx=5, pady=5)
            self.l1 = Label(master, text="1) select a color pattern type: ")
            mode = True
            self.l1.grid(row=0, column=0, sticky=W, pady=2)
            self.hexEntry = Entry(master, text="")
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


            if self.isDarkMode:
                master.config(background="#2c2f33")
                self.l1.config(background="#2c2f33", foreground="#E4E6EB")
                self.squareOne.destroy()
                self.squareTwo.destroy()
                self.squareThree.destroy()
                self.squareFour.destroy()
                self.squareFive.destroy()
                self.squareSix.destroy()

                self.squareOne = Label(master, font=1000, text=str(self.printedcolors[0]))
                self.squareOne.grid(row=4, column=0, sticky=W)
                self.squareTwo = Label(master, font=1000, text=str(self.printedcolors[1]))
                self.squareTwo.grid(row=4, column=1, sticky=W)
                self.squareThree = Label(master, font=1000, text=str(self.printedcolors[2]))
                self.squareThree.grid(row=4, column=2, sticky=W)
                self.squareFour = Label(master, font=1000, text=str(self.printedcolors[3]))
                self.squareFour.grid(row=4, column=3, sticky=W)
                self.squareFive = Label(master, font=1000, text=str(self.printedcolors[4]))
                self.squareFive.grid(row=4, column=4, sticky=W)
                self.squareSix = Label(master, font=1000, text=str(self.printedcolors[5]))
                self.squareSix.grid(row=4, column=5, sticky=W)
                self.optionLabel.config(background="#2c2f33", foreground="#E4E6EB")
                self.squareOne.config(background="#2c2f33", foreground="#E4E6EB")
                self.squareTwo.config(background="#2c2f33", foreground="#E4E6EB")
                self.squareThree.config(background="#2c2f33", foreground="#E4E6EB")
                self.squareFour.config(background="#2c2f33", foreground="#E4E6EB")
                self.squareFive.config(background="#2c2f33", foreground="#E4E6EB")
                self.squareSix.config(background="#2c2f33", foreground="#E4E6EB")
                self.hexLabel.config(background="#2c2f33", foreground="#E4E6EB")
                image = Image.open(self.resource_path("blackColorWheel.PNG"))
                photo = ImageTk.PhotoImage(image)
                self.photoslice.destroy()
                self.photoslice = Label(master, image=photo)
                self.photoslice.image = photo
                self.photoslice = Button(master, image=photo, command=self.colorpicker)
                self.photoslice.grid(row=0, column=2,
                                     columnspan=2, rowspan=2, padx=5, pady=5)

            # button widget

    def lightModes(self):
        self.isDarkMode= False
        master.config(background="#F0F0F0")
        self.optionLabel.config(background="#F0F0F0", foreground="#000000")
        self.hexLabel.config(background="#F0F0F0", foreground="#000000")
        self.l1.config(background="#F0F0F0", foreground="#000000")
        self.squareOne.config(background="#F0F0F0", foreground="#000000")
        self.squareTwo.config(background="#F0F0F0", foreground="#000000")
        self.squareThree.config(background="#F0F0F0", foreground="#000000")
        self.squareFive.config(background="#F0F0F0", foreground="#000000")
        self.squareFour.config(background="#F0F0F0", foreground="#000000")
        self.squareSix.config(background="#F0F0F0", foreground="#000000")

        self.photoslice.destroy()
        image = Image.open(self.resource_path("wheelofgod.png"))
        photo = ImageTk.PhotoImage(image)
        self.photoslice = Label(master, image=photo)
        self.photoslice.image = photo
        self.photoslice = Button(master, image=photo, command= self.colorpicker)
        self.photoslice.grid(row=0, column=2,
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
                randomcolor= "#"
                while len(str(randomcolor)) <7:
                    randomcolor += random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
                if isHex(selectedColor) == False:
                    messagebox.showerror("ERROR", "Invalid character(s), color will be set to random")

                    selectedColor= randomcolor
                if selectedColor[0] != '#':
                    messagebox.showerror("ERROR", "Hex Code must start with #,color will be set to random")
                    selectedColor = randomcolor
                    if (int(str(selectedColor), 16)) > 16777216:
                        messagebox.showerror("ERROR", "Invalid Hex Code,color will be set to random")
                        selectedColor = randomcolor

            import CoolColors
            import WarmColors


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
            self.printedcolors = printedcolors

        else:
            print("error")
            #1345768
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
        self.squareOne.destroy()
        self.squareTwo.destroy()
        self.squareThree.destroy()
        self.squareFour.destroy()
        self.squareFive.destroy()
        self.squareSix.destroy()

        self.squareOne = Label(master, font=1000, text=str(printedcolors[0]))
        self.squareOne.grid(row=4, column=0, sticky=W)
        self.squareTwo = Label(master, font=1000, text=str(printedcolors[1]))
        self.squareTwo.grid(row=4, column=1, sticky=W)
        self.squareThree = Label(master, font=1000, text=str(printedcolors[2]))
        self.squareThree.grid(row=4, column=2, sticky=W)
        self.squareFour = Label(master, font=1000, text=str(printedcolors[3]))
        self.squareFour.grid(row=4, column=3, sticky=W)
        self.squareFive = Label(master, font=1000, text=str(printedcolors[4]))
        self.squareFive.grid(row=4, column=4, sticky=W)
        self.squareSix = Label(master, font=1000, text=str(printedcolors[5]))
        self.squareSix.grid(row=4, column=5, sticky=W)

    def changeLogIn(self):
        self.LoginWindows = Tk()

        self.LoginWindows.resizable(0, 0)
        self.LoginWindows.wm_title("Log in")
        newuser = Label(self.LoginWindows, text= "Enter log in")
        newuser.grid(row=0, column= 0)
        newpassword=  Label(self.LoginWindows, text= "Enter account password")
        newpassword.grid(row=1, column=0)
        self.userEntry = Entry(self.LoginWindows)
        self.passwordEntry= Entry(self.LoginWindows, show = "*")
        self.userEntry.grid(row=0, column= 1)
        self.passwordEntry.grid(row=1, column=1)
        enterButton = Button(self.LoginWindows, text = "change log in", command= self.changeLogger)
        enterButton.grid(row= 2, column=1, columnspan=2)

    def changeLogger(self):
        conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                               password="Eeliak99.", database="capstone")

        c = conn.cursor()
        c.execute("SELECT* FROM users")
        records = c.fetchall()
        users = records
        entry = False

        global answer
        answer = self.userEntry.get()

        for i in range(0, len(users)):
            if self.userEntry.get() in users[i]:
                if self.passwordEntry.get() in users[i]:

                    entry = True
        if entry == False:
            messagebox.showerror("ERROR", "This password or Username is incorrect")

        if entry == True:
            self.username = self.userEntry.get()
            print("user has been changed")
            print(self.username)
            favorites = []
            messagebox.showinfo("Success", "Switched accounts.")
            self.LoginWindows.destroy()

    def createLogIn(self):
        self.LoginWindow = Tk()

        self.LoginWindow.resizable(0, 0)
        self.LoginWindow.wm_title("Create new Log in")
        newuser = Label(self.LoginWindow, text="Enter new log in")
        newuser.grid(row=0, column=0)
        newpassword = Label(self.LoginWindow, text="Enter new account password")
        namer = Label(self.LoginWindow, text="Enter your first name").grid(row = 2, column= 0)
        lastname= Label(self.LoginWindow, text= "Enter your last name").grid(row= 3, column = 0)
        self.namerentry = Entry(self.LoginWindow)
        self.namerentry.grid(row=2, column=1)
        self.lastnamentry = Entry(self.LoginWindow)
        self.lastnamentry.grid(row=3, column=1)
        newpassword.grid(row=1, column=0)
        self.userEntry = Entry(self.LoginWindow)
        self.passwordEntry = Entry(self.LoginWindow, show="*")
        self.userEntry.grid(row=0, column=1)
        self.passwordEntry.grid(row=1, column=1)
        enterButton = Button(self.LoginWindow, text="create log in",
                             command= self.createLogger)
        enterButton.grid(row=4, column=1, columnspan=2)

    def createLogger(self):
        conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                               password="Eeliak99.", database="capstone")
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        import re
        c = conn.cursor()
        sql = "SELECT * FROM `users`"
        c.execute(sql)
        records = c.fetchall()
        users = records
        entry = False
        for i in range(0, len(users)):
            if self.userEntry.get() in users[i]:
                entry = True
        if (entry == False):
            if (len(self.userEntry.get()) >= 6):
                if (self.userEntry.get() != ""):
                    if (self.namerentry.get() != ""):
                        if (re.search(regex, self.userEntry.get())):

                            conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com',
                                                   user='kailee',
                                                   password="Eeliak99.", database="capstone")

                            c = conn.cursor()
                            sql = "INSERT INTO `users` (`username`, `first_name`, `last_name`, `password`) VALUES (%s, %s, %s, %s)"
                            c.execute(sql, (self.userEntry.get(), self.namerentry.get(), self.lastnamentry.get(), self.passwordEntry.get()))
                            conn.commit()
                            sql = "SELECT * FROM `users`"
                            c.execute(sql)
                            result = c.fetchall()
                            user = result
                            self.userEntry.delete(0, END)
                            self.namerentry.delete(0, END)
                            self.lastnamentry.delete(0, END)
                            self.passwordEntry.delete(0, END)

                            messagebox.showinfo("Success!", "Your account has been created!")
                            self.LoginWindow.destroy()

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

    def warmColors(self):

        import WarmColors
        printedcolors = WarmColors.WarmColors()
        self.printedcolors = printedcolors
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

        self.squareOne.destroy()
        self.squareTwo.destroy()
        self.squareThree.destroy()
        self.squareFour.destroy()
        self.squareFive.destroy()
        self.squareSix.destroy()

        self.squareOne = Label(master, font=1000, text=str(printedcolors[0]))
        self.squareOne.grid(row=4, column=0, sticky=W)
        self.squareTwo = Label(master, font=1000, text=str(printedcolors[1]))
        self.squareTwo.grid(row=4, column=1, sticky=W)
        self.squareThree = Label(master, font=1000, text=str(printedcolors[2]))
        self.squareThree.grid(row=4, column=2, sticky=W)
        self.squareFour = Label(master, font=1000, text=str(printedcolors[3]))
        self.squareFour.grid(row=4, column=3, sticky=W)
        self.squareFive = Label(master, font=1000, text=str(printedcolors[4]))
        self.squareFive.grid(row=4, column=4, sticky=W)
        self.squareSix = Label(master, font=1000, text=str(printedcolors[5]))
        self.squareSix.grid(row=4, column=5, sticky=W)

    def coolColors(self):
        import CoolColors
        printedcolors = CoolColors.coolColors()
        self.printedcolors = printedcolors
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

        self.squareOne.destroy()
        self.squareTwo.destroy()
        self.squareThree.destroy()
        self.squareFour.destroy()
        self.squareFive.destroy()
        self.squareSix.destroy()
        self.squareOne = Label(master, font=1000, text=str(printedcolors[0]))
        self.squareOne.grid(row=4, column=0, sticky=W)
        self.squareTwo = Label(master, font=1000, text=str(printedcolors[1]))
        self.squareTwo.grid(row=4, column=1, sticky=W)
        self.squareThree = Label(master, font=1000, text=str(printedcolors[2]))
        self.squareThree.grid(row=4, column=2, sticky=W)
        self.squareFour = Label(master, font=1000, text=str(printedcolors[3]))
        self.squareFour.grid(row=4, column=3, sticky=W)
        self.squareFive = Label(master, font=1000, text=str(printedcolors[4]))
        self.squareFive.grid(row=4, column=4, sticky=W)
        self.squareSix = Label(master, font=1000, text=str(printedcolors[5]))
        self.squareSix.grid(row=4, column=5, sticky=W)
    def helpWindow(self):

        helpWindow = Tk()
        
        helpWindow.resizable(0, 0)
        helpWindow.wm_title("Window")

        l90 = Label(helpWindow,
                    text= """To generate a palette, there are three different methods:

pattern generation:
1) first select a type of  pattern from the drop down.
2) either enter a hex code yourself or click the 
   image of the color wheel to use the color slider
3) click GENERATE PALLETE
*patterns can be create multiple times by clicking GENERATE PALLETE   


warm and cool colors:
1) click either WARM COLORS or COOL COLORS
* you do not need to enter a hex code as it will not be used

palette from a photo:
1) click the check box to change the interface
2) upload a PNG by click the upload button
3) click GENRATE PALLETE
*patterns can be create multiple times by clicking GENERATE PALLETE  

                     
                    """)
        l90.grid(row=0, column=0)


    def switchModes(self):
        self.isDarkMode= True
        master.config(background="#2c2f33")
        self.l1.config(background="#2c2f33", foreground="#E4E6EB")
        self.squareOne.destroy()
        self.squareTwo.destroy()
        self.squareThree.destroy()
        self.squareFour.destroy()
        self.squareFive.destroy()
        self.squareSix.destroy()

        self.squareOne = Label(master, font=1000, text=str(self.printedcolors[0]))
        self.squareOne.grid(row=4, column=0, sticky=W)
        self.squareTwo = Label(master, font=1000, text=str(self.printedcolors[1]))
        self.squareTwo.grid(row=4, column=1, sticky=W)
        self.squareThree = Label(master, font=1000, text=str(self.printedcolors[2]))
        self.squareThree.grid(row=4, column=2, sticky=W)
        self.squareFour = Label(master, font=1000, text=str(self.printedcolors[3]))
        self.squareFour.grid(row=4, column=3, sticky=W)
        self.squareFive = Label(master, font=1000, text=str(self.printedcolors[4]))
        self.squareFive.grid(row=4, column=4, sticky=W)
        self.squareSix = Label(master, font=1000, text=str(self.printedcolors[5]))
        self.squareSix.grid(row=4, column=5, sticky=W)
        self.optionLabel.config(background="#2c2f33", foreground="#E4E6EB")
        self.squareOne.config(background="#2c2f33", foreground="#E4E6EB")
        self.squareTwo.config(background="#2c2f33", foreground="#E4E6EB")
        self.squareThree.config(background="#2c2f33", foreground="#E4E6EB")
        self.squareFour.config(background="#2c2f33", foreground="#E4E6EB")
        self.squareFive.config(background="#2c2f33", foreground="#E4E6EB")
        self.squareSix.config(background="#2c2f33", foreground= "#E4E6EB")
        self.hexLabel.config(background="#2c2f33", foreground="#E4E6EB")
        image = Image.open(self.resource_path("blackColorWheel.PNG"))
        photo = ImageTk.PhotoImage(image)
        self.photoslice.destroy()
        self.photoslice = Label(master, image=photo)
        self.photoslice.image = photo
        self.photoslice = Button(master, image=photo, command=self.colorpicker)
        self.photoslice.grid(row=0, column=2,
                        columnspan=2, rowspan=2, padx=5, pady=5)



    def resource_path(self,relative_path):
        #used tutorail for all instances of this function https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
        try:
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
