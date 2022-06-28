from PIL import Image
from matplotlib import pyplot


def colorToGrayscale(colorimg):
    img = Image.open(colorimg)
    name = input('Name the new gray file(without extension): ')
    destination = Image.new('L',(img.width, img.height),255)
    for pixcolm in range(img.height):
        for pixrow in range(img.width):
            rgb = img.convert('RGB')
            R, G, B = rgb.getpixel((pixrow, pixcolm))
            Gray = round(0.299 * R + 0.587 * G + 0.114 * B)
            print(Gray)


colorToGrayscale('Hello.bmp')
