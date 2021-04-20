import colorsys
import ausxillaryFunctions


#this file creates colors 180 degrees apart on the color wheel

def threeAnalagous(color, color1, color2):
    array = []
    color = ausxillaryFunctions.hex_to_rgb(color
                                           )
    color1 = ausxillaryFunctions.hex_to_rgb(color1
                                            )
    color2 = ausxillaryFunctions.hex_to_rgb(color2
                                            )
    R = int(color[0])
    G = int(color[1])
    B = int(color[2])
    h, s, v = colorsys.rgb_to_hsv(R, G, B)
    h = (h * 360 + 30) % 360 / 360

    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    H = int(H)
    S = int(S)
    V = int(V)
    val = '#{:02x}{:02x}{:02x}'.format(H, S, V)

    array.append(val)
    R = int(color1[0])
    G = int(color1[1])
    B = int(color1[2])
    h, s, v = colorsys.rgb_to_hsv(R, G, B)
    h = (h * 360 + 30) % 360 / 360

    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    H = int(H)
    S = int(S)
    V = int(V)
    color1 = '#{:02x}{:02x}{:02x}'.format(H, S, V)
    array.append(color1)
    R = int(color2[0])
    G = int(color2[1])
    B = int(color2[2])
    h, s, v = colorsys.rgb_to_hsv(R, G, B)
    h = (h * 360 + 30) % 360 / 360

    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    H = int(H)
    S = int(S)
    V = int(V)
    color1 = '#{:02x}{:02x}{:02x}'.format(H, S, V)

    array.append(color1)

    return array


def compAndAnalagous(color):

    array = []
    color = color[1:]

    color = ausxillaryFunctions.hex_to_rgb(color)

    array.append(color)
    A, B, C = colorsys.hex_to_rgb(color)

    r = int(str(A))
    g = int(str(B))
    b = int(str(B))

    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h2 = (h * 360 + 180) % 360 / 360
    H, S, V = colorsys.hsv_to_rgb(h, s, v)


    H = int(H)
    S = int(S)
    V = int(V)

    color = '#{:02x}{:02x}{:02x}'.format(H, S, V)
    array.append(color)
    return array
