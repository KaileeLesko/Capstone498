from colormap import hex2rgb
from AdditionalColors import additonalColors
from ausxillaryFunctions import RGB2HSL
import colormap


def tetradic(color):
    R, G, B = hex2rgb(color)
    print("RGB", R, G, B)
    H, S, L = RGB2HSL(R, G, B)
    print("Start Hue", H)
    array = [color]
    start = 90
    end = 270
    while start <= end:
        H1 = (H + start)
        if (H1 >= 360):
            H1 -= 360

        print("HSL IS", H1, S, L)

        print(H1)
        R, G, B = colormap.hls2rgb(H1 / 360, L, S)
        R = R * 255
        G = G * 255
        B = B * 255
        print("THIS IS RGB", R, G, B)

        color = colormap.rgb2hex(round(R), round(G), round(B))
        array.append(color)
        start += 90
        print("loop")
    array = additonalColors(array)
    return array
