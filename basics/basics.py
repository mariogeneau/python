# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# STANDALONE APP MAC

# from setuptools import setup
# 
# APP = ['MadNotes/MadNotes.py']
# DATA_FILES = []
# OPTIONS = {
#     'argv_emulation': False,
#     'packages': ['PIL']
#     }
# 
# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     setup_requires=['py2app'],
# )

# python3 setup.py py2app

# STANDALONE APP WINDOWS

# pyinstaller --onefile --windowed first_app.py

# import os
# os.getcwd()

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# VARIABLES

# my_int = 103204934813
# my_string = 'Hello, World!'
# my_flt = 45.06
# my_bool = 5 > 9
# my_list = ['item_1', 'item_2', 'item_3', 'item_4']
# my_tuple = ('one', 'two', 'three')
# my_dict = {'letter': 'g', 'number': 'seven', 'symbol': '&'}
# x = y = z = 0
# j, k, l = "shark", 2.05, 15
# 
# glb_var = "global"
# def var_function():
#     lcl_var = "local"
#     print(lcl_var)
# var_function()
# print(glb_var)
# 
# def new_shark():
#     global shark
#     shark = "Sammy"
# new_shark()
# print(shark)

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# CONDITIONAL STATEMENTS

# If it rains tomorrow, I will do the following:
#     - tidy up the cellar 
#     - paint the walls
#     - If there is some time left, I will 
#           - do my tax declaration
# Otherwise, I will do the following:
#     - go swimming
# go to the cinema with my wife in the evening

# if raining_tomorrow:
#     tidy_up_the_cellar() 
#     paint_the_walls()
#     if time_left: 
#         do_taxes()
# else:
#     enjoy_swimming()
# go_cinema()

# person = input("Nationality? ")
# if person == "french":
#     print("Préférez-vous parler français?")

# person = input("Nationality? ")
# if person == "french" or person == "French":
#     print("Préférez-vous parler français?")

# person = input("Nationality? ")
# if person == "french" or person == "French" :
#     print("Préférez-vous parler français?")
# if person == "italian" or person == "Italian" :
#     print("Preferisci parlare italiano?")

# person = input("Nationality? ")
# if person == "french" or person == "French" :
#     print("Préférez-vous parler français?")
# elif person == "italian" or person == "Italian":
#     print("Preferisci parlare italiano?")
# else:
#     print("You are neither Italian nor French,")
#     print("so we have to speak English with each other.")

# age = int(input("Age of the dog: "))
# if age < 1:
# 	print("This can hardly be true!")
# elif age == 1:
# 	print("about 14 human years")
# elif age == 2:
# 	print("about 22 human years")
# elif age > 2:
# 	human = 22 + (age - 2) * 5
# 	print("Human years: ", human)
# input('press Return>')

# The following objects are evaluated by Python as False:
# numerical zero values (0, 0.0, 0.0+0.0j),
# the Boolean value False,
# empty strings,
# empty lists and empty tuples,
# empty dictionaries.
# plus the special value None.

# max = a if (a > b) else b
# max = (a if (a > b) else b) * 2.45 - 4

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# LOOPS

# n = 100
# s = 0
# counter = 1
# while counter <= n:
#     s = s + counter
#     counter += 1
# print("Sum of 1 until %d: %d" % (n,s))

# import sys 
# 
# text = ""
# while 1:
#    c = sys.stdin.read(1)
#    text = text + c
#    if c == '\n':
#        break
# print("Input: %s" % text)

# import random
# 
# n = 20
# to_be_guessed = int(n * random.random()) + 1
# guess = 0
# while guess != to_be_guessed:
#     guess = int(input("New number: "))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print("Number too large")
#         elif guess < to_be_guessed:
#             print("Number too small")
#     else:
#         print("Sorry that you're giving up!")
#         break
# else:
#     print("Congratulation. You made it!")

# edibles = ["ham", "spam","eggs","nuts"]
# for food in edibles:
#     if food == "spam":
#         print("No more spam please!")
#         break
#     print("Great, delicious " + food)
# else:
#     print("I am so glad: No spam!")
# print("Finally, I finished stuffing myself")

# n = 100
# sum = 0
# for counter in range(1, n + 1):
#     sum = sum + counter
# print("Sum of 1 until %d: %d" % (n,sum))

