import random
import colormap

def coolColors():
    returner = []
    while len(returner) < 6:
        red = random.randint(0, 129)
        green = random.randint(0, 255)
        blue = random.randint(128, 255)
        color = colormap.rgb2hex(round(red), round(green), round(blue))
        if color not in returner:
            returner.append(color)
    return returner
