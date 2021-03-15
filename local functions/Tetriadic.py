# import random
import colorsys
import ausxillaryFunctions
# import matplotlib
# import complimentary
import math
from difflib import SequenceMatcher
from colormap import hex2rgb
from AdditionalColors import additonalColors
from colormap import rgb2hex
import colormap


def tetradic(color):
    R, G, B = hex2rgb(color)
    print("RGB",R,G,B)
    H,S,L= RGB2HSL(R,G,B)
    print("Start Hue", H)
    array = [color]
    start =  90
    end =  270
    while start <= end:
        H1=(H+ start)
        if (H1 >= 360):
            H1-=360

        print("HSL IS",H1,S,L)

        # H1=  math.fmod(H1 + 0.25, 1.0)
        print(H1)
        R,G,B= colormap.hls2rgb(H1/360,L,S)
        R= R*255
        G= G*255
        B= B*255
        print("THIS IS RGB",R,G,B)

        color = colormap.rgb2hex(round(R),round(G),round(B))
        array.append(color)
        start += 90
        print("loop")
    array= additonalColors(array)
    return array


# H, S, V = ausxillaryFunctions.hex_to_rgb(color)
# H,S,L = RGB2HSL(H,S,V)
# array = []
# white = 0xffffff
# color= color[1:]
# color5= "0x"+color[1:]
# color6= white-int(color5,16)
# color6 = '#' + str(color6)[2:]
# color6 = color6[0:7]
# array.append(color6)
# print(H,S,L)
# i = 90
# stop = 271
#
# H1=H
# H1 = (H1 + 90)%360
# print(H1)
# R, G, B = HSL2RGB(H1,S,V)
# print("RGB IS",R, G, B)
# R = int(R)
# B = int(B)
# G = int(G)
# color1='#{:02x}{:02x}{:02x}'.format(R, G, B)
# color1=color1[0:7]
# array.append(color1)
# H1 = (H1 + 180) % 360
# print(H1)
# R, G, B = HSL2RGB(H1, S, V)
# print("RGB IS", R, G, B)
# R = int(R)
# B = int(B)
# G = int(G)
# color1 = '#{:02x}{:02x}{:02x}'.format(R, G, B)
# color1[0:7]
# array.append(color1)
# color7 = "0x" + str(color1)[1:]
# color2= white-int(color7,16)
# color2= '#'+ str(color2)[2:]
# color2=color2[0:7]
# array.append(color2)
#


def HSL2RGB(H, S, L):
    if L < 0.5:
        temporary_1 = L * (1.0 + S)
    else:
        temporary_1 = L + S - L * S
    temporary_2 = 2 * L - temporary_1
    H = H / 360
    temporary_R = H + 0.333
    temporary_G = H
    temporary_B = H - 0.333
    if (temporary_B < 0):
        temporary_B += 1
    if (temporary_G < 0):
        temporary_G += 1
    if (temporary_R < 0):
        temporary_R += 1
    if (6 * temporary_R < 1):
        Red = temporary_2 + (temporary_1 - temporary_2) * 6 * temporary_R
    elif (2 * temporary_R < 1):
        Red = temporary_1
    elif (3 * temporary_R < 2):
        Red = temporary_2 + (temporary_1 - temporary_2) * (0.666 - temporary_R) * 6
    else:
        Red = temporary_2

    if (6 * temporary_G < 1):
        Green = temporary_2 + (temporary_1 - temporary_2) * 6 * temporary_G
    elif (2 * temporary_G < 1):
        Green = temporary_1
    elif (3 * temporary_G < 2):
        Green = temporary_2 + (temporary_1 - temporary_2) * (0.666 - temporary_G) * 6
    else:
        Green = temporary_2
    if (6 * temporary_B < 1):
        Blue = temporary_2 + (temporary_1 - temporary_2) * 6 * temporary_B
    elif (2 * temporary_B < 1):
        Blue = temporary_1
    elif (3 * temporary_B < 2):
        Blue = temporary_2 + (temporary_1 - temporary_2) * (0.666 - temporary_B) * 6
    else:
        Blue = temporary_2
    print("COLOR IS ", str([int(Red * 255), int(Blue * 255), int(Green * 255)]))
    return [Red * 255, Blue * 255, Green * 255]


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

    HueChoices= [R,G,B]
    Hue= max(HueChoices)
    if Hue == R:
        H= (G -B) / (maxB - minR)
        H=H*60
    if Hue == G:
        H=2.0 + (B -R) / (maxB - minR)
        H=H*60
    else:
        H= 4.0 + (R - G) / (maxB - minR)
        H*= 60
    if H < 0:
        H += 360
    return [H, S, L]
