# import random
# print("Welcome to the word guessing game!")

# # Step -1: List of words that can be accepted
# # RANDOM = Generate random numbers

# words = ['mosiah', 'moroni', 'nephi']

# # CHOICE = returns a randomly selected element from the specified sequence.
# word = random.choice(words)
# # print(word)

# # Step -2: Adding blank spaces
# # LEN = returns the number of items in an object.
# spaces = ['_']*len(word)

# # DEF = is the keyword for defining a function.


# def get_letter_position(guess, word, spaces):

#     # Create and set a variable called index to be -2
#     index = -2

#     # Create a loop to continue to look through the word for every single position where that letter exist
#     # WHILE LOOP = A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.
#     while index != -1:

#         # Check if the character/guess is in word, it then removes the character from the word and add it to spaces
#         # IF =
#         # IN = The in keyword has two purposes: The in keyword is used to check if a value is present in a sequence (list, range, string etc.).
#         if guess in word:

#             # FIND() = method finds the first occurrence of the specified value.
#             index = word.find(guess)

#             # remove that letter from the word
#             # this is the special character that will let us know that the character is removed from the word
#             # COLON = A colon is used to represent an indented block. Another major use of the colon is slicing. In slicing, the programmer specifies the starting index and the ending index and separates them using a colon which is the general syntax of slicing.
#             removed_character = '*'
#             word = word[:index] + removed_character + word[index + 1:]
#             spaces[index] = guess

#         else:
#             index = -1

#             return(word, spaces)


# # Step -3: Validating user input
# def win_check():

#     # RANGE() = The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#     for i in range(0, len(spaces)):
#         if spaces[i] == '_':
#             return -1
#         return 1


# # Choose some number of turns for the user to guess the word
# num_turns = len(word)
# for i in range(0, num_turns):

#     # ask the user to guess a character
#     guess = input('Your hint is: ')

#     if guess in word:
#         word, spaces = get_letter_position(guess, word, spaces)
#         print(spaces)

#     else:
#         print('Your guess was not correct!')


#     #check if the player guess the word
#     if win_check() == 1:
#         print('Congratulations you won')
#         break

#     print('you have'+str(num_turns - i)+' turns left.')
#     print()


# from posixpath import split
# from re import S


print("Welcome to the word guessing game!")

secret_word = "mosiah"
# print(len(secret_word))  # 6
# print(secret_word)  # ['m', 'o', 's', 'i', 'a', 'h']
# print(secret_word.index("m"))

guess = input("What is your guess?")

if guess == secret_word:
    print("Greay Job!")

elif guess.index("m") or guess.index("M"):
    print("Awesome!")

else:
    ("You failed")


# guess = input("What is your guess?")

# # guess_letter = guess.split()

# if guess == secret_word:
#     print("You did it!")

# else:
#     print("You failed!")




# guess_number = ""

# hint = print('Your hint is: _ _ _ _ _ _')

# while guess_array != secret_word:
#     guess = input('What is your guess? ')

# guess_array = guess.split()


# if guess_array == secret_word:
#     print("you did it!")


# guess = input('What is your guess? ')


##################################################

# import random

# magic_number = random.randint(1, 100)

# guess = -1

# while guess != magic_number:
#     guess = int(input("What is your guess?"))

#     if guess < magic_number:
#         print("higher")
#     elif guess > magic_number:
#         print("Lower")
#     else:
#         print("You guess it!")


#########################################################
