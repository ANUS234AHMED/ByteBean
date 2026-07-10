name =input("Enter your name: ")
take_order = input("What would you love to order : \n 1. coffee \n 2. tea \n 3. juice\n")
num_of_cups=int(input("How many cups would you like to have?"))

coffee=250
tea= 190
juice=170


total_amount= num_of_cups * coffee
if total_amount > 1000:
    total_amount = total_amount- (total_amount * 0.1)





if take_order == "1":
    print(f"----------- \n customer name:{name} \n order: {take_order} \n number of cups: {num_of_cups} \n total amount: {total_amount} \n -----------")
    
elif take_order == "2":
    total_amount = num_of_cups * tea
    print(f"----------- \n customer name:{name} \n order: {take_order} \n number of cups: {num_of_cups} \n total amount: {total_amount} \n -----------")
    
elif take_order == "3":
    total_amount = num_of_cups * juice
    print(f"----------- \n customer name:{name} \n order: {take_order} \n number of cups: {num_of_cups} \n total amount: {total_amount} \n -----------")
    