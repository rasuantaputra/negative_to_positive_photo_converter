from PIL import Image, ImageOps

# Open the negative photo
negative_image = Image.open('image.jpg')

# Convert the negative photo to positive by inverting the colors
positive_image = ImageOps.invert(negative_image)

# Save the positive photo
positive_image.save('positive_photo.png')
