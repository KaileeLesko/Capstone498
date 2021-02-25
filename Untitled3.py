#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import colorsys
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io import imread, imsave, imshow, show, imread_collection, imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.pylab as plt
import matplotlib
from scipy.ndimage import affine_transform, zoom
from scipy import misc
import cv2


# In[41]:


def hex_to_rgb(value):
    value = value.lstrip('#')
    print(list(int(value[i:i+2], 16) for i in (0, 2, 4)))
    return list(int(value[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def colorFromPhoto():
    # this function pulls out 6 random colors from the photo

    # open the photo
    img = Image.open(r"C:\Users\Kailuu\Pictures\my photo.png")

    # round the colors to these values :
    colors = [255, 223, 191, 159, 127, 95, 63, 31, 0]
    color_count = {}
    original_color_count = {}
    width, height = img.size
    for w in range(width):
        for h in range(height):
            current_color = img.getpixel((w, h))

            if current_color in original_color_count:
                original_color_count[current_color] += 1
            else:
                original_color_count[current_color] = 1

            r, g, b, c = current_color
            r_set = False
            g_set = False
            b_set = False

            #  Loop through our allowed values and find the closest value to snap to
            for i in range(len(colors)):
                color_one = colors[i]
                color_two = colors[i + 1]

                if not r_set:
                    if color_one >= r >= color_two:
                        distance_one = color_one - r
                        distance_two = r - color_two
                        r = color_one if distance_one <= distance_two else color_two
                        r_set = True

                if not g_set:
                    if color_one >= g >= color_two:
                        distance_one = color_one - g
                        distance_two = g - color_two
                        g = color_one if distance_one <= distance_two else color_two
                        g_set = True

                if not b_set:
                    if color_one >= b >= color_two:
                        distance_one = color_one - b
                        distance_two = b - color_two
                        b = color_one if distance_one <= distance_two else color_two
                        b_set = True

                if all((r_set, g_set, b_set)):
                    break

            # Set our new pixel back on the image to see the difference
            new_rgb = (r, g, b)
            img.putpixel((w, h), new_rgb)

            if new_rgb in color_count:
                color_count[new_rgb] += 1
            else:
                color_count[new_rgb] = 1

    lister = []
    finallist = []
    for item in color_count:
        lister.append([item, color_count[item]])

    for i in range(len(lister)):
        lister[i] = lister[i]

    for item in color_count:
        tempstring = (" {} {} ".format(item, color_count[item]))
        finer = tempstring.find(")")
        finallist.append([tempstring[2:finer], tempstring[finer + 1:]])
    i = 0
    newlist = []

    check = True
    while check == True:
        if len(newlist) != 10:
            randomed = random.choice(finallist)
            if randomed not in newlist:
                newlist.append(randomed)
        else:
            check = False
    hexlist = []
    returnlist = []
    for i in range(10):
        find1 = newlist[i][0].find(',')
        find2 = newlist[i][0].find(',', find1 + 2, len(newlist[i][0]))
        stringer = str(newlist[i][0])
        stringer = stringer.replace(",", "", 2)
        stringer = stringer.replace("'", "", 5)
        spaceOne = stringer.find(" ")
        spaceTwo = stringer.find(" ", spaceOne + 1, len(stringer))
        answer = hex(int(stringer[0:spaceOne])) + " " + hex(int(stringer[spaceOne + 1:spaceTwo])) + hex(
            int(stringer[spaceTwo + 1:]))
        answer = answer.replace(" ", "")
        answer = answer.replace("0x", "", 3)
        returnlist.append(answer)
    return answer


def analagous(c1x, c1y):
    import colorsys
    color = "#003874"
    color = hex_to_rgb(color)
    print("COLOR: " ,str(color))
    R= int(color[0])
    G= int(color[1])
    B= int(color[2])
    h, s, v = colorsys.rgb_to_hsv(R,G,B)
    h2 = (h * 360 + 60) % 360 / 360

    h3 = (h * 360 + 30) % 360 / 360

    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    A, B, C = colorsys.hsv_to_rgb(h2, s, v)
    D, E, F = colorsys.hsv_to_rgb(h3, s, v)
    
    H= int(H)
    S= int(S)
    V= int(V)
    HSV = str(H)  + str(S)+ str(V)
    
    A= int(A)
    B= int(B)
    C= int(C)
    
    D= int(D)
    E= int(E)
    F= int(F)
    print(H,S,V)
    print("Analagous: ")
    color1 ='#{:02x}{:02x}{:02x}'.format(H,S,V)
    color2 = '#{:02x}{:02x}{:02x}'.format(A,B,C)
    color3 = '#{:02x}{:02x}{:02x}'.format(D,E,F)
    return [color1, color2, color3]



def comp(c1x, c1y):

    img = Image.open(r"C:\Users\Kailuu\Pictures\wheeler.png")
    img.convert("RGB")

    A, B, C, D = img.getpixel((c1x, c1y))

    r = int(str(A))
    g = int(str(B))
    b = int(str(B))
    
    

    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    print(h,s,v)
    h2 = (h * 360 + 180) % 360 / 360
    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    A, B, C = colorsys.hsv_to_rgb(h2, s, v)
    print(H,S,V)
    H= int(H)
    S= int(S)
    V= int(V)

    A= int(A)
    B= int(B)
    C= int(C)
    
  
    print("Complementary: ")
     color1 ='#{:02x}{:02x}{:02x}'.format(H,S,V)
    color2 = '#{:02x}{:02x}{:02x}'.format(A,B,C)
    return color1,color2

def splitComplementary(c1x,c1y):

    img = Image.open(r"C:\Users\Kailuu\Pictures\wheeler.png")
    img.convert("RGB")

    A, B, C, D = img.getpixel((c1x, c1y))

    r = int(str(A))
    g = int(str(B))
    b = int(str(B))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h2 = (h * 360 + 150) % 360 / 360
    h3 = (h * 360 +210) % 360 / 360
    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    A, B, C = colorsys.hsv_to_rgb(h2, s, v)
    D,E,F = colorsys.hsv_to_rgb(h3, s, v)

    H= int(H)
    S= int(S)
    V= int(V)

    A= int(A)
    B= int(B)
    C= int(C)
    
    D= int(D)
    E= int(E)
    F= int(F)

    color1 = (str(hex(H))[2:] + str(hex(S))[2:] + str(hex(V))[2:])
    color2 = (str(hex(A))[2:] + str(hex(B))[2:] + str(hex(C))[2:])
    color3 = (str(hex(D))[2:] + str(hex(E))[2:] + str(hex(F))[2:])

    print("Split Complementary:" )
    return color1,color2,color3


def  Triadic(c1x, c1y):

    img = Image.open(r"C:\Users\Kailuu\Pictures\wheeler.png")
    img.convert("RGB")

    A, B, C, D = img.getpixel((c1x, c1y))

    r = int(str(A))
    g = int(str(B))
    b = int(str(B))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h2 = (h * 360 + 120) % 360 / 360
    h3 = (h * 360 + 240) % 360 / 360
    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    A, B, C = colorsys.hsv_to_rgb(h2, s, v)
    D, E, F = colorsys.hsv_to_rgb(h3, s, v)
    
    H= int(H)
    S= int(S)
    V= int(V)

    A= int(A)
    B= int(B)
    C= int(C)
    
    D= int(D)
    E= int(E)
    F= int(F)

    color1 = '#{:02x}{:02x}{:02x}'.format(H,S,V )
    color2 = (str(hex(A))[2:] + str(hex(B))[2:] + str(hex(C))[2:])
    color3 = (str(hex(D))[2:] + str(hex(E))[2:] + str(hex(F))[2:])

    print("Triadic:")
    return color1, color2, color3


def  tetradic(c1x, c1y):

    img = Image.open(r"C:\Users\Kailuu\Pictures\wheeler.png")
    img.convert("RGB")

#     A, B, C, D = img.getpixel((c1x, c1y))

    r = int(str(A))
    g = int(str(B))
    b = int(str(B))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h1 = (h * 360 + 90) % 360 / 360
    h2 = (h * 360 +  180) % 360 / 360
    h3 = (h * 360 + 270) % 360 / 360
    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    A, B, C = colorsys.hsv_to_rgb(h1, s, v)
    D, E, F = colorsys.hsv_to_rgb(h2, s, v)
    G,I,J = colorsys.hsv_to_rgb(h3, s, v)
#     H= int(H)
#     S= int(S)
#     V= int(V)

    A= int(A)
    B= int(B)
    C= int(C)
    
    D= int(D)
    E= int(E)
    F= int(F)
    G= int(G)
    I= int(I)
    J= int(J)
    

    color1 = (str(hex(H))[2:] + str(hex(S))[2:] + str(hex(V))[2:])
    color2 = (str(hex(A))[2:] + str(hex(B))[2:] + str(hex(C))[2:])
    color3 = (str(hex(D))[2:] + str(hex(E))[2:] + str(hex(F))[2:])
    color4 = (str(hex(G))[2:] + str(hex(I))[2:] + str(hex(J))[2:])

    print("Tetradic:")
    return color1, color2, color3,color4

def monochrome(c1x,c1y):
#     img = Image.open(r"C:\Users\Kailuu\Pictures\wheeler.png")
#     img.convert("RGB")
    colorList=[]
#     A, B, C, D = img.getpixel((c1x, c1y))
    

    r = int(str(A))
    g = int(str(B))
    b = int(str(B))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    colorList.append([h,s,v])
    truth = True
    while truth == True:
        if len(colorList) < 7:
            temp= ([h, random.randint(0,100),random.randint(0,100)])
            if temp not in colorList:
                colorList.append(temp)
        else:
            truth= False
    finalList=[]
    for i in range(0,7):
        H,S,B = colorsys.hsv_to_rgb(.8,int(colorList[i][1]), int(colorList[i][2]))
    
        print(H,S,B)
        
    
        answer = (str(hex(H)[2:4]) + str(hex(S)[3:5])+ str(hex(B))[3:5])
        finalList.append(answer)
        
#     a(str(hex(A)[2:4]) + str(hex(B)[2:4])+ str(hex(C))[2:4])
    #print("monochrome: ")
    
    return colorList


# In[40]:



c1x = 239
c1y = 1089

print(analagous(c1x,c1y))

print(" ")
print(comp(c1x,c1y))

print(" ")
print(splitComplementary(c1x,c1y))

print(" ")
print(tetradic(c1x,c1y))

print(" ")
print(Triadic(c1x,c1y))

print(monochrome(c1x,c1y))


# In[ ]:


print(colorFromPhoto())


# In[ ]:





# In[ ]:





# In[ ]:




