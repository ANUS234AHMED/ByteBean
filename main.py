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



def show_menu(drink_menu):
    print("\n======= BYTEBEAN MENU =======")

    for key, value in drink_menu.items():
        print(f"{key}. {value['category']}")

def show_drinks(drink_menu,category):
    
    print(f"\n----- {drink_menu[category]['category']} Menu -----")

    for key, value in drink_menu[category]["items"].items():
        print(f"{key}. {value['name']} - Rs.{value['price']}")

def print_receipt(customer_name,cart,grand_total, discount_percent, discount, final_amount):
    print("\n====================================")
    print("        BYTEBEAN RECEIPT")
    print("====================================")

    print(f"Customer Name : {customer_name}")

    for order in cart:
       print("------------------------------------")
       print(f"Category : {order['category']}")
       print(f"Drink    : {order['name']}")
       print(f"Price    : Rs.{order['price']}")
       print(f"Quantity : {order['quantity']}")
       print(f"Total    : Rs.{order['total']}")


    print("------------------------------------")
    print(f"Grand Total      : Rs.{grand_total}")
    print(f"Discount ({discount_percent}%) : Rs.{discount:.2f}")
    print(f"Final Amount     : Rs.{final_amount:.2f}")
    print("====================================")
    print("Thank you for visiting ByteBean ☕")

def calculate_discount(cart):
    
    
    grand_total = sum(order["total"] for order in cart)
    discount = 0
    discount_percent = 0

    if grand_total >= 1000:
       discount_percent = 10
       discount = grand_total * 0.10
       print("\nCongratulations! You received a 10% discount!")

    elif grand_total >= 500:
        discount_percent = 5
        discount = grand_total * 0.05
        print("\nCongratulations! You received a 5% discount!")

    else:
         print("\nNo discount applied. Orders above Rs.500 get a discount.")

    final_amount = grand_total - discount

    return grand_total, discount_percent, discount, final_amount

def main():

    print("====== Welcome to ByteBean ======")
    
    customer_name = input("Please enter your name: ")

    cart = []

    while True:

      show_menu(drink_menu)   
      category = input("\nSelect a category (1-4): ")

      if category not in drink_menu:
        print("Invalid category!")
        exit()

      show_drinks(drink_menu, category)

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

    grand_total, discount_percent, discount, final_amount = calculate_discount(cart)

    print_receipt(customer_name, cart, grand_total, discount_percent, discount, final_amount)

    print("Please visit again!")
    print("====================================")

main()
