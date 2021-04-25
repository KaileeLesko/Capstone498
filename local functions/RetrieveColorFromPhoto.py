import random

#referenced this website: https://www.andrewshay.me/blog/find-most-common-color-in-image-with-python/

def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


def colorFromPhoto(img):
    #the colors are rounded here to prevent duplicates or almost identical looking colors
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

            for i in range(len(colors)):

                if not r_set:
                    r = closest(colors, r)
                    r_set= True


                if not g_set:
                    g= closest(colors,g)
                    g_set= True
                if not b_set:
                    b = closest(colors, b)
                    b_set= True

                if all((r_set, g_set, b_set)):
                    break

            new_rgb = (r, g, b)
            img.putpixel((w, h), new_rgb)

            if new_rgb in color_count:
                color_count[new_rgb] += 1
            else:
                color_count[new_rgb] = 1
    #end borrowed reference

    lister = []
    for item in color_count:
        lister.append([item, color_count[item]])

    for i in range(len(lister)):
        lister[i] = lister[i]
    for k in range(len(lister)):
        lister[k] = '#{:02x}{:02x}{:02x}'.format(lister[k][0][0], lister[k][0][1], lister[k][0][2])


    array = []
    i = 0
    if (len(lister) <= 6):
        return lister+ ['#ffffff','#ffffff','#ffffff','#ffffff','#ffffff','#ffffff','#ffffff']

    while len(array) < 6:
        randomed = random.choice(lister)
        if (randomed not in array):
            array.append(randomed)


    return array
