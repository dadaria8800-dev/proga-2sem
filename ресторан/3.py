class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0  # начальный рейтинг

    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт!")

    # метод для обновления рейтинга
    def set_rating(self, new_rating):
        self.rating = new_rating
        print(f"Новый рейтинг ресторана {self.restaurant_name}: {self.rating}")


my_rest = Restaurant("Пельмешки", "Русская")

# проверяем начальный рейтинг
my_rest.describe_restaurant()
print()

# меняем рейтинг
my_rest.set_rating(10)
print()

# смотрим результат
my_rest.describe_restaurant()