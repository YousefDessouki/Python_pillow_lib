from PIL import Image, ImageDraw, ImageFont,ImageFilter,ImageColor
#here u created an image
image=Image.new("RGB",(512,512),ImageColor.getrgb("#ffffffff"))

#get the image size and save it
width,height=image.size

for x in range(height):
    image.putpixel((x,x),(0,0,0,255));
    image.putpixel((x,-x), (0, 0, 0, 255));

image.putpixel((100,100),(255,0,0,255))
image.show()
