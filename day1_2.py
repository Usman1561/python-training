# --  Basics -- 

# name = 'usman'
# age = 23
# birthdate = '3rd March - 2000'
# company_name = input('where exaclty are you going to work? ')
# print('Company: ' + company_name)


# -- type conversion --
# birth_year = input("Enter your birth year: ")
# age = 2023- int(birth_year)
# print(age)


# -- sum calculator program --
# first = float(input("please enter your first no:"))
# second = float(input("please enter your second number:"))
# sum = first + second
# print("Sum:" + str(sum))

# -- object in python --
# -- methods/functions to objects -- 
# subject = 'object Oriented Programming'
# print(subject.capitalize) #returns a new string
# print(subject)
# subject.find('O') #if no values finds, returns -1 as false
# subject.lower
# subject.upper
# print(subject.replace('Oriented', 'oriented'))
# print('Programming' in subject)

# -- Arithmetic Operators --
# print(10 // 3 ) #returns value in float point
# print(10 / 3)
# print(10 % 3) #returns value of reminder
# print(10 ** 3) #return val of int to the power raised
# x = 10
# x = 10 + 3 
# x += 3 #augmented assignment operator 
# # use parenthesis to evade math rule 
# x = 10 + 3 * 2 
# x = (10 + 3 ) * 2

# -- Types Comparison Operator -- 
# >, >=, <, <=, ==, !=

# -- logical operators -- 
# age = 23
# print(age > 20 and age < 30) # check for all
# print(age > 20 or age < 30) # check for any true
# print(not age < 20) # check for false

# -- if statement --
# age = 32 
# if age > 30:
#     print("Not Recommended")
# elif age > 20 or age < 30:
#     print("Recommended")
# print("this code is not a part of if block")

# weight problem exercise 
# weight = float(input('Weight: '))
# weight_type = input("(K)gs or (L)bs: ")
# if weight_type == 'L' or weight_type == 'l':
#     result_kg = weight * 0.45359237
#     print(result_kg)
# elif weight_type == 'K' or weight_type == 'k':
#     result_lb = weight * 2.20462
#     print (result_lb)
    
# -- loops --
# i = 10
# while i >= 5:
#       print(i * '*')
#       i = i - 1 

# num = [1, 3, 4, 5, 7, 9, 10]
# for items in num:
#     print(items)

# i = 0
# while i < len(num):
#     print(num[i])
#     i = i + 1

# l = ['geeks', 'for', 'geeks'] # in array
# for i in l:
#     print(i)
    
# t = ('geeks', 'for', 'geeks') # in tuple
# for i in t:
#     print(i)

# name = 'usman' # in string
# for i in name:
#     print(i)
    
# d = dict() # in dictionary
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#     print("%s %d" % (i, d[i]))

# vowel = ('a', 'i', 'e', 'o', 'u')
# for v in vowel:
#     print(v)

# arr = [1, 2, 3, 4] #iterate using index & range 
# for i in range(len(arr)):
#     print(arr[i])

# name = 'arima kousei' # use of continue statement
# for i in name:
#     if i == 'a' or i == 'i':
#         continue
#     print(i)

# for i in 'usman': # break statement in for loop
#     if i == 'm':
#         break
#     print(i)

# pass statement in python
# for i in 'python':
#     pass 
# print(i)

# wordlist = ['islam', 'my', 'heart']
# letterlist = []
# for i in wordlist:
#     for j in i: 
#         letterlist.append(j)
#         print(j)

# list - comprehension
# sq_nums = [ i*i for i in range(1,5) if i%2 != 0]
# print(sq_nums)

# -- Complex Types: List --
# names = ["Usman", "Maazo", "Irfan"]
# print(names)
# print(names[1])
# print(names[-1])
# names[2] = "Hassan"
# print(names[1:3])

# -- list methods --
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)
# numbers.insert(0, 0) 
# print(numbers)
# print(1 in numbers)
# print (len(numbers))

# -- Range Function -- 
# num = range(5, 10, 2)
# for i in num :
#     print(i)
# for i in range(5):
#     print(i)
    
# -- tuples --
# numbers = (1, 2, 3, 3)
# # numbers[0] = 0  wont work as tuples are immutable 
# print(numbers.count(3))
# print(numbers.index(2))

# --- Exception Handling --- 
# try: 
#     print(x)
# except: 
#     print('x is not defined')
    
