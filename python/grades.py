grade_percentage = float(input('What is your grade percentage? '))

if grade_percentage >= 90:
    grade_letter = 'A'
    if grade_percentage % 10 < 3:
        final_letter = grade_letter + '-'
    elif grade_percentage % 10 >= 3:
        final_letter = grade_letter

elif grade_percentage >= 80:
    grade_letter = 'B'
    if grade_percentage % 10 < 3:
        final_letter = grade_letter + '-'
    elif grade_percentage % 10 >= 7:
        final_letter = grade_letter + '+'
    else:
        final_letter = grade_letter

elif grade_percentage >= 70:
    grade_letter = 'C'
    if grade_percentage % 10 < 3:
        final_letter = grade_letter + '-'
    elif grade_percentage % 10 >= 7:
        final_letter = grade_letter + '+'
    else:
        final_letter = grade_letter

elif grade_percentage >= 60:
    grade_letter = 'D'
    if grade_percentage % 10 < 3:
        final_letter = grade_letter + '-'
    elif grade_percentage % 10 >= 7:
        final_letter = grade_letter + '+'
    else:
        final_letter = grade_letter

elif grade_percentage < 60:
    grade_letter = 'F'
    final_letter = grade_letter
print(f'Your grade letter is {final_letter}')
#print(f'Your grade letter is {grade_letter}')
# if (grade_percentage % 10) < 3:
#      print(f'Your grade letter is {grade_letter}-')
# elif (grade_percentage % 10) >= 7:
#     print(f'Your grade letter is {grade_letter}+')
# else:
#     print(f'Your grade letter is {grade_letter}')
if grade_percentage >= 70:
    print('Congratuation! You have passed.')
else:
    print("Sorry. You din't pass. Please study more and tray to pass later. In order to pass you need to have grade precentage of 70 credits or more." )


    