# I added an if/else statement to the change variable print to avoid calculation errors or negative results
# Also added an string to the subtotal and total prints to make it clear to the user.

child_meal = float(input("Please, enter the price of a child's meal: "))
adult_meal = float(input("Please, enter the price of an adult's meal: "))
children_number = int(input("How many children are there? "))
adults_number = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

meal_subtotal = (child_meal * children_number) + (adult_meal * adults_number)
print(f"Subtotal: ${meal_subtotal}")

sales_tax = meal_subtotal * (tax_rate / 100)
total_price = meal_subtotal + sales_tax
print(f"Total (with taxes): ${total_price}")

payment_amount = float(input("What is the payment amount? $"))
change = payment_amount - total_price

if change >= 0:
  print(f"Your change is: ${float(change)}")
else:
  print(f"Please, pay at least: ${total_price:}")