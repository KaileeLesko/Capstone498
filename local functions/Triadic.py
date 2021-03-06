import colormap
from AdditionalColors import additonalColors
from auxsillaryFunctions import RGB2HSL


def Triadic(color):
    R, G, B = colormap.hex2rgb(color)

    H, S, L = RGB2HSL(R, G, B)

    array = [color]
    start = 120
    end = 240
    while start <= end:
        H1 = (H + start)
        if (H1 >= 360):
            H1 -= 360

        print(H1)
        R, G, B = colormap.hls2rgb(H1 / 360, L, S)
        R = R * 255
        G = G * 255
        B = B * 255

        color = colormap.rgb2hex(round(R), round(G), round(B))
        array.append(color)
        start += 120

    array = additonalColors(array)
    return array
