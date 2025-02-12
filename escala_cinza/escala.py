import sys
import os
from PIL import Image
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from utils import in_file, out_file

def avg_grayscale(colored_image):
    widht, height = colored_image.size
    gray_image = Image.new("RGB", (widht, height))
    for x in range(widht):
        for y in range(height):
            pxl = colored_image.getpixel((x, y))
            luminensce = (pxl[0] + pxl[1] + pxl[2])//3
            gray_image.putpixel((x, y), (luminensce, luminensce, luminensce))

    return gray_image


def grayscale(colored_image):
    widht, height = colored_image.size
    gray_image = Image.new("RGB", (widht, height))
    for x in range(widht):
        for y in range(height):
            pxl = colored_image.getpixel((x, y))
            luminensce = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2])
            gray_image.putpixel((x, y), (luminensce, luminensce, luminensce))

    return gray_image

if __name__ == "__main__":
    img = Image.open(in_file("banananelson.jpg"))    
    imgGrey = grayscale(img)
    imgGrey.save(out_file("banananelson-grey.jpg"))