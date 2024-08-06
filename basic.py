from PIL import Image 

#Create an image via import
image = Image.open('gato.jpg')

# #analyze the image
# print(image.size)
# print(image.filename)
# print(image.format)

# # flip/rotate image
# image = image.transpose(Image.Transpose.ROTATE_90)

# Show the image
image.show()

cat_rotated = image.rotate(30)
cat_rotated.save('cat_rotated.png', 'png')