from PIL import Image
im = Image.open('img/stars.jpg')

width, height = im.size

im = im.crop((0 + (width / 2 - 540), 0 + (height / 2 - 540), width - (width / 2 - 540), height - (height / 2 - 540)))

width, height = im.size

print(width, height)

im = im.convert('1')

im.save('img/stars_processed.jpg')
im.show()
# print(left, upper, right, lower)
# print(height)
