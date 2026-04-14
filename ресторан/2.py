class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

restaurant1 = Restaurant("Итальянский дворик", "Итальянская")
restaurant2 = Restaurant("Суши", "Японская")
restaurant3 = Restaurant("Бургирыы", "Американская")

print("Ресторан 1:")
restaurant1.describe_restaurant()

print("Ресторан 2:")
restaurant2.describe_restaurant()

print("Ресторан 3:")
restaurant3.describe_restaurant()