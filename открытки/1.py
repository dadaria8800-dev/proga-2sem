from PIL import Image
img = Image.open('otkritka.jpg')

#чат гпт:
left = 20    # отступ слева
top = 200       # отступ сверху
right = 300  # правая граница (ширина - сколько пикселей оставить)
bottom = 400  # нижняя граница (высота - сколько пикселей оставить)


cropped_img = img.crop((left, top, right, bottom))#вот тут по тем цифоркам обрезается
cropped_img.save('babochka.jpg')

