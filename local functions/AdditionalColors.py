import random
import colorsys
import colormap
import ausxillaryFunctions

def additonalColors(array):
    arrays=array
    while len(arrays)<6:
        color= random.choice(arrays)
        R, G, B = colormap.hex2rgb(color)
        print("RGB", R, G, B)
        H, S, L = RGB2HSL(R, G, B)
        print("Start Hue", H)
        array = [color]
        ranges= [15,30,45,60]
        range= random.choice(ranges)
        H1 = (H + range)
        if (H1 >= 360):
            H1 -= 360
        R, G, B = colormap.hls2rgb(H1 / 360, L, S)
        R = R * 255
        G = G * 255
        B = B * 255
        print("THIS IS RGB", R, G, B)

        color1 = colormap.rgb2hex(round(R), round(G), round(B))
        if (color1 not in arrays):
            arrays.append(color1)
    return arrays


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
