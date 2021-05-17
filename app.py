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

# car_started = False
# while True:
#     prompt = input("> ").lower()
#     if prompt == 'start':
#         if car_started:
#             print("Car is already started!")
#         else:
#             car_started = True
#             print('Car started...Ready to go!')
#     elif prompt == 'stop':
#         if not car_started:
#             print('Car is already stopped')
#         else:
#             car_started = False
#             print('Car stopped.')
#     elif prompt == 'help':
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif prompt == 'quit':
#         break
#     else:
#         print('Sorry, I don\'t understand that')


# for item in range(5, 10, 2):
#     print(item)


# For Loops

# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# Nested Loops

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# Nested loops "x" challenge

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output = output + 'X'
#     print(output)

# for x in range(5):
#     print(x)


# More Lists

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[0])

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[4])

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[2:])

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[:4])

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[2:4])

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[4])

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names)

# numbers = [5, 2, 9, 2, 2]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# 2D Lists

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[0][1])

# returns 2


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix[0][1] = 20
# print(matrix[0][1])

# returns 20

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for item in row:
#         print(item)

# Returns 1-9 in a column


# List Functions/Methods

# numbers = [5, 2, 1, 7, 4]
# numbers.append(20)
# print(numbers)

# to end of list

# numbers = [5, 2, 1, 7, 4]
# numbers.insert(0, 10)
# print(numbers)

# insert 10 in place of index number 0

# numbers = [5, 2, 1, 7, 4]
# numbers.remove(5)
# print(numbers)

# removes 5 (all of them)

# numbers = [5, 2, 1, 7, 4]
# numbers.clear()
# print(numbers)

# clears out the list

# numbers = [5, 2, 1, 7, 4]
# numbers.pop() #remove last item from list
# print(numbers)

# numbers = [5, 2, 1, 7, 4]
# numbers.index(5) (if printed, this would return 0)
# print(numbers.index(5))

# returns 0, in the index number

# numbers = [5, 2, 1, 7, 4]
# print(50 in numbers)

# returns false

# numbers = [5, 2, 1, 7, 5, 4]
# print(numbers.count(5))

# retuns: 2

# numbers = [5, 2, 1, 7, 4]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# numbers = [5, 2, 1, 7, 4]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)

# numbers = [5, 2, 1, 7, 7, 4, 2, 5]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


# Tuples

# Immutable. They cannot be modified.

# numbers = (1, 2, 3, 4, 5)
# print(numbers[0])

# operators that work with tuples: these give information only
# .Count and .index

# Tuples - unpacking. Works with lists also.

# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates [2]
# x, y, z = coordinates

# dictionary


# name: john smith
# email: john@email.com
# phone: 234234

# dictionaries are used

# customer = {
#     "name": "john smith",
#     "age": 30
#     "is-verified": True
# }

# [customer["name"] = "Jack Smith"

# this would alter "name" in dictionary to "Jack Smith"

# customer[name]
# print([customer[name])

# #if we use wrong case for the "name" it will throw an error. However, if we use "get" it won't error, and instead will say "none."

# print(customer.get("birthdate"))

# result: none

# Project: Dictionary and Tuples

# number_words = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }

# phone_number = input('Phone: ')
# output = ""
# for digits in phone_number:
#     output += number_words.get(digits, "#") + " "
# print(output)

# message = input(">")
# words = message.split(' ')

# emojis = {

#     ":)": "😁",
#     ":(": "😩",
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


# functions

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('hi there')
#     print('welcome aboard')


# print('start')
# greet_user("John", "Smith")
# greet_user('Mary', 'Smith')
# print('Finish')

# "aruments, or parameters" -
# ordered arguments - we have to put 'Mary' first, and then 'Smith'. Have the be the same number of arguments as defined in the function.

# "Keyword arguments" greet_user(first_name="John"). You "call out" the arguments by using the key_words. You must call out all key words. If you do one, then all.

def square(number):
    return number * number


print(square(3))
