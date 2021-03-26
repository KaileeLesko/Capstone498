from PIL import Image
import cv2


def create(color1, color2, color3, color4, color5, color6):
    img = Image.new("RGBA", (200, 200), color1)
    img1 = Image.new("RGBA", (200, 200), color2)
    img2 = Image.new("RGBA", (200, 200), color3)
    img3 = Image.new("RGBA", (200, 200), color4)
    img4 = Image.new("RGBA", (200, 200), color5)
    img5 = Image.new("RGBA", (200, 200), color6)
    img.save('img.png')
    img1.save('img1.png')
    img2.save('img2.png')
    img3.save('img3.png')
    img4.save('img4.png')
    img5.save('img5.png')
    img1 = cv2.imread('img.png')
    img2 = cv2.imread('img1.png')
    img3 = cv2.imread('img2.png')
    img4 = cv2.imread('img3.png')
    img5 = cv2.imread('img4.png')
    img6 = cv2.imread('img5.png')
    im_h = cv2.hconcat([img1, img2, img3, img4, img5, img6])
    cv2.imwrite('myImage.png', im_h)



from PIL import Image
import cv2


def createwhite():
    img = Image.new("RGBA", (200, 200), '#ffffff')
    img1 = Image.new("RGBA", (200, 200), '#ffffff')
    img2 = Image.new("RGBA", (200, 200), '#ffffff')
    img3 = Image.new("RGBA", (200, 200), '#ffffff')
    img4 = Image.new("RGBA", (200, 200), '#ffffff')
    img5 = Image.new("RGBA", (200, 200), '#ffffff')
    img.save('img.png')
    img1.save('img1.png')
    img2.save('img2.png')
    img3.save('img3.png')
    img4.save('img4.png')
    img5.save('img5.png')
    img1 = cv2.imread('img.png')
    img2 = cv2.imread('img1.png')
    img3 = cv2.imread('img2.png')
    img4 = cv2.imread('img3.png')
    img5 = cv2.imread('img4.png')
    img6 = cv2.imread('img5.png')
    im_h = cv2.hconcat([img1, img2, img3, img4, img5, img6])
    cv2.imwrite('whiteIMG.png', im_h)

