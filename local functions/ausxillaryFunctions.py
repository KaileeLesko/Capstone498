
def hex_to_rgb(value):
    print(value, " value")
    value = value.lstrip('#')
    print(list(int(value[i:i+2], 16) for i in (0, 2, 4)))
    return list(int(value[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb