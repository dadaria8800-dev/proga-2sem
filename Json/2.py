import json

with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

name = input("введите название: ")
price = int(input("введите цену: "))
weight = int(input("введите вес: "))
available = input("есть в наличии? (да/нет): ")

# превращаем ответ в True или False
if available == "да":
    available = True
else:
    available = False

# создаем словарь нового продукта
new_product = {
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
}

# добавляем в список продуктов
data['products'].append(new_product)

# сохраняем обратно в файл
with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("\nПродукт добавлен! Новый список продуктов:\n")

for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")

    if product['available'] == True:
        print("В наличии")
    else:
        print("Нет в наличии!")
