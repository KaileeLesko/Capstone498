def hex_to_rgb(value):
    print(value, " value")
    value = value.lstrip('#')
    print(list(int(value[i:i + 2], 16) for i in (0, 2, 4)))
    return list(int(value[i:i + 2], 16) for i in (0, 2, 4))
from TwitterBot import execute
global favorites
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

global favorites, favorite
def RGB2HSL(R, G, B):
    R = R / 255
    G = G / 255
    B = B / 255
    arr = [R, G, B]
    maxB = -1000000
    minR = 1000000

    i = 0

    while i < len(arr):
        if arr[i] > maxB:
            maxB = arr[i]
        if arr[i] < minR:
            minR = arr[i]
        i = i + 1

    L = (minR + maxB) / 2

    if L <= 0.5:
        S = (maxB - minR) / (maxB + minR)
    else:
        S = (maxB - minR) / (2.0 - maxB - minR)

    HueChoices = [R, G, B]
    Hue = max(HueChoices)
    if Hue == R:
        H = (G - B) / (maxB - minR)
        H = H * 60
    if Hue == G:
        H = 2.0 + (B - R) / (maxB - minR)
        H = H * 60
    else:
        H = 4.0 + (R - G) / (maxB - minR)
        H *= 60
    if H < 0:
        H += 360
    return [H, S, L]


from tkinter import messagebox
import os
import base64
from PIL import Image, ImageTk
import tkinter
import pymysql
import Constants
def createFavorites():
    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")
    c = conn.cursor()

    c.execute("SELECT * FROM favoriteImages")
    favorite = c.fetchall()
    favorites=[]
    print("favorite ", favorite)
    for i in range(0, len(favorite)):
        if favorite[i][0] == Constants.setUser():
            favorites.append(favorite[i])
    return favorites
def remover(i, favorites, lastindex, rooter, favorite,  current):

    conn = pymysql.connect(host='coolorcoordinator.cuw5r9k9lei6.us-east-1.rds.amazonaws.com', user='kailee',
                           password="Eeliak99.", database="capstone")
    c = conn.cursor()
    sql= "DELETE FROM favoriteImages WHERE image = %s"
    print(current)
    #adr = current.decode('utf-8')
    adr= current
    c.execute(sql, adr)
    conn.commit()
    nextsix(4, rooter, favorites, favorite)
def massdestroy(f1):
    f1.destroy()


def multipleOptions(row,column, rooter,i,favorite,favorites,lastindex,temp):
    f1 = tkinter.Frame(rooter)
    b1 =Button(f1, text="Delete from Favorites",command= lambda: remover(i, favorites, lastindex, rooter, favorite, favorites[temp][1]))
    b2 = Button(f1, text="Post to Twitter", command= lambda: post(favorites[temp][1]))
    b3 = Button(f1, text= "close" ,command= lambda: massdestroy(f1))
    b1.pack(side="top")
    b2.pack(side="top")
    b3.pack(side="top")

    f1.grid(row= row, column= column)

