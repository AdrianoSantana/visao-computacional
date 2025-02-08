from PIL import Image
from PIL import ImageFilter
import numpy as np
import os

def show_vertical(img1, img2):
    im = Image.fromarray(np.hstack((np.array(img1), np.array(img2))))
    im.show()
    im.save('filtro.jpg')

cwd = os.getcwd()
filePath = os.path.abspath(f"{cwd}/data/banananelson.jpg")
image = Image.open(filePath)

filtered = image.filter(ImageFilter.CONTOUR)
show_vertical(image, filtered) 
