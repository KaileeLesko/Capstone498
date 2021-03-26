from ausxillaryFunctions import RGB2HSL
import colormap


def analagous(color):
    R, G, B = colormap.hex2rgb(color)
    print("RGB", R, G, B)
    H, S, L = RGB2HSL(R, G, B)
    print("Start Hue", H)
    array = [color]
    start = 15
    i = 6
    while len(array) < 6:
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
        start += 15
        print("loop")
    return array