from tkinter import Label,Button
def nextsix(lastindex, rooter,favorites,favorite):
            favorites = createFavorites()
            print("reached next six")
            global photo3, photo1, photo2, photo4, photo5, photo6
            global one, two, three, four, five, six

            if os.path.exists('two.png'):
                os.remove('two.png')
            if os.path.exists('one.png'):

                os.remove('one.png')
            if os.path.exists('three.png'):
                os.remove('three.png')
            if os.path.exists('four.png'):
                os.remove('four.png')
            if os.path.exists('five.png'):
                os.remove('five.png')
            if os.path.exists('six.png'):
                os.remove('six.png')
            count=1
            for i in range(lastindex-4, lastindex+2):
                print("reached again")
                print(type(favorites))
                print(len(favorites))
                if (count == 1):

                    if i >= len(favorites):
                        newimg = Image.open('whiteIMG.png')
                        newimg = newimg.resize((600, 100))
                        photo1 = ImageTk.PhotoImage(newimg)
                        rooter.one = Label(rooter, image=photo1)
                        rooter.one.grid(row=1, column=1)
                    else:
                        if os.path.exists('one.png'):
                            os.remove('one.png')
                        decodeit = open('one.png', 'wb')
                        print(i)
                        decodeit.write(base64.b64decode((favorites[i][1])))
                        decodeit.close()
                        newimg = Image.open('one.png')
                        newimg = newimg.resize((600, 100))
                        temp1= i
                        photo1 = ImageTk.PhotoImage(newimg)
                        row1=1
                        column1=1
                        rooter.one = Button(rooter, image=photo1, command= lambda: multipleOptions(row1,column1, rooter,i,favorite,favorites,lastindex,temp1))
                        rooter.one.grid(row=1, column=1)
                    count = 2
                elif (count == 2):
                    print("index:", i )
                    if i >= len(favorites):
                        newimg = Image.open('whiteIMG.png')
                        newimg = newimg.resize((600, 100))
                        photo2 = ImageTk.PhotoImage(newimg)
                        rooter.two = Label(rooter, image=photo2)
                        rooter.two.grid(row=2, column=1)
                    else:
                        if os.path.exists('two.png'):
                            os.remove('two.png')
                        decodeit = open('two.png', 'wb')
                        decodeit.write(base64.b64decode((favorites[i][1])))
                        decodeit.close()
                        newimg = Image.open('two.png')
                        newimg = newimg.resize((600, 100))
                        temp2= i
                        photo2 = ImageTk.PhotoImage(newimg)
                        row2= 2
                        column2= 1
                        rooter.two = Button(rooter, image=photo2, command= lambda: multipleOptions(row2,column2, rooter,i,favorite,favorites,lastindex,temp2))
                        rooter.two.grid(row=2, column=1)
                    count = 3

                elif (count == 3):
                    if i >= len(favorites):
                        newimg = Image.open('whiteIMG.png')
                        newimg = newimg.resize((600, 100))
                        photo3 = ImageTk.PhotoImage(newimg)
                        rooter.three = Label(rooter, image=photo3)
                        rooter.three.grid(row=3, column=1)
                    else:
                        if os.path.exists('three.png'):
                            os.remove('three.png')
                        decodeit = open('three.png', 'wb')

                        decodeit.write(base64.b64decode((favorites[i][1])))
                        decodeit.close()
                        newimg = Image.open('three.png')
                        newimg = newimg.resize((600, 100))
                        temp3= i
                        photo3 = ImageTk.PhotoImage(newimg)
                        row3=3
                        column3=1
                        rooter.three= Button(rooter, image=photo3, command= lambda: multipleOptions(row3,column3, rooter,i,favorite,favorites,lastindex,temp3))
                        rooter.three.grid(row=3, column=1)
                    count = 4
                elif (count == 4):
                    print("LEN OF FAV", len(favorites), i)
                    if i >= len(favorites):
                        newimg = Image.open('whiteIMG.png')
                        newimg = newimg.resize((600, 100))
                        photo4 = ImageTk.PhotoImage(newimg)
                        rooter.four = Label(rooter, image=photo4)
                        rooter.four.grid(row=1, column=2)
                    else:
                        if os.path.exists('four.png'):
                            os.remove('four.png')
                        decodeit = open('four.png', 'wb')

                        decodeit.write(base64.b64decode((favorites[i][1])))
                        decodeit.close()
                        newimg = Image.open('four.png')
                        newimg = newimg.resize((600, 100))
                        photo4 = ImageTk.PhotoImage(newimg)
                        row4=1
                        temp4=i
                        column4= 2
                        rooter.four = Button(rooter, image=photo4, command= lambda: multipleOptions(row4,column4, rooter,i,favorite,favorites,lastindex,temp4))
                        rooter.four.grid(row=1, column=2)
                    count = 5
                elif (count == 5):
                    if i >= len(favorites):
                        newimg = Image.open('whiteIMG.png')
                        newimg = newimg.resize((600, 100))
                        photo5 = ImageTk.PhotoImage(newimg)
                        rooter.five = Label(rooter, image=photo5)
                        rooter.five.grid(row=2, column=2)
                    else:
                        if os.path.exists('five.png'):
                            os.remove('five.png')
                        decodeit = open('five.png', 'wb')

                        decodeit.write(base64.b64decode((favorites[i][1])))
                        decodeit.close()
                        newimg = Image.open('five.png')
                        newimg = newimg.resize((600, 100))
                        temp5=i
                        photo5 = ImageTk.PhotoImage(newimg)
                        row5= 2
                        column5= 2
                        rooter.five = Button(rooter, image=photo5, command= lambda: multipleOptions(row5,column5, rooter,i,favorite,favorites,lastindex,temp5))
                        rooter.five.grid(row=2, column=2)
                    count = 6
                elif count==6:
                    if i >= len(favorites):
                        newimg = Image.open('whiteIMG.png')
                        newimg = newimg.resize((600, 100))
                        photo6= ImageTk.PhotoImage(newimg)
                        rooter.six = Label(rooter, image=photo6)
                        rooter.six.grid(row=3, column=2)
                    else:
                        if os.path.exists('six.png'):
                            os.remove('six.png')
                        decodeit = open('six.png', 'wb')

                        decodeit.write(base64.b64decode((favorites[i][1])))
                        decodeit.close()
                        newimg = Image.open('six.png')
                        newimg = newimg.resize((600, 100))
                        temp6=i
                        photo6 = ImageTk.PhotoImage(newimg)
                        row6= 3
                        column6=2
                        rooter.six = Button(rooter, image=photo6, command= lambda: multipleOptions(row6,column6, rooter,i,favorite,favorites,lastindex,temp6))
                        rooter.six.grid(row=3, column=2)
                    count = 7
                    lastindex=i
                    print("HELLO ",i)
                    print("DING DONG DONE")
            return lastindex

