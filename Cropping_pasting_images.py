from PIL import Image, ImageDraw, ImageFont

im=Image.open("/Users/yousef/Desktop/atlas.png")

#defines the locations/coordinates
#the order is horizontalSP,VerticalSP,HorizontalED,VerticalED
box=(100,188,547,591);

#here u are starting the cropping action
croppedImage=im.crop(box);
# croppedImage.show()

#pasting
im.paste(croppedImage,(0,0));
im.paste(croppedImage,(40,40));
im.show();
