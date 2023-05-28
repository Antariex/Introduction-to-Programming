#I change the add/remove functionality to also ask for numbers of units of each item, and adaptted the view cart functionality accordingly.

welcome = print("Welcome to the Shopping Cart Program!")

cart = []
prices = []

while True:
    options = input("\nPlease select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\n\nPlease enter an action:\n")
    
#Adding an item to the shopping cart:
    if options == "1":
     item = input("What item would you like to add? ")
     cart.append(item)
     price = float(input(f"What is the price of {item}? "))
     units = int(input(f"How many units of {item} would you like to add? "))
     prices.append(price * units)
     print(f"'{item}' has been added to the cart.")

#Show the items on the shopping cart:     
    elif options == "2":
        if len(cart) == 0:
            print("The shopping cart is empty!")
        else:
            print("The contents of the shopping cart are:")
            for item in range(len(cart)):
                print(f"{item+1}. {cart[item]} * {units} units.")

#Remove an item of the shopping cart:
    elif options == "3":
     item = input("Which item (all units) would you like to remove? ")
     if item in cart:
         index = cart.index(item)
         cart.remove(item)
         prices.pop(index)
         print("Item removed.")

#Compute the total cost of the shopping cart:
    elif options == "4":
        total_price = sum(prices)
        compute = print(f"The total price of the items in the shopping cart is ${total_price}")

#Goodbye message:
    elif options == "5":
     print("Thank you. Goodbye.");
     break