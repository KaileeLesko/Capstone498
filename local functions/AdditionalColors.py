import random
import colormap
from ausxillaryFunctions import RGB2HSL

def additonalColors(array):
    arrays = array
    while len(arrays) < 6:
        color = random.choice(arrays)
        R, G, B = colormap.hex2rgb(color)
        print("RGB", R, G, B)
        H, S, L = RGB2HSL(R, G, B)
        print("Start Hue", H)
        ranges = [15, 30, 45, 60]
        range = random.choice(ranges)
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


