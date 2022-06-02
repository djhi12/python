# print(f"You guessed {number}")

# What is the magic number? 18
# What is your guess? 5
# Higher
# What is your guess? 6
# Higher
# What is your guess? 7
# Higher
# What is your guess? 20
# Lower
# What is your guess? 19
# Lower
# What is your guess? 18
# You guessed it!


import random

magic = random.randint(1, 100000000)
guess = None

while guess != magic:
    guess = input("What is your guess? ")
    guess = int(guess)

    if guess == magic:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")


#############################################################


# What is the magic number? 18
# What is your guess? 5
# Higher
# What is your guess? 6
# Higher
# What is your guess? 7
# Higher
# What is your guess? 20
# Lower
# What is your guess? 19
# Lower
# What is your guess? 18
# You guessed it!

number = 0
guess = "number"

number = int(input("What is the magic number? "))
number = int(input("What is your guess? "))

while number < 0:

    number = print("What is your guess? ")

if number < 20:
    int(input("Higher"))

while number < 0:

    print(f"Lower {number}")
