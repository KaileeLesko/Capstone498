from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

def hex_to_rgb(value):
    value = value.lstrip('#')
    print(list(int(value[i:i+2], 16) for i in (0, 2, 4)))
    return list(int(value[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

@app.route("analagous")
def analagous():
    import colorsys
    color = "#003874"
    color = hex_to_rgb(color)
    print("COLOR: ", str(color))
    R = int(color[0])
    G = int(color[1])
    B = int(color[2])
    h, s, v = colorsys.rgb_to_hsv(R, G, B)
    h2 = (h * 360 + 60) % 360 / 360

    h3 = (h * 360 + 30) % 360 / 360

    H, S, V = colorsys.hsv_to_rgb(h, s, v)
    A, B, C = colorsys.hsv_to_rgb(h2, s, v)
    D, E, F = colorsys.hsv_to_rgb(h3, s, v)

    H = int(H)
    S = int(S)
    V = int(V)
    HSV = str(H) + str(S) + str(V)

    A = int(A)
    B = int(B)
    C = int(C)

    D = int(D)
    E = int(E)
    F = int(F)
    print(H, S, V)
    print("Analagous: ")
    color1 = '#{:02x}{:02x}{:02x}'.format(H, S, V)
    color2 = '#{:02x}{:02x}{:02x}'.format(A, B, C)
    color3 = '#{:02x}{:02x}{:02x}'.format(D, E, F)
    return [color1, color2, color3]



print(str(analagous))