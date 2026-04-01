from PIL import Image, ImageDraw, ImageFont

otkritki = {
    'новый год': 'noviy_god.jpg',
    '8 марта': '8_marta.jpg',
    '23 февраля': '23_fevralya.jpg',
    'день рождения': 'den_rozhdeniya.jpg',
}

print('какие праздники есть:')
for prazdnik in otkritki.keys():
    print(f'- {prazdnik}')

vybor = input('к какому празднику нужна открытка? ')


if vybor in otkritki:
    name = input('введите имя того, кого хотите поздравить: ')

    img = Image.open(otkritki[vybor])

    img_rgba = img.convert('RGBA')
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    text = f'{name}, поздравляю)'

    font = ImageFont.truetype("arial.ttf", 100) #шрифт, размер

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    #тут типо снизу по центру, хз гпт
    x = (img.width - text_width) // 2
    y = img.height - text_height - 50

    # Делаем текст жирным через наложение
    # Рисуем текст 4 раза со смещением (с первой страницы в гугле)ы
    draw.text((x, y), text, font=font, fill=(255, 0, 0, 255))
    draw.text((x + 1, y), text, font=font, fill=(255, 0, 0, 255))
    draw.text((x, y + 1), text, font=font, fill=(255, 0, 0, 255))
    draw.text((x + 1, y + 1), text, font=font, fill=(255, 0, 0, 255))

    # Накладываем текст на картинку
    result = Image.alpha_composite(img_rgba, layer)

    result.save('otkritka_s_imenem.png')
    result.show()

    print('всо, открытка сохранена как otkritka_s_imenem.png')

else:
    print('такого праздника нет в списке(')