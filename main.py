print("====== Welcome to ByteBean ======")

name = input("Please enter your name: ")

print("====== Menu ======")
print("1. Coffee")
print("2. Tea")
print("3. Juice")
print("4. Water")
print("5. Exit")



drink_name ={ "1": "Coffee", "2": "Tea", "3": "Juice", "4": "Water" }

drink_price = { "1": 300, "2": 200, "3": 250, "4": 100 }

opt=input(f"Hello, {name}! Please select an option from the menu. ")

num_of_cups = int(input("How many cups would you like to order? " ))


if opt in drink_name:
    print(f"You have selected {drink_name[opt]}.\n")
    total_amount = drink_price[opt] * num_of_cups
elif opt == "5":    
    print("Thank you for visiting ByteBean! Have a great day!")
    exit()

original_total = total_amount

# Determine discount percent 
discount_per = 0
if original_total >= 5000:
    discount_per = 20
elif original_total >= 3000:
    discount_per = 15
elif original_total > 1000:
    discount_per = 10

# Calculate discount amount and final total
discount_amount = round((discount_per / 100) * original_total, 2)
final_total = round(original_total - discount_amount, 2)

if discount_per > 0:
    print(f"You are eligible for a {discount_per}% discount!\n\n\n")

print("====== Receipt ======")

print("Customer Name: ", name, "\n")

print("Number of cups ordered: ", num_of_cups, "\n")

print("Selected option: ", drink_name[opt], "\n")

print("Your total amount is: ", final_total, "\n")

print(f"You got {discount_per}% discount on your order.\n \n \n")

print("=========Thank you for your order!\n Please visit again.==========", "\n \n \n")
