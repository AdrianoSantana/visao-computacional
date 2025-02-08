from PIL import Image
import os

cwd = os.getcwd()
filePath = os.path.abspath(f"{cwd}/data/banananelson.jpg")
image = Image.open(filePath)

print(image.getpixel((100, 100)))
image.show()