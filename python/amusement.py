
# The basic rules are as follows:

# No one under 36 inches may ever ride, either by themselves or with another rider.

# Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

# If there are two riders and one of them is at least 18 years old, they may ride together.

##################################################

# What is the age of the first rider? 12
# What is the height of the first rider? 46
# Is there a second rider (yes/no)? no
# Sorry, you may not ride.

# What is the age of the first rider? 82
# What is the height of the first rider? 75
# Is there a second rider (yes/no)? yes
# What is the age of the second rider? 14
# What is the height of the second rider? 35
# Sorry, you may not ride.


# What is the age of the first rider? 82
# What is the height of the first rider? 75
# Is there a second rider (yes/no)? yes
# What is the age of the second rider? 14
# What is the height of the second rider? 36
# Welcome to the ride. Please be safe and have fun!


age_first_rider = int(input('What is the age of the first rider?'))
height_first_rider = int(input('What is the height of the first rider?'))
# second_rider_question = input('Is there a second rider (yes/no)?')

# First Rider | Less than of age and height
if age_first_rider <= 18 and height_first_rider <= 46:

    second_rider_question = input('Is there a second rider (yes/no)?')
    # print('Welcome to the ride. Please be safe and have fun!')

    if second_rider_question == 'no':
        print('Sorry, you may not ride.')

    elif second_rider_question =='yes':
        age_second_rider = int(input('What is the age of the second rider?'))
        height_second_rider = int(input('What is the height of the second rider?'))

        if age_second_rider >= 18 and height_second_rider >= 36:
            print('Welcome to the ride. Please be safe and have fun!')

# Second rider | Greater than of age and height
elif age_first_rider >= 18 and height_first_rider >= 36:
    second_rider_question = input('Is there a second rider (yes/no)?')

    if second_rider_question == 'no':
        print('Welcome to the ride. Please be safe and have fun!')

    elif second_rider_question == 'yes':
        age_second_rider = int(input('What is the age of the second rider?'))
        height_second_rider = int(input('What is the height of the second rider?'))

        if age_second_rider >= 14 and height_second_rider >= 36:
            print('Welcome to the ride. Please be safe and have fun!')

        else:
            print('Sorry, you may not ride.')








# else:
#     second_rider_question = input('Is there a second rider (yes/no)?')

#     if second_rider_question == 'no':
#         print('Sorry, you may not ride.')

#     elif second_rider_question == 'yes':
#         age_second_rider = input('What is the age of the second rider?')
#         height_second_rider = input('What is the height of the second rider?')

#         if age_second_rider >= 18 and height_second_rider >= 36:
#             print('Welcome to the ride. Please be safe and have fun!')

#         else:
#             print('Sorry, you may not ride.')
