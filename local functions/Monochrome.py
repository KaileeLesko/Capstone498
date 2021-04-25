import colormap
from auxsillaryFunctions import RGB2HSL
import random

def monochrome(color):
    R, G, B = colormap.hex2rgb(color)
    print("R G B", R,G,B)
    H, S, L = RGB2HSL(R, G, B)
    print("H S L ", H,S,L)
    print(H,S,L)
    array = [color]
    while len(array) < 6:
        H1 = H
        S = random.random()
        L= random.random()

        R, G, B = colormap.hls2rgb(H1 / 360, L, S)

        R = R * 255
        G = G * 255
        B = B * 255

        color = colormap.rgb2hex(round(R), round(G), round(B))
        if (color not in array):
            array.append(color)
    return array
