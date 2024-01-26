# Import PIL
from PIL import Image, ImageOps

# create image
im1 = Image.open("/Users/yousef/Desktop/atlas.png")

# flip vertically
im2 = ImageOps.flip(im1)

# flip horizontally
im3 = ImageOps.mirror(im1)

# turn image into gray scale
im4 = ImageOps.grayscale(im1)

# invert image
im5 = ImageOps.invert(im1)



