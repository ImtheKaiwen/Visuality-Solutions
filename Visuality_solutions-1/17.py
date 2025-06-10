from PIL import Image

image = Image.open("pic.jpg")

width, height = image.size

print(f'{width}x{height}')