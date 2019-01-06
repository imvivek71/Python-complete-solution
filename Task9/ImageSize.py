from PIL import Image

im = Image.open('whatever.png')
width, height = im.size
print("size", width, " ", height)
