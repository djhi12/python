# Your hint is: _ _ _ _ _ _
# What is your guess? temple
# Your hint is: _ _ m _ _ _
# What is your guess? moroni
# Your hint is: M O _ o _ i
# What is your guess? hhhhhh
# Your hint is: h h h h h H
# What is your guess? mosiah
# Congratulations! You guessed it!
# It took you 4 guesses.


import random
print(" 07 Prove. Assignement Milestone")
input()
# library that we use in order to choose
# on random words from a list of words

name = input("Your hint is: _ _ _ _ _ _ ")
# Here the user is asked to enter the name first

print("What is your guess? ")

words = ["Books", 'computer', 'laptop', 'programming',
         'abinadi', 'Moroni', 'temple', 'chapel',
         'lehi', 'nephi', 'helaman', 'prophets']

# Function will choose one random
# word from this list of words
word = random.choice(words)

guesses = ''

# any number of turns can be used here
turns = 12


while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            print(char, end=" ")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("guess a character:")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
