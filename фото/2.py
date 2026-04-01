from PIL import Image

original_img = Image.open('5.jpg')

width, height = original_img.size #получаем размеры
new_width = int(width / 3) #уменьшаем в три раза
new_height = int(height / 3)

small_img = original_img.resize((new_width, new_height)) #resize -> новое изображение с такими-то данными


small_img.save('small.jpg')
#отражаем по горизонтали
mirror_horizontal = original_img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_horizontal.save('mirror1.jpg')

#отражаем по вертикали
mirror_vertical = original_img.transpose(Image.FLIP_TOP_BOTTOM)
mirror_vertical.save('mirror2l.jpg')

print("Всо")