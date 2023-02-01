from PIL import Image, ImageFilter

# img = Image.open('images/pikachu.jpg')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# # print(dir(img))

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("images/filtered/blur.png", 'png')

# filtered_img = filtered_img.filter(ImageFilter.SHARPEN)  # BLUR, SHARPEN,
# filtered_img.save("images/filtered/sharp.png", 'png')


# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# crooked.save("images/filtered/grey.png", 'png')

# resize = img.resize((300, 300))
# resize.save("images/filtered/resized.jpeg", 'jpeg')

# box = (100, 100, 400, 400)
# region = img.crop(box)
# region.save("images/filtered/crop.png", 'png')
# region.show()

beach = Image.open('images/jackson-david-lWq_Fx7qLzg-unsplash.jpg')
# beach.show()
# new_img = beach.resize((200, 400))
print(beach)
beach.thumbnail((400, 400))
print(beach)
beach.save('images/filtered/thumbnail.jpg')
beach.show()
# print(beach.size)
beach.
