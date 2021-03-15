import random
import colorsys
import colormap
import ausxillaryFunctions

import random
import colorsys
def monochrome(color):
    R, G, B = colormap.hex2rgb(color)
    print("RGB", R, G, B)
    H, S, L = RGB2HSL(R, G, B)
    print("Start Hue", H)
    array = [color]
    while len(array)<6:
        H1= H+random.choice([5,-5])
        if (H1 >=360):
            H1-=360
        S= random.random()
        L= random.random()

        print("HSL IS", H1, S, L)

        # H1=  math.fmod(H1 + 0.25, 1.0)
        R, G, B = colormap.hls2rgb(H1 / 360, L, S)
        R = R * 255
        G = G * 255
        B = B * 255
        print("THIS IS RGB", R, G, B)
        color = colormap.rgb2hex(round(R), round(G), round(B))
        if (color not in array):
            array.append(color)

        print("loop")
    return array


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






