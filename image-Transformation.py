from PIL import Image, ImageDraw, ImageFont

# create image
im1 = Image.open("/Users/yousef/Desktop/atlas.png")

#rotate the original pic with the designated degree
im1=im1.rotate(0)


#resize the pic
im1=im1.resize((100,100))

im1.show()