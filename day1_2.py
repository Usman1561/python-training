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

weight = float(input('Weight: '))
weight_type = input("(K)gs or (L)bs: ")
if weight_type == 'L' or weight_type == 'l':
    result_kg = weight * 0.45359237
    print(result_kg)
elif weight_type == 'K' or weight_type == 'k':
    result_lb = weight * 2.20462
    print (result_lb)
 


    