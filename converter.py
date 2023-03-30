from PIL import Image, ImageOps

# Open the negative photo
photo = []

# change range depend on total picture
for i in range(1,6):
    photo.append("" + str(i) + ""+".jpg")

for i in photo:
    ImageOps.invert(Image.open(i)).save('convert-'+i)
