import colormap
from ausxillaryFunctions import RGB2HSL
import random



def monochrome(color):
    R, G, B = colormap.hex2rgb(color)
    print("RGB", R, G, B)
    H, S, L = RGB2HSL(R, G, B)
    print("Start Hue", H)
    array = [color]
    while len(array) < 6:
        H1 = H + random.choice([5, -5])
        if (H1 >= 360):
            H1 -= 360
        S = random.random()
        L = random.random()

        print("HSL IS", H1, S, L)

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