def lastsix(lastindex, rooter,favorites,favorite):
    print("reached next six")
    global photo3, photo1, photo2, photo4, photo5, photo6
    global one, two, three, four, five, six
    favorites= createFavorites()
    if (lastindex <0):
        messagebox.showerror("You have no more favorites saved")

    else:
        if os.path.exists('two.png'):
            os.remove('two.png')
        if os.path.exists('one.png'):
            os.remove('one.png')
        if os.path.exists('three.png'):
            os.remove('three.png')
        if os.path.exists('four.png'):
            os.remove('four.png')
        if os.path.exists('five.png'):
            os.remove('five.png')
        if os.path.exists('six.png'):
            os.remove('six.png')
        count = 1
        for i in range(lastindex-1,lastindex-8,-1):
            print("reached again")
            print(type(favorites))
            print(len(favorites))
            if (count == 1):
                lastindex = i
                if i >= len(favorites):

                    newimg = Image.open('whiteIMG.png')
                    newimg = newimg.resize((600, 100))
                    photo1 = ImageTk.PhotoImage(newimg)
                    rooter.one = Label(rooter, image=photo1)
                    rooter.one.grid(row=1, column=1)
                else:
                    if os.path.exists('one.png'):
                        os.remove('one.png')
                    decodeit = open('one.png', 'wb')
                    print(i)
                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('one.png')
                    newimg = newimg.resize((600, 100))
                    temp1 = i
                    photo1 = ImageTk.PhotoImage(newimg)
                    row1 = 1
                    column1 = 1
                    rooter.one = Button(rooter, image=photo1,
                                        command=lambda: multipleOptions(row1, column1, rooter, i, favorite, favorites,
                                                                        lastindex, temp1))
                    rooter.one.grid(row=1, column=1)
                count = 2
            elif (count == 2):
                print("index:", i)
                if i >= len(favorites):
                    newimg = Image.open('whiteIMG.png')
                    newimg = newimg.resize((600, 100))
                    photo2 = ImageTk.PhotoImage(newimg)
                    rooter.two = Label(rooter, image=photo2)
                    rooter.two.grid(row=2, column=1)
                else:
                    if os.path.exists('two.png'):
                        os.remove('two.png')
                    decodeit = open('two.png', 'wb')
                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('two.png')
                    newimg = newimg.resize((600, 100))
                    temp2 = i
                    photo2 = ImageTk.PhotoImage(newimg)
                    row2 = 2
                    column2 = 1
                    rooter.two = Button(rooter, image=photo2,
                                        command=lambda: multipleOptions(row2, column2, rooter, i, favorite, favorites,
                                                                        lastindex, temp2))
                    rooter.two.grid(row=2, column=1)
                count = 3

            elif (count == 3):
                if i >= len(favorites):
                    newimg = Image.open('whiteIMG.png')
                    newimg = newimg.resize((600, 100))
                    photo3 = ImageTk.PhotoImage(newimg)
                    rooter.three = Label(rooter, image=photo3)
                    rooter.three.grid(row=3, column=1)
                else:
                    if os.path.exists('three.png'):
                        os.remove('three.png')
                    decodeit = open('three.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('three.png')
                    newimg = newimg.resize((600, 100))
                    temp3 = i
                    photo3 = ImageTk.PhotoImage(newimg)
                    row3 = 3
                    column3 = 1
                    rooter.three = Button(rooter, image=photo3,
                                          command=lambda: multipleOptions(row3, column3, rooter, i, favorite, favorites,
                                                                          lastindex, temp3))
                    rooter.three.grid(row=3, column=1)
                count = 4
            elif (count == 4):
                print("LEN OF FAV", len(favorites), i)
                if i >= len(favorites):
                    newimg = Image.open('whiteIMG.png')
                    newimg = newimg.resize((600, 100))
                    photo4 = ImageTk.PhotoImage(newimg)
                    rooter.four = Label(rooter, image=photo4)
                    rooter.four.grid(row=1, column=2)
                else:
                    if os.path.exists('four.png'):
                        os.remove('four.png')
                    decodeit = open('four.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('four.png')
                    newimg = newimg.resize((600, 100))
                    photo4 = ImageTk.PhotoImage(newimg)
                    row4 = 1
                    temp4=i
                    column4 = 2
                    rooter.four = Button(rooter, image=photo4,
                                         command=lambda: multipleOptions(row4, column4, rooter, i, favorite, favorites,
                                                                         lastindex, temp4))
                    rooter.four.grid(row=1, column=2)
                count = 5
            elif (count == 5):
                if i >= len(favorites):
                    newimg = Image.open('whiteIMG.png')
                    newimg = newimg.resize((600, 100))
                    photo5 = ImageTk.PhotoImage(newimg)
                    rooter.five = Label(rooter, image=photo5)
                    rooter.five.grid(row=2, column=2)
                else:
                    if os.path.exists('five.png'):
                        os.remove('five.png')
                    decodeit = open('five.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('five.png')
                    newimg = newimg.resize((600, 100))
                    temp5 = i
                    photo5 = ImageTk.PhotoImage(newimg)
                    row5 = 2
                    column5 = 2
                    rooter.five = Button(rooter, image=photo5,
                                         command=lambda: multipleOptions(row5, column5, rooter, i, favorite, favorites,
                                                                         lastindex, temp5))
                    rooter.five.grid(row=2, column=2)
                count = 6
            elif count == 6:
                if i >= len(favorites):
                    newimg = Image.open('whiteIMG.png')
                    newimg = newimg.resize((600, 100))
                    photo6 = ImageTk.PhotoImage(newimg)
                    rooter.six = Label(rooter, image=photo6)
                    rooter.six.grid(row=3, column=2)
                else:
                    if os.path.exists('six.png'):
                        os.remove('six.png')
                    decodeit = open('six.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('six.png')
                    newimg = newimg.resize((600, 100))
                    temp6 = i
                    photo6 = ImageTk.PhotoImage(newimg)
                    row6 = 3
                    column6 = 2
                    rooter.six = Button(rooter, image=photo6,
                                        command=lambda: multipleOptions(row6, column6, rooter, i, favorite, favorites,
                                                                        lastindex, temp6))
                    rooter.six.grid(row=3, column=2)
                count = 7

                print("HELLO ", i)
                print("DING DONG DONE")
        return lastindex







from tkinter import Entry
import tkinter as tk
from TwitterBot import executefavorites

def post(entrypic):
        item2 = tk.Tk()
        item2.wm_title("Window")
        item2.geometry("200x200")
        l = Label(item2, text="What Text do you want your tweet to say?")
        e1 = Entry(item2)
        e1.grid(row=1, column=0)
        l.grid(row=0, column=0)
        if os.path.exists('temp.png'):
            os.remove('temp.png')
        decodeit = open('temp.png', 'wb')
        decodeit.write(base64.b64decode((entrypic)))
        b = Button(item2, text="Submit", command= lambda: executefavorites('temp.png', e1.get()))
        b.grid(row=2, column=0)
       #b2.grid(row=3, column=0)



















