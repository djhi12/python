"""
Problem Statement:

You are tasked with creating a Python program to calculate the total cost of a meal, including tax and tip. Your program should prompt the user to input the cost of the meal and the percentage of tip they want to leave. The program should then validate the tip percentage to ensure it is greater than or equal to 0. If the tip percentage is valid, the program should calculate the total cost including an 8% tax rate and the specified tip percentage. Finally, the program should display the total cost of the meal.

Your task is to complete the Python program by implementing the calculate_total_cost() function. This function takes two parameters: meal_cost (the cost of the meal) and tip_percentage (the tip percentage to leave). It should return the total cost of the meal including tax and tip. If the tip percentage is less than 0, the function should print "Please enter a valid tip percentage." and return None.

"""


def calculate_total_cost(meal_cost, tip_percentage):
    """
    Calculate the total cost of the meal including tax and tip.

    Parameters:
    meal_cost (float): The cost of the meal.
    tip_percentage (float): The tip percentage to leave.

    Returns:
    float: The total cost of the meal including tax and tip.
    """
    # Check if the tip percentage is valid (greater than or equal to 0)
    if tip_percentage < 0:
        print("Please enter a valid tip percentage.")
        return None
    else:
        # Calculate the total cost including tax and tip
        tax_rate = 0.08  # 8% tax rate
        tax_amount = meal_cost * tax_rate
        tip_amount = meal_cost * (tip_percentage / 100)
        total_cost = meal_cost + tax_amount + tip_amount
        return total_cost


# Get user input for meal cost and tip percentage
meal_cost = float(input("Enter the cost of the meal: $"))
tip_percentage = float(
    input("Enter the tip percentage you want to leave (e.g., 15 for 15%): "))

# Calculate total cost using the function
total_cost = calculate_total_cost(meal_cost, tip_percentage)

# Print the total cost if it's not None
if total_cost is not None:
    print(
        f"The total cost of the meal, including tax and tip, is: ${total_cost:.2f}")
