# cоздаем класс
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    # метод, сообщает что ресторан открыт
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

newRestaurant = Restaurant("фудкорт", "фастфуд")

print(f"Название: {newRestaurant.restaurant_name}")
print(f"Кухня: {newRestaurant.cuisine_type}")

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()