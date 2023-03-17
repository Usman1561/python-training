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