# try:
#     print(y)
# except NameError:
#     print('y is not defined')
# except:
#     print('Something else went wrong')

# try: 
#     print(x)
# except: 
#     print('Something went wrong')
# finally: 
#     print(' exception handling managed ')

# raise keyword 
# x = -1
# if x < 0:
#     raise Exception("sorry, no numbers below zero")

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# function 
# def greet():
#     name = 'usman'
#     print(name) 
# greet()

# def sum_func(n1, n2):
#     sum = n1 + n2
#     print(sum)
# sum_func(1, 2)

# --- partial functions ---
# from functools import partial
# def add(a, b):
#     return a * 100 + b + 10
# add_part = partial(add, b = 3)
# print(add_part(1))


# -- anynomous/ lambda function
# x = lambda n:n*2
# print(x(5))

# larger = lambda a,b:a if a>b else b
# print(larger(2,3))

# names = ['usman', 'arman', 'bilal', 'sheroz']
# names.sort()
# print(names)

# names = ['m usman', 'arman', 'bilal ch', 'sheroz']
# names.sort(key = lambda x:len(x))
# print(names)

# recursive function 
# def factorial(x):
#     if x == 1:
#         return 1
#     else: 
#         return (x * factorial(x-1))
# num = 3
# print (factorial(num))

# Monkey patch
# monk.py ( if in module )
# class A:
#     def func(self):
#         print('func() is called')

# # import monk ( if in module )
# def monkey_f(self):
#     print('money_f() is being called')

# A.func = monkey_f # monk.A.func (if in module)
# obj = A()

# obj.func()

# Collections ( Arrays )
# slicing of list
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# sliced_list = list[1:5]
# print(sliced_list)

# list comprehension 
# odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
# print(odd_square)

# set 
# vowel = {'a', 'i', 'e', 'o', 'u'}
# vowel.add('u')
# print(vowel)
# a = {'a', 'i', 'e', 'o'}
# b = {'u'}
# union in set
# vowel = a.union(b)
# vowel = a|b # or using | operator 
# print(vowel)

# dictionary 
# Dict = dict([('first_name', 'Muhammad'), ('last_name', 'Usman')])
# print(Dict)
# Dict = {}
# Dict['nested'] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
# print(Dict)

# strings 
# name = 'arimakousei'
# name = ''.join(reversed(name))
# print(name)

# escape sequence 
# path = "C:\\Internship\\Python_training"
# print(path)

# formatting
# positional 
# format_name = "{1} {0}".format('muhammad', 'usman')
# print(format_name)

# string1 = "{0:.2f}".format(2/7) # rounding off ints
# print(string1)

# ---- OOP ---- #
# class Employee: 
#     empCount = 0
    
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
    
#     def displayCount(self):
#         print("Total Employees are %d" % Employee.empCount)
        
#     def displayEmployee(self):
#         print("Name: ", self.name, ", Salary: ", self.salary)
    
# emp = Employee('Usman', 90000)
# emp.displayEmployee()
# emp.displayCount()

# -- class methods -- 

# class Employee:
#     company = 'devsinc'
    
#     def show(self):
#         print(self.name)
#         print(self.company)
    
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
        
# e1 = Employee()
# e1.name = 'Harry'
# e1.show()
# e1.changeCompany('Contour')
# e1.show()

# -- Inheritance -- #
# Single level
# class Parent:
#     i = 5
#     def parent_method(self):
#         print('I am the parent class method')

# class SubClass(Parent):
#     i = 10 
#     def child_method(self):
#         print('I m the sub class method')
        
# sub = SubClass()
# sub.parent_method()
# sub.child_method()

# Multiple Inheritance
# class Parent1:
#     i = 5
#     def parent1_method(self):
#         print('I am the parent1 class method')
        
# class Parent2:
#     i = 7
#     def parent2_method(self):
#         print('I am the parent2 class method')

# class SubClass(Parent1, Parent2):
#     i = 10 
#     def child_method(self):
#         print('I m the sub class method')
        
# sub = SubClass()
# sub.parent1_method()
# sub.parent2_method()
# sub.child_method()

# class/static variable
# class MyClass:
#     name = 'usman'
    
#     def __init__(self):
#         print('this is constructor')
        
#     def method(self):
#         language = 'python'

# obj = MyClass()
# print(obj.name)


