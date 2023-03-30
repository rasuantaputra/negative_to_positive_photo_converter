from PIL import Image, ImageOps

# Open the negative photo
photo = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']

for i in photo:
    ImageOps.invert(Image.open(i)).save('convert-'+i)
