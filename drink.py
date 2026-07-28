class Drink:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        print(f"{self.name} - Rs.{self.price} ({self.category})")

    def calculate_total(self, quantity):
        return self.price * quantity 

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"{self.name} - Rs.{self.price} ({self.category})"