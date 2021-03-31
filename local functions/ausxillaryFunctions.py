def hex_to_rgb(value):
    print(value, " value")
    value = value.lstrip('#')
    print(list(int(value[i:i + 2], 16) for i in (0, 2, 4)))
    return list(int(value[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


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
    favorites=[]
    c.execute("SELECT * FROM favoriteImages")
    favorite= c.fetchall()
    print("favorite ", favorite)
    for i in range(0, len(favorite)):
        if favorite[i][0] == Constants.setUser():
            favorites.append(favorite[i])
    print("deleted")
    lastindex=4
    nextsix(lastindex, rooter, favorites, favorite)


from tkinter import Label,Button
def nextsix(lastindex, rooter,favorites,favorite):
        print("reached next six")
        global photo3, photo1, photo2, photo4, photo5, photo6
        global one, two, three, four, five, six
        if (lastindex== len(favorite)):
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
                        rooter.one = Button(rooter, image=photo1, command= lambda: remover(i, favorites, lastindex, rooter, favorite, favorites[temp1][1]))
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
                        rooter.two = Button(rooter, image=photo2, command= lambda: remover(i, favorites, lastindex, rooter, favorite, favorites[temp2][1]))
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
                        rooter.three = Button(rooter, image=photo3, command= lambda: remover(i, favorites, lastindex, rooter, favorite, favorites[temp3][1]))
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
                        rooter.four = Button(rooter, image=photo4, command= lambda: remover(i, favorites, lastindex, rooter, favorite, favorites[i][1]))
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
                        temp4=i
                        photo5 = ImageTk.PhotoImage(newimg)
                        rooter.five = Button(rooter, image=photo5, command= lambda: remover(i, favorites, lastindex, rooter, favorite, favorites[temp4][1]))
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
                        temp5=i
                        photo6 = ImageTk.PhotoImage(newimg)
                        rooter.six = Button(rooter, image=photo6, command= lambda: remover(i, favorites, lastindex, rooter, favorite, favorites[temp5][1]))
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
            if (count == 1):
                if i >= len(favorites):
                    converted_string = base64.b64encode(open("myImage.png", "rb").read())
                    favorites.append(['hello', converted_string])
                lastindex = i
                if os.path.exists('one.png'):
                    os.remove('one.png')
                decodeit = open('one.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('one.png')
                newimg = newimg.resize((600, 100))

                photo1 = ImageTk.PhotoImage(newimg)
                rooter.one = Label(rooter, image=photo1)
                rooter.one.grid(row=3, column=2)
                count = 2
            elif (count == 2):
                if i >= len(favorites):
                    converted_string = base64.b64encode(open("myImage.png", "rb").read())
                    favorites.append(['hello',converted_string])
                if os.path.exists('two.png'):
                    os.remove('two.png')
                decodeit = open('two.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('two.png')
                newimg = newimg.resize((600, 100))

                photo2 = ImageTk.PhotoImage(newimg)
                rooter.two = Button(rooter, image=photo2, command= lambda: remove(i, favorites, lastindex, rooter, favorite, favorites[i][1]))
                rooter.two.grid(row=2, column=2)
                count = 3
            elif (count == 3):
                if i >= len(favorites):
                    converted_string = base64.b64encode(open("myImage.png", "rb").read())
                    favorites.append(['hello', converted_string])
                if os.path.exists('three.png'):
                    os.remove('three.png')
                decodeit = open('three.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('three.png')
                newimg = newimg.resize((600, 100))

                photo3 = ImageTk.PhotoImage(newimg)
                rooter.three = Label(rooter, image=photo3)
                rooter.three.grid(row=1, column=2)
                count = 4
            elif (count == 4):
                if i >= len(favorites):
                    converted_string = base64.b64encode(open("myImage.png", "rb").read())
                    favorites.append(['hello', converted_string])
                if os.path.exists('four.png'):
                    os.remove('four.png')
                decodeit = open('four.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('four.png')
                newimg = newimg.resize((600, 100))
                photo4 = ImageTk.PhotoImage(newimg)
                rooter.four = Button(rooter, image=photo4, command= lambda: remove(i, favorites, lastindex, rooter, favorite, favorites[i][1]))
                rooter.four.grid(row=3, column=1)
                count = 5
            elif (count == 5):
                if i >= len(favorites):
                    converted_string = base64.b64encode(open("myImage.png", "rb").read())
                    favorites.append(['hello', converted_string])
                if os.path.exists('five.png'):
                    os.remove('five.png')
                decodeit = open('five.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('five.png')
                newimg = newimg.resize((600, 100))

                photo5 = ImageTk.PhotoImage(newimg)
                rooter.five = Button(rooter, image=photo5, command= lambda: remove(i, favorites, lastindex, rooter, favorite, favorites[i][1]))
                rooter.five.grid(row=2, column=1)
                count = 6
            elif count == 6:
                if i >= len(favorites):
                    converted_string = base64.b64encode(open("myImage.png", "rb").read())
                    favorites.append(['hello',converted_string])
                if os.path.exists('six.png'):
                    os.remove('six.png')
                decodeit = open('six.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('six.png')
                newimg = newimg.resize((600, 100))

                photo6 = ImageTk.PhotoImage(newimg)
                rooter.six = Button(rooter, image=photo6, command= lambda: remove(i, favorites, lastindex, rooter, favorite, favorites[i][1]))
                rooter.six.grid(row=1, column=1)
                count = 7

                print("DING DONG DONE")
                print("HELLO ", i)

    return lastindex
