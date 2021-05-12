# print('I am Jed Thompson')
# print('o----')
# print(' ||||')
# print('*' * 10)

# price = 10
# price = 20
# print(price)

# name = 'John Smith'
# age = 20
# is_new = True
# name = input('what is your name? ')
# print("Hi " + name)

# name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print('Hi ' + name + ". " + "Your favorite color is " + color + ".")

# birth_year = input('Birth year: ')
# age = 2021 - int(birth_year)
# print(age)

# weight = input('What is your weight? ')
# kilo_weight = int(weight) * 0.453592
# print("Your Weight in Kilograms is: " + str(kilo_weight))

# course = 'Python\'s Course for "Beginners"'
# print(course[0])

# course = 'Python\'s Course for "Beginners"'
# print(course[0:3])
#
# course = 'Python\'s Course for "Beginners"'
# print(course[0:])

# course = 'Python\'s Course for "Beginners"'
# print(course[:5])

# course = 'Python\'s Course for "Beginners"'
# print(course[1:-1])

# first = "John"
# last = 'Smith'
# message = first + ' [' + last + '] is a coder.'
# msg = f'{first} [{last}] is a coder'
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find(0))
# print(course.replace('P', "J"))
# Boolean expression
#     print("Python" in course)


# good_credit = False
# bad_credit = True
# price = 1000000
# down_payment_good = price * .1
# down_payment_bad = price * .2

# if good_credit:
#     print('Your down payment is: ' + "$" + str(down_payment_good))
# elif bad_credit:
#     print('Your down payment is: ' + "$" + str(down_payment_bad))
# else:
#     print('Get lost!')

# has_high_income = True
# has_good_credit = False

# if has_high_income and has_good_credit:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible for Loan")

# has_criminal_record = True
# has_good_credit = True

# if has_good_credit and not has_criminal_record:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible for Loan")

# has_criminal_record = True
# has_good_credit = True

# if has_good_credit and not has_criminal_record:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible for Loan")


# temperature = 86
# if temperature >= 85:
#     print("it's a hot day")
# else:
#     print('it\'s not a hot day')

# username = input("Name: ")

# if len(username) <= 3:
#     print('name must be at least 4 characters')
# elif len(username) > 50:
#     print('name must be less than 50 characters')
# else:
#     print('looks good')

# weight = input('How much do you weigh? ')
# unit_of_weight = input('(L)bs or (K)g? ')

# if unit_of_weight.upper() == 'L':
#     result = float(weight) * .45
#     print(f'Your weight is {result} Kilos')

# elif unit_of_weight.upper() == "K":
#     result = float(weight) * 2.20462
#     print(f'Your weight is {result} Lbs')

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print('Done')

# SECRET NUMBER GAME

# magic_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == magic_number:
#         print('you win!')
#         break
#     elif guess_count == guess_limit and guess == magic_number:
#         print('you win!')
#         break
#     elif guess_count == guess_limit:
#         print('out of tries!')
#         break
#     else:
#         print('try again!')

# Car Game

prompt = input('>')
while prompt != "quit":
    if prompt == 'start'.upper:
        print('Car started...Ready to go!')
    elif prompt == 'stop'.upper:
        print('Car Stopped')
    else:
        print('I don't understand that...')
