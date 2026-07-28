from drink import Drink

class Order:

    def __init__(self, customer_name, drink, quantity):
        self.customer_name = customer_name
        self.drink = drink
        self.quantity = quantity
        self.total = drink.calculate_total(quantity)

    def display(self):
        print(f"{self.customer_name} - {self.drink} x {self.quantity} -")

    def update_order(self,new_customer_name, new_drink, updated_quantity):
        self.customer_name = new_customer_name
        self.drink = new_drink
        self.quantity = updated_quantity
        self.total = self.drink.calculate_total(self.quantity)

    def __str__(self):
        return f"{self.customer_name} - {self.drink} ({self.quantity})"

    
    