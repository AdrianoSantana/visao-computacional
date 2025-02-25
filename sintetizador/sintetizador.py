from PIL import Image
import os

cwd = os.getcwd()
filePath = os.path.abspath(f"{cwd}/data/banananelson.jpg")


image = Image.new('RGB', (1080, 920), (255, 255, 0))


def triangle(size):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    image = Image.new("RGB", (size, size), WHITE)

    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x, y), BLACK)

    return image

def french_flag(height):
    BLUE = (0,85,164)
    WHITE = (255,255,255)
    RED = (239,65,53)

    width = 3*height//2
    image = Image.new("RGB", (width, height), WHITE)

    offset = width//3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2*offset, y), RED)
    return image


def japanese_flag(height):
    width = 3*height//2
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)

    r = 3*height//10
    c = (width//2, height//2)

    image = Image.new('RGB', (width, height), WHITE)

    for x in range(c[0]-r, c[0]+r):
        for y in range(c[1]-r, c[1]+r):
            if (x - c[0])**2 + (y - c[1])**2 <= r**2:
                image.putpixel((x, y), RED)

    return image
if __name__ == "__main__":
    jp = japanese_flag(2040)
    jp.show()
