with open('en-ru.txt', 'r', encoding='utf-8') as file: #
    lines = file.readlines()

# создаем пустой словарь для записи перевода
ru_en = {}

for line in lines:
    # убираем лишние пробелы и переносы
    line = line.strip()

    # разделяем английскую и русскую части
    parts = line.split(' - ')
    english = parts[0]  # английское слово
    russian_part = parts[1]  # русские переводы

    # разделяем русские переводы по запятой
    russian_words = russian_part.split(', ')

    # для каждого русского слова добавляем запись в словарь
    for russian in russian_words:
        if russian in ru_en:
            # добавляем английский вариант через запятую
            ru_en[russian] = ru_en[russian] + ', ' + english
        else:
            # создаем новую запись
            ru_en[russian] = english

# сортируем русские слова по алфавиту
sorted_words = sorted(ru_en.keys())

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for russian in sorted_words:
        file.write(f"{russian} -- {ru_en[russian]}\n")

print("Словарь создан! Файл ru-en.txt готов!")