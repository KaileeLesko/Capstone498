from colormap import hex2rgb
from AdditionalColors import additonalColors
from ausxillaryFunctions import RGB2HSL
import colormap


def tetradic(color):
    R, G, B = hex2rgb(color)

    H, S, L = RGB2HSL(R, G, B)

    array = [color]
    start = 90
    end = 270
    while start <= end:
        H1 = (H + start)
        if (H1 >= 360):
            H1 -= 360

        R, G, B = colormap.hls2rgb(H1 / 360, L, S)
        R = R * 255
        G = G * 255
        B = B * 255

        color = colormap.rgb2hex(round(R), round(G), round(B))
        array.append(color)
        start += 90

    array = additonalColors(array)
    return array
