class Restaurant:
    def __init__(self, name, kuhnya):
        self.name = name
        self.kuhnya = kuhnya


class IceCreamStand(Restaurant):
    def __init__(self, name, kuhnya):
        super().__init__(name, kuhnya)
        # а) атрибуты
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное"]
        self.location = "Парк"  # локация
        self.work_time = "10:00 - 22:00"  # время работы
        # г) типы мороженого
        self.stick = ["Эскимо"]  # на палочке
        self.soft = ["Мягкое ванильное"]  # мягкое

    # показать сорта
    def show_flavors(self):
        print("Сорта:", self.flavors)

    # б) добавить сорт
    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print("Добавили сорт:", new_flavor)

    # б) удалить сорт
    def remove_flavor(self, flavor):
        self.flavors.remove(flavor)
        print("Удалили сорт:", flavor)

    # в) проверить наличие
    def has_flavor(self, flavor):
        if flavor in self.flavors:
            print("Да, сорт есть!")
        else:
            print("Нет, такого сорта нет")

    # г) показать мороженое на палочке
    def show_stick(self):
        print("На палочке:", self.stick)

    # г) добавить мороженое на палочке
    def add_stick(self, new_item):
        self.stick.append(new_item)
        print("Добавили в на палочке:", new_item)

    def show_soft(self):
        print("Мягкое:", self.soft)

    def add_soft(self, new_item):
        self.soft.append(new_item)
        print("Добавили в мягкое:", new_item)


# Создаем кафе
cafe = IceCreamStand("Мороженка", "Сладкая")

# Проверяем всё
print("Название:", cafe.name)
print("Кухня:", cafe.kuhnya)
print("Локация:", cafe.location)
print("Время работы:", cafe.work_time)
print()

cafe.show_flavors()
cafe.add_flavor("Карамельное")
cafe.show_flavors()
cafe.remove_flavor("Шоколадное")
cafe.show_flavors()
print()

cafe.has_flavor("Ванильное")
cafe.has_flavor("Фисташковое")
print()

cafe.show_stick()
cafe.add_stick("Фруктовый лед")
cafe.show_stick()
print()

cafe.show_soft()
cafe.add_soft("Шоколадное мягкое")
cafe.show_soft()