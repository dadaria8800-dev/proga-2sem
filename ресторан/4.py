# создаем класс Уборщик
class Cleaner:
    def __init__(self, name):
        self.name = name  # имя уборщика

    def clean(self):
        print(f"Уборщик {self.name} делает уборку в ресторане!")


# класс ресторан с уборщиком
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # добавляем нового уборщика
        self.cleaner = Cleaner("Егорик")

    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт!")


    # заставить уборщика работать
    def do_cleaning(self):
        print(f"В ресторане {self.restaurant_name} начинается уборка!")
        self.cleaner.clean()  # вызываем метод уборщика


my_rest = Restaurant("макдоналс", "Фастфуд")

my_rest.describe_restaurant()  # выводим информацию о ресторане
my_rest.do_cleaning() # заставляем уборщика работать