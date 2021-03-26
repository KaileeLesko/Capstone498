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
from tkinter import Label
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
                if (count == 1):

                    if os.path.exists('one.png'):
                        os.remove('one.png')
                    decodeit = open('one.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('one.png')
                    newimg = newimg.resize((600, 100))

                    photo1 = ImageTk.PhotoImage(newimg)
                    rooter.one = Label(rooter, image=photo1)
                    rooter.one.grid(row=1, column=1)
                    count = 2
                elif (count == 2):

                    if os.path.exists('two.png'):
                        os.remove('two.png')
                    decodeit = open('two.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('two.png')
                    newimg = newimg.resize((600, 100))

                    photo2 = ImageTk.PhotoImage(newimg)
                    rooter.two = Label(rooter, image=photo2)
                    rooter.two.grid(row=2, column=1)
                    count = 3
                elif (count == 3):

                    if os.path.exists('three.png'):
                        os.remove('three.png')
                    decodeit = open('three.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('three.png')
                    newimg = newimg.resize((600, 100))

                    photo3 = ImageTk.PhotoImage(newimg)
                    rooter.three = Label(rooter, image=photo3)
                    rooter.three.grid(row=3, column=1)
                    count = 4
                elif (count == 4):

                    if os.path.exists('four.png'):
                        os.remove('four.png')
                    decodeit = open('four.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('four.png')
                    newimg = newimg.resize((600, 100))
                    photo4 = ImageTk.PhotoImage(newimg)
                    rooter.four = Label(rooter, image=photo4)
                    rooter.four.grid(row=1, column=2)
                    count = 5
                elif (count == 5):

                    if os.path.exists('five.png'):
                        os.remove('five.png')
                    decodeit = open('five.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('five.png')
                    newimg = newimg.resize((600, 100))

                    photo5 = ImageTk.PhotoImage(newimg)
                    rooter.five = Label(rooter, image=photo5)
                    rooter.five.grid(row=2, column=2)
                    count = 6
                elif count==6:

                    if os.path.exists('six.png'):
                        os.remove('six.png')
                    decodeit = open('six.png', 'wb')

                    decodeit.write(base64.b64decode((favorites[i][1])))
                    decodeit.close()
                    newimg = Image.open('six.png')
                    newimg = newimg.resize((600, 100))

                    photo6 = ImageTk.PhotoImage(newimg)
                    rooter.six = Label(rooter, image=photo6)
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

                if os.path.exists('two.png'):
                    os.remove('two.png')
                decodeit = open('two.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('two.png')
                newimg = newimg.resize((600, 100))

                photo2 = ImageTk.PhotoImage(newimg)
                rooter.two = Label(rooter, image=photo2)
                rooter.two.grid(row=2, column=2)
                count = 3
            elif (count == 3):

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

                if os.path.exists('four.png'):
                    os.remove('four.png')
                decodeit = open('four.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('four.png')
                newimg = newimg.resize((600, 100))
                photo4 = ImageTk.PhotoImage(newimg)
                rooter.four = Label(rooter, image=photo4)
                rooter.four.grid(row=3, column=1)
                count = 5
            elif (count == 5):

                if os.path.exists('five.png'):
                    os.remove('five.png')
                decodeit = open('five.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('five.png')
                newimg = newimg.resize((600, 100))

                photo5 = ImageTk.PhotoImage(newimg)
                rooter.five = Label(rooter, image=photo5)
                rooter.five.grid(row=2, column=1)
                count = 6
            elif count == 6:

                if os.path.exists('six.png'):
                    os.remove('six.png')
                decodeit = open('six.png', 'wb')

                decodeit.write(base64.b64decode((favorites[i][1])))
                decodeit.close()
                newimg = Image.open('six.png')
                newimg = newimg.resize((600, 100))

                photo6 = ImageTk.PhotoImage(newimg)
                rooter.six = Label(rooter, image=photo6)
                rooter.six.grid(row=1, column=1)
                count = 7

                print("DING DONG DONE")
                print("HELLO ", i)

    return lastindex

