# What is the price of a child's meal? 4.50
# What is the price of an adult's meal? 9.00
# How many children are there? 4
# How many adults are there? 2
# What is the sales tax rate? 0.06

# Subtotal: $36.00
# Sales Tax: $2.16
# Total: $38.16

# variables for price, number of persons, and tax
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adult = int(input("How many adult are there? "))

# multiply the price of food and number of both children and adult 
child_meal_total = child_meal * number_of_children
adult_meal_total = adult_meal * number_of_adult

# add the total meal of both children and adult
subtotal = child_meal_total + adult_meal_total

print(f"Subtotal {subtotal}")
print()

# tax rate
tax_rate = float(input("What is the sales tax rate? "))
print()

sales_tax = tax_rate * subtotal

print(f"Sales Tax {sales_tax}")
print()

# Total of all calculations
total = subtotal + sales_tax

print(f"Total {total}")

# Payment
payment_amount = int(input("What is the payment amount? "))
change = payment_amount - total
print("Change: {:.3f}".format(change))
input()