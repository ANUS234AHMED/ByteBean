print("====== Welcome to ByteBean ======")

customer_name = input("Please enter your name: ")

drink_menu = {
    "1": {
        "category": "Coffee",
        "items": {
            "1": {"name": "Espresso", "price": 300},
            "2": {"name": "Cappuccino", "price": 200},
            "3": {"name": "Latte", "price": 250},
            "4": {"name": "Americano", "price": 100}
        }
    },

    "2": {
        "category": "Tea",
        "items": {
            "1": {"name": "Green Tea", "price": 300},
            "2": {"name": "Black Tea", "price": 200},
            "3": {"name": "Oolong Tea", "price": 250},
            "4": {"name": "Chamomile Tea", "price": 100}
        }
    },

    "3": {
        "category": "Juice",
        "items": {
            "1": {"name": "Orange Juice", "price": 300},
            "2": {"name": "Apple Juice", "price": 200},
            "3": {"name": "Grape Juice", "price": 250},
            "4": {"name": "Pineapple Juice", "price": 100}
        }
    },

    "4": {
        "category": "Water",
        "items": {
            "1": {"name": "Mineral Water", "price": 300},
            "2": {"name": "Sparkling Water", "price": 200},
            "3": {"name": "Spring Water", "price": 250},
            "4": {"name": "Distilled Water", "price": 100}
        }
    }
}

# Create the cart ONCE
cart = []

while True:

    print("\n======= BYTEBEAN MENU =======")

    for key, value in drink_menu.items():
        print(f"{key}. {value['category']}")

    category = input("\nSelect a category (1-4): ")

    if category not in drink_menu:
        print("Invalid category!")
        exit()

    print(f"\n----- {drink_menu[category]['category']} Menu -----")

    for key, value in drink_menu[category]["items"].items():
        print(f"{key}. {value['name']} - Rs.{value['price']}")

    drink = input("\nSelect your drink: ")

    if drink not in drink_menu[category]["items"]:
        print("Invalid drink!")
        exit()

    num_of_cups = int(input("How many cups would you like to order? "))

    selected_item = drink_menu[category]["items"][drink]

    total_amount = selected_item["price"] * num_of_cups

    cart.append({
    "category": drink_menu[category]["category"],
    "name": selected_item["name"],
    "price": selected_item["price"],
    "quantity": num_of_cups,
    "total": total_amount
})

    again = input("Would you like to order another drink? (yes/no): ").lower()

    if again != "yes":
        break

for order in cart:
    print(f"{order['quantity']} x {order['name']} ({order['category']}) - Rs.{order['total']}")