from PIL import Image, ImageDraw, ImageFont,ImageFilter

im=Image.open("/Users/yousef/Desktop/atlas.png")

#blurring an image
blurImage1=im.filter(ImageFilter.BLUR)   #just blurs an image
blurImage2=im.filter(ImageFilter.GaussianBlur(90)) #blurs the image and allows u to sepfciy the dgree of bluriing
blurImage3=im.filter(ImageFilter.EDGE_ENHANCE) #enchances the edges
blurImage4=im.filter(ImageFilter.EMBOSS) #embosses the image
blurImage5=im.filter(ImageFilter.CONTOUR)  #contours the image
blurImage6=im.filter(ImageFilter.SHARPEN)  #shaprens

blurImage6.show()
