import random
from PIL import Image


def colorFromPhoto(img):
    # this function pulls out 6 random colors from the photo



    # round the colors to these values :
    colors = [255, 223, 191, 159, 127, 95, 63, 31, 0]
    color_count = {}
    original_color_count = {}
    width, height = img.size
    for w in range(width):
        for h in range(height):
            current_color = img.getpixel((w, h))

            if current_color in original_color_count:
                original_color_count[current_color] += 1
            else:
                original_color_count[current_color] = 1

            r, g, b, c = current_color
            r_set = False
            g_set = False
            b_set = False

            #  Loop through our allowed values and find the closest value to snap to
            for i in range(len(colors)):
                color_one = colors[i]
                color_two = colors[i + 1]

                if not r_set:
                    if color_one >= r >= color_two:
                        distance_one = color_one - r
                        distance_two = r - color_two
                        r = color_one if distance_one <= distance_two else color_two
                        r_set = True

                if not g_set:
                    if color_one >= g >= color_two:
                        distance_one = color_one - g
                        distance_two = g - color_two
                        g = color_one if distance_one <= distance_two else color_two
                        g_set = True

                if not b_set:
                    if color_one >= b >= color_two:
                        distance_one = color_one - b
                        distance_two = b - color_two
                        b = color_one if distance_one <= distance_two else color_two
                        b_set = True

                if all((r_set, g_set, b_set)):
                    break

            # Set our new pixel back on the image to see the difference
            new_rgb = (r, g, b)
            img.putpixel((w, h), new_rgb)

            if new_rgb in color_count:
                color_count[new_rgb] += 1
            else:
                color_count[new_rgb] = 1

    lister = []
    finallist = []
    for item in color_count:
        lister.append([item, color_count[item]])

    for i in range(len(lister)):
        lister[i] = lister[i]
    for k in range(len(lister)):
        lister[k]=  '#{:02x}{:02x}{:02x}'.format(lister[k][0][0], lister[k][0][1], lister[k][0][2])
    print(lister)

    array=[]
    i=0
    while len(array)< 6:
        randomed= random.choice(lister)
        if (randomed not in array):
            array.append(randomed)

    print(array)
    return array
