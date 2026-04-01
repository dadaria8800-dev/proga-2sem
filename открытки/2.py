from PIL import Image

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
    #показываем выбронную открытку
    img = Image.open(otkritki[vybor])
    img.show()

    print(f'открытка для праздника "{vybor}"')
else:
    print('такого нет:(')