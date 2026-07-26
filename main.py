from drink import Drink
from database import create_table, insert_order, view_orders,search_orders_by_customer,update_order,delete_order

test_drink = Drink("Espresso", 300, "Coffee")

print(test_drink.name)
print(test_drink.price)
print(test_drink.category)

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

    create_table()  # to ensure database and table are created in irl not my delusions


    print("====== Welcome to ByteBean ======")

    customer_name = input("Please enter your name: ")

    cart = []

    while True:

        show_menu(drink_menu)

        # Category Validation
        while True:
            category = input("\nSelect a category (1-4): ")

            if category in drink_menu:
                break

            print("Invalid category! Please try again.")

        show_drinks(drink_menu, category)

        # Drink Validation
        while True:
            drink = input("\nSelect your drink: ")

            if drink in drink_menu[category]["items"]:
                break

            print("Invalid drink! Please try again.")

        # Quantity Validation
        while True:
            try:
                num_of_cups = int(input("How many cups would you like to order? "))

                if num_of_cups > 0:
                    break

                print("Quantity must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        selected_item = drink_menu[category]["items"][drink]

        total_amount = selected_item["price"] * num_of_cups

        cart.append({
            "category": drink_menu[category]["category"],
            "name": selected_item["name"],
            "price": selected_item["price"],
            "quantity": num_of_cups,
            "total": total_amount
        })

        insert_order(
            customer_name,
            drink_menu[category]["category"],
            selected_item["name"],
            selected_item["price"],
            num_of_cups,
            total_amount
)

        # Order Again Validation
        while True:
            again = input("Would you like to order another drink? (yes/no): ").strip().lower()

            if again == "yes":
                break

            elif again == "no":
                break

            else:
                print("Please enter yes or no.")

        if again == "no":
            break

    grand_total, discount_percent, discount, final_amount = calculate_discount(cart)

    print_receipt(
        customer_name,
        cart,
        grand_total,
        discount_percent,
        discount,
        final_amount
    )


def display_orders():
    orders = view_orders()  # to view all orders in the database

    if not orders:
        print("No orders found.")
        return

    print("\n======= All Orders =======")

    for order in orders:
        print("------------------------------------")
        print(f"Order ID      : {order[0]}")
        print(f"Customer Name : {order[1]}")
        print(f"Category      : {order[2]}")
        print(f"Drink         : {order[3]}")
        print(f"Price         : Rs.{order[4]}")
        print(f"Quantity      : {order[5]}")
        print(f"Total         : Rs.{order[6]}")


def search_orders():
    customer_name=input("Enter customer name : ")

    orders= search_orders_by_customer(customer_name)

    if not orders:
        print("No orders found")
        return

    for order in orders:
     print("------------------------------------")
     print(f"Order ID      : {order[0]}")
     print(f"Customer Name : {order[1]}")
     print(f"Category      : {order[2]}")
     print(f"Drink         : {order[3]}")
     print(f"Price         : Rs.{order[4]}")
     print(f"Quantity      : {order[5]}")
     print(f"Total         : Rs.{order[6]}")
    

def update_order_menu():

    order_id = int(input("Enter Order ID: "))
    customer_name = input("Enter customer name: ")
    category = input("Enter category: ")
    drink = input("Enter drink: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    update_order(
        order_id,
        customer_name,
        category,
        drink,
        price,
        quantity,
        total
    )

    print("Order updated successfully!")
    display_orders()



def delete_order_menu():
    order_id = int(input("Enter your order id:"))

    delete_order(order_id)

    print("Order deleted successfully !")
    display_orders()



print("Please visit again!")
print("====================================")

def menu():

    while True:

        print("\n========== BYTEBEAN ==========")
        print("1. Place New Order")
        print("2. View All Orders")
        print("3. Search Orders")
        print("4. Update Order")
        print("5. Delete Order")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            main()

        elif choice == "2":
            display_orders()

        elif choice == "3":
            search_orders()

        elif choice == "4":
            update_order_menu()

        elif choice == "5":
            delete_order_menu()

        elif choice == "6":
            print("\nThank you for visiting ByteBean ☕")
            break

        else:
            print("\nInvalid choice! Please try again.")



if __name__ == "__main__":
    create_table()  
    menu()
