from PIL import Image, ImageDraw, ImageFont

img = Image.open('3.jpg')

layer = Image.new('RGBA', img.size, (0, 0, 0, 0))  #слой для текста

draw = ImageDraw.Draw(layer)
font = ImageFont.truetype("arial.ttf", 80)

#вот это хз откуда взялось и как считается это все нейронка
text = "bybybyy"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (img.width - text_width) // 2  # координаты по центру
y = (img.height - text_height) // 2

draw.text((x, y), text, fill=(255, 255, 255, 128), font=font)

result = Image.alpha_composite(img.convert('RGBA'), layer) #накладываем слой с текстом на картинку
result.save('watermarked.png')

print('всо')