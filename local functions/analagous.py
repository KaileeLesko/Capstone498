from ausxillaryFunctions import RGB2HSL
import colormap


#generates analagous colors (colors next to each other on the wheel)

def analagous(color):
    R, G, B = colormap.hex2rgb(color)

    H, S, L = RGB2HSL(R, G, B)
    print("S IS",S)

    array = [color]
    start = 15
    i = 6
    while len(array) < 6:
        H1 = (H + start)
        if (H1 >= 360):
            H1 -= 360
        R, G, B = colormap.hls2rgb(H1 / 360, L, S)
        R = R * 255
        G = G * 255
        B = B * 255
        color = colormap.rgb2hex(round(R), round(G), round(B))
        array.append(color)
        start += 15
    return array
