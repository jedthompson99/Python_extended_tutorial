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


good_credit = False
bad_credit = True
price = 1000000
down_payment_good = 1000000 * .1
down_payment_bad = 1000000 * .2

if good_credit:
    print('Your down payment is: ' + "$" + str(down_payment_good))
elif bad_credit:
    print('Your down payment is: ' + "$" + str(down_payment_bad))
else:
    print('Get lost!')
