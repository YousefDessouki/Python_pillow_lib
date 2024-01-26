from PIL import Image, ImageDraw, ImageFont,ImageFilter,ImageColor
#here u created an image
image=Image.new("RGB",(512,512),ImageColor.getrgb("#ffffffff"))

draw=ImageDraw.Draw(image)
#draws a line
draw.line([(0,0),(100,100)],fill="red",width=5)

#draws an ecilpse
#
draw.ellipse((50,100,150,200),fill="blue",outline=(0,0,0))


#rectangle
draw.rectangle((200,100,300,200),fill="green",outline=(0,0,0))

image.show()
