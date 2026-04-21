# класс ресторан из прошлого задания
class Restaurant:
    def __init__(self, name, kuhnya):
        self.name = name
        self.kuhnya = kuhnya


# новый класс кафе-мороженое (берет всё из Restaurant)
class IceCreamStand(Restaurant):
    def __init__(self, name, kuhnya):
        super().__init__(name, kuhnya)
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное"]  # список сортов

    def show_flavors(self):
        print(self.flavors)  # просто печатаем список


my_cafe = IceCreamStand("мороженка", "сладкая")

my_cafe.show_flavors()