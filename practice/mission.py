# print("-----------------------------------------------------------")
# print("\nTHE STORY GAME! Base upon your choices make will decide, what will happen to your story!")
# print()
# print(f"You are turning 18 YEARS OLD (Men) and 19 YEARS OLD (Women) What you would like to choose over your age and you have 3 choices to made: SERVING MISSION or CAREER or LOVE LIFE? ")

# # Match
# choices = input('Enter choices: ')
# work_with_missionaries = input('Enter choices')

# if choices.lower() == "serving mission":
#     serving_mission = input("You choose serving mission: Oh that's great choices and also commandments. How would you prepare for your mission? WORK WITH MISSIONARIES or RELAX or PLAYING GAMES? ")

#     print()

# elif work_with_missionaries.lower() == "next year":
#         print("Your choose to work with Fulltime missionaries. That's goood decision and precisely the Lord Jesus Christ is Happy for you decision. When you will apply your mission? NEXT YEAR or MIDDLE OF THE YEAR or END OF THE YEAR?. ")
#         input()

# elif work_with_missionaries.lower() == "middle of the year":
#         print("that is 2023")

# elif work_with_missionaries.lower() == "end of the year":
#         print("Your wasting your time")
# else:
#     print("Please only on the choices given. Thanks!!!")
#     print()

#######################################################

# print("-----------------------------------------------------------")
# print("\nTHE STORY GAME! Base upon your choices make will decide, what will happen to your story!")

# print()

# # Scenario
# choice = input("You are turning 18 YEARS OLD (Men) and 19 YEARS OLD (Women) What you would like to choose over your age and you have 3 choices to made: SERVING MISSION or CAREER or LOVE LIFE? ").lower()

# # Scenario number 1: Serving Mission
# if choice == "serving mission":
#     preparation = input(
#         "You choose serving mission: Oh that's great choices and also commandments. How would you prepare for your mission? WORK WITH MISSIONARIES or RELAX or PLAYING GAMES? ").lower()

#     # Preparation number 1:
#     if preparation == "work with missionaries":
#         print("").lower()

#     # Preparation number 2:
#     elif preparation == "Relax":
#         print().lower()

#     # Preparation number 3:
#     elif preparation == "playing games":
#         print().lower()

#         # Space
#         print().lower()


# # Scenario number 2: Career
# elif choice == "career":
#     print("").lower()

#     input().lower()

# # Scenario number 3: Love life
# elif choice == "love life":
#     print().lower()


#######################################################

# if choices.lower() == "carrer":
#     carrer = input(f"You choose carrer: Oh that's good choices for your future. What would you like to be? ENGINEER, DOCTOR or PROGRAMMER? ")

# if carrer.lower() == "engineer":
#     print("Wow thats tough decission and better future. What field of Engineering you like? Civil, Mechanical or Electrical?. ")
#     input()
#     print("Awesome! You like to build a empire building.")


# if carrer.lower() == "engineer":
#         input()
# print("Great! You like to create a Robot.")


# if carrer.lower() == "engineer":
#     input()
#     print("Wonderful! Electerifying job.")

# elif carrer.lower() == "civil engineering":
#     print("Awesome! You like to build a empire building")
# elif carrer.lower() == "mechanical engineering":
#     print("Great! You like to create a Robot")
# elif carrer.lower() == "electrical engineering":
#     print("Wonderful! Electerifying job")

# print()

# # Scenario
# choice = input(f"If you are turning 18 YEARS OLD(Men) and 19 YEARS OLD (Women) What you would like to choose at your age? You have 3 choices: Serving mission?, Work?, or Education? ? ")

# # Scenario number 1: Serving Mission
# if choice == "serving mission":
#     preparation = input(
#         "You choose serving mission: Oh that's great! How would you prepare for your mission? Work with missionaries, Play games, or Relax? ").lower()

#     # Preparation number 1
#     if preparation == "work with missionaries":
#         time_serving = input(
#             "That's a good decision! When you will apply your mission? Middle of the year? End of the Year?, or Next Year? ").lower()

#         if time_serving == "middle":
#             print("")

#         elif time_serving == "end of the year":
#             print("")

#         elif time_serving == "next year":
#             print("")

#     # Preparation number 2:
#     elif preparation == ("relax"):
#         relaxation_type = input(
#             "Which one would you like to choose? Watching Nexflix, Listen music, ").lower()

#         if relaxation_type == "watching netflix":
#             print()

#     # Preparation number 3:
#     elif preparation == "playing games":
#         print()

#     # Space
#     print()


# # Scenario number 2: Work
# elif choice == "work":
#     print("")

#     input()

# # Scenario number 3: Education
# elif choice == "education":
#     print("")


# # Scenario 4:
# else:
#     print('Sleep')


print()

# Scenario
choice = input(f"If you are turning 18 YEARS OLD(Men) and 19 YEARS OLD (Women) What you would like to choose at your age? You have 3 choices: SERVING MISSION?, WORK?, or EDUCATION? ").lower()

input()

# Scenario number 1: Serving Mission
if choice == "serving mission":

    #
    preparation = input(
        "You choose serving mission: Oh that's great! How would you prepare for your mission? WORK WITH MISSIONARIES?, PLAY GAMES?, or RELAX?").lower()

    input()

    # Preparation number 1
    if preparation == "work with missionaries":

        #
        time_serving = input(
            "That's a good decision! When you will apply your mission? MIDDLE OF THE YEAR?, END OF THE YEAR?, or NEXT YEAR? ").lower()

        input()

        if time_serving == "middle of the year":
            print(
                "Awesome! Enough time to prepare for studying scriptures and all other stuff")

        elif time_serving == "end of the year":
            print("Great! You have still time to prepare ")

        elif time_serving == "next year":
            print("OH! That is next year.")

        else:
            print("You choose the wrong answer! ")

# Scenario number 2: Play Games
    elif preparation == "relax":

        #
        relaxation_type = input("You choose relax, But don't waste time!")

        if relaxation_type == "watching netflix":
            input(
                "You enjoy watching neflix. But to much watching netflix are not good. You will not learn for new skills for your future")

        elif relaxation_type == "":
            print("")

        elif relaxation_type == "":
            print()

        else:
            print("")

    # Preparation number 3:
    elif preparation == "play games":
        game_type = input("Oh! A quite fun but you also balance more important things.")

        if game_type == "":
            print("")

        elif game_type == "":
            print("")

        else:
            print()

    else:
        print("You choose the wrong answer!")

    # Space
    print()


# Scenario number 2: work
elif choice == "work":
    print("You choose WORK!. Probably you saving money and don't forget about your mission.")

    input()

# Scenario number 3: education
elif choice == "education":
    print("You choose EDUCATION! Learning is good and don't forget about your mission. ")

else:
    print("You choose the wrong answer!")