# from math import sqrt
# n = int(input("Maximal Number? "))
# for a in range(1,n+1):
#     for b in range(a,n):
#         c_square = a**2 + b**2
#         c = int(sqrt(c_square))
#         if ((c_square - c**2) == 0):
#             print(a, b, c)

# fibonacci = [0,1,1,2,3,5,8,13,21]
# for i in range(len(fibonacci)):
#     print(i,fibonacci[i])
# print()

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ARRAYS

# a = [1, 3.5, "Hello"] # list

# import array as arr
# a = arr.array('d', [1.1, 3.5, 4.5])
# print(a)

# import array as arr
# a = arr.array('i', [2, 4, 6, 8])
# print("First element:", a[0])
# print("Second element:", a[1])
# print("Last element:", a[-1])

# import array as arr
# numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
# numbers_array = arr.array('i', numbers_list)
# print(numbers_array[2:5]) # 3rd to 5th
# print(numbers_array[:-5]) # beginning to 4th
# print(numbers_array[5:])  # 6th to end
# print(numbers_array[:])   # beginning to end

# import array as arr
# numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
# numbers[0] = 0    
# print(numbers)
# numbers[2:5] = arr.array('i', [4, 6, 8])   
# print(numbers)

# import array as arr
# numbers = arr.array('i', [1, 2, 3])
# numbers.append(4)
# print(numbers)
# numbers.extend([5, 6, 7]) 
# print(numbers)

# import array as arr
# odd = arr.array('i', [1, 3, 5])
# even = arr.array('i', [2, 4, 6])
# numbers = arr.array('i')
# numbers = odd + even
# print(numbers)  

# import array as arr
# number = arr.array('i', [1, 2, 3, 3, 4])
# del number[2]
# print(number)
# del number
# print(number)

# import array as arr
# numbers = arr.array('i', [10, 11, 12, 12, 13])
# numbers.remove(12)
# print(numbers)
# print(numbers.pop(2))
# print(numbers)

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# lists

# list1 = ['physics', 'chemistry', 1997, 2000];
# list2 = [1, 2, 3, 4, 5 ];
# list3 = ["a", "b", "c", "d"];

# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])

# list = ['physics', 'chemistry', 1997, 2000]
# print("Value available at index 2 : ", list[2])
# list[2] = 2001
# print("New value available at index 2 : ", list[2])

# list = ['physics', 'chemistry', 1997, 2000]
# print(list)
# del list[2]
# print("After deleting value at index 2 : ", list)

# len([1, 2, 3]) > 3 > Length
# [1, 2, 3] + [4, 5, 6] > [1, 2, 3, 4, 5, 6] > Concatenation
# ['Hi!'] * 4 > ['Hi!', 'Hi!', 'Hi!', 'Hi!'] > Repetition
# 3 in [1, 2, 3] > True > Membership
# for x in [1,2,3] : print (x,end = ' ') > 1 2 3 > Iteration

# L = ['C++'', 'Java', 'Python']
# L[2] > 'Python' > Offsets start at zero
# L[-2] > 'Java' > Negative: count from the right
# L[1:] > ['Java', 'Python'] > Slicing fetches sections

# my_list = [4, 5, 1, 6, 7]
# print(len(my_list))
# print(max(my_list))
# print(min(my_list))

# a_tuple = ("Hello", 12, True)
# a_list = list(a_tuple)
# print(a_list)

# class ClassName(object):
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg    
# obj1 = ClassName("Mario Geneau")
# obj2 = ClassName("Jen Danely")
# a_list = []
# a_list.append(obj1)
# a_list.append(obj1)
# a_list.append(obj2)
# print(a_list.count(obj1))

# list1 = ['physics', 'chemistry', 'maths']
# list2 = list(range(5))
# list1.extend(list2)
# print('Extended List :', list1)

# list1 = ['physics', 'chemistry', 'maths']
# list1.insert(1, 'Biology')
# print('Final list : ', list1)
        
# list1 = ['physics', 'Biology', 'chemistry', 'maths']
# list1.pop()
# print("list now : ", list1)
# list1.pop(1)
# print("list now : ", list1)

# list1 = ['physics', 'Biology', 'chemistry', 'maths']
# list1.remove('Biology')
# print("list now : ", list1)
# list1.remove('maths')
# print("list now : ", list1)

# list1 = ['physics', 'Biology', 'chemistry', 'maths']
# list1.reverse()
# print("list now : ", list1)

# list1 = ['physics', 'Biology', 'chemistry', 'maths']
# list1.sort()
# print("list now : ", list1)














