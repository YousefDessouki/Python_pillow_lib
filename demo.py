from PIL import Image
#firstly you are importing all the neseecary libtraies which is image from pillow

#Here u are importing the images and assiging it to a variable
im=Image.open(r"/Users/yousef/Desktop/atlas.png")

#here u are showing the image
im.show()

#shows the format/extension
print(im.format)

#shows the colour contribution to the image
print(im.mode)

#gets the size
print(im.size)
print(im.width)
print(im.height)
print(im.info)

#wanna save the image in a new format
im.save("atlas.gif")

