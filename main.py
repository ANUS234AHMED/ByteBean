print("====== Welcome to ByteBean ======")

name = input("Please enter your name: ")

print("====== Menu ======")
print("1. Coffee")
print("2. Tea")
print("3. Juice")
print("4. Water")
print("5. Exit")

opt=input(f"Hello, {name}! Please select an option from the menu.")

num_of_cups = int(input("How many cups would you like to order?"))

total_amount = opt * num_of_cups

if opt == "1":
    print("You selected Coffee.")
    total_amount = 300*num_of_cups
elif opt == "2":
    print("You selected Tea.")
    total_amount = 200*num_of_cups  

elif opt     == "3":
    print("You selected Juice.")
    total_amount = 250*num_of_cups

elif opt == "4":
    print("You selected Water.")
    total_amount = 100*num_of_cups

elif opt == "5":
    print("Thank you for visiting ByteBean. Goodbye!")
   


if total_amount > 1000:
    print("You are eligible for a 10% discount!")
    total_amount = total_amount * 0.9


print("====== Receipt ======")
print("Customer Name: ", name)
print("Number of cups ordered: ", num_of_cups)
print("Selected option: ", opt)
print("Your total amount is: ", total_amount)