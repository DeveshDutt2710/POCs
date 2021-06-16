
# first argument is the file name and second argument defines the output quality in terms of percentage(1-100)
# python changeImageResolution.py profile.jpeg 10


from PIL import Image
import sys
import os

image_path = sys.argv[1]
quality = (int)(sys.argv[2])

image_file = Image.open(image_path)
  

image_file.save("saved_image.jpg", quality=quality)
  