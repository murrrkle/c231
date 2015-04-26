print("Welcome to Change Calculator!\nI will help you calculate the change you owe to your customer!")

# Below: Amount customer owes to tender

before_tax = float(input("\nFirst, please enter the total original price of the item(s):\n$"))

after_tax = round((before_tax * 1.05) - 0.005, 2) # Subtracting 0.005 results in the customer saving a penny in the case that cent values less then one cause rounding up; emulates in-store policy

payment = float( input("\nNext, please enter the customer's payment:\n$"))

print("\nThe total price after applying tax is " + "$" + str(after_tax))

# Below: Change owed to customer

change_total = (payment - after_tax)

change_dollars = int(change_total)

TminusD = (change_total - change_dollars) # For the sake of the following lines looking nicer

change_quarters = int(TminusD / 0.25)

change_dimes = int(((TminusD - (change_quarters * 0.25)) / 0.1))

change_pennies = int(((TminusD - (change_quarters * 0.25) - (change_dimes * 0.1)) / 0.01))

print("You owe the customer " + str(change_dollars) + " dollar(s), " + str(change_quarters) + "quarter(s), " + str(change_dimes) + " dime(s) and " + str(change_pennies) + " pennies.") # Translates chain into exact coinage

