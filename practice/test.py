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


# import random

# magic = random.randint(1, 100000000)
# guess = None

# while guess != magic:
#     guess = input("What is your guess? ")
#     guess = int(guess)

#     if guess == magic:
#         print("congratulations! you won!")
#         break
#     else:
#         print("nope, sorry. try again!")


#############################################################

print("Welcome to the word guessing game!")
print("Your hint is: _ _ _ _ _ _")
word_guess = "mosiah"
guess = None
score = 0

while guess != "mosiah":
    guess = input("What is your guess? ")
    # guess = int(guess)
    score += 1

    if guess == "mosiah":
        print("MOSIAH congratulations! you won!")
        print(f"It took you {score} guesse(s)")
        break
    
    elif guess != "mosiah":
        print(f"You guessed {guess}. Try again!")
        print(f"It took you {score} guesse(s)")
        break

    else:
        print("nope, sorry. try again!")
        print(f"It took you {score} guesse(s)")
