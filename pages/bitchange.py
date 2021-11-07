#!/usr/local/bin/python3
from PIL import Image

def bitchange():

    # Load the image and convert to 32-bit RGBA
    im = Image.open("C:/Users/BTLsub/realsite/media/input/원본.jpg").convert('RGB')

    # Save result
    im.save("C:/Users/BTLsub/realsite/media/input/원본.jpg")