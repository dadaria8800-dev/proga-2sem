import json

with open('products.json', 'r', encoding='utf-8') as file: #открываем файл для чтения и переводим в числа( что бы компутер прочитал)
    data = json.load(file) #превращаем JSON в словарь питона

# Проходим по каждому продукту
for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")

    # Проверяем, есть ли в наличии
    if product['available'] == True:
        print("В наличии")
    else:
        print("Нет в наличии!")

    print() #пустая строка для красоты