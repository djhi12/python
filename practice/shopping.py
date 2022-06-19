print(" Welcome to the Shopping Cart Program! \n")
action = int(input("Please select one of the following: \n\n 1. Add Item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit \n \nPlease enter an action: "))
# print(f"{menu} \n")
action_list = [0, 1, 2, 3, 4, 5]
list_items = []
# print(len(action_list))

while action != len(action_list):

    if action == action_list[1]:
        add_item = input("What item would you like to add? ")
        list_items.append(add_item)
        print(f"{add_item} has been added to the cart.")
        break

    elif action == action_list[2]:
        print(list_items)
        break

    elif action == action_list[3]:
        break

    else:
        print("Incorrect input. Try again")
