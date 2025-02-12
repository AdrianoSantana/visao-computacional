from PIL import Image
import os

cwd = os.getcwd()
INPUT_PATH = os.path.abspath(f"{cwd}/data")
OUTPUT_PATH = os.path.abspath(f"{cwd}/data_output")

def in_file(filename):
    return os.path.join(INPUT_PATH, filename)

def out_file(filename):
    return os.path.join(OUTPUT_PATH, filename)