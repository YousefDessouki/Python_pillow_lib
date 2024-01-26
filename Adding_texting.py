from PIL import Image, ImageDraw, ImageFont

im=Image.open(r"/Users/yousef/Desktop/atlas.png")

#takes a copy to edit on
d1=ImageDraw.Draw(im)

#load the font u wanna use
myfont=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',140)

#adds the parameter to edit on the image
d1.text((28,36),"HelloWorld",font=myfont,fill=(255,255,255))

im.show()
