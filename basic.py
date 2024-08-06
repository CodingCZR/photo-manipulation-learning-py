from PIL import Image 

#Create an image via import
image = Image.open('gato.jpg')

#analyze the image
print(image.size)

# Show the image
image.show()