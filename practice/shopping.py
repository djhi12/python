# Shopping Cart

# empty items and prices
items = []
prices = []

# Type item
new_item = input("What item would you like to add? ")

# Tye price
price = float(input(f"What is the price of {new_item}? "))

# Add item and price
items.append(new_item)
prices.append(price)

print(f"The price of this {items} is {prices}\n")
print(f"{items} has been added to the cart\n")