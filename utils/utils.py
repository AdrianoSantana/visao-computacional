from PIL import Image
import os
import numpy as np

cwd = os.getcwd()
INPUT_PATH = os.path.abspath(f"{cwd}/data")
OUTPUT_PATH = os.path.abspath(f"{cwd}/data_output")

def in_file(filename):
    return os.path.join(INPUT_PATH, filename)

def out_file(filename):
    return os.path.join(OUTPUT_PATH, filename)

def show_vertical(img1, img2):
    im = Image.fromarray(np.hstack((np.array(img1), np.array(img2))))
    im.show()
    
def compare_images(img_one, img_two):
    first = Image.open(img_one)
    second = Image.open(img_two)
    
    show_vertical(first, second)
    