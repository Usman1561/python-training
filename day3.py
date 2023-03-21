# Python Day 3 #

# -- File Handling -- # 
# f = open('test.txt', 'r')
# for each in f:
#     print(each)
    

# with open('test.txt') as f:
#     f.read()

# with open('test.txt', 'r') as f:
#     f.read()
#     data = f.readlines()
#     for l in data:
#         word = l.split()
#         print(word)

# -- Iterator -- # 0

# custom iterators 

# class PowTwo:
#     def __init__(self, max=0):
#         self.max = max
    
#     def __iter__(self):
#         self.n = 0
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
        
# num = PowTwo(2)

# i = iter(num)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# from itertools import count
# inf_iterator = count(1)
# print(inf_iterator)

# for i in range(5):
#     print(next(inf_iterator))

# def shout(text):
#     return text.upper()
 
# print(shout('Hello'))
 
# yell = shout
# print(yell('Hello'))

# def shout(text):
#     return text.upper()
# def whisper(text):
#     return text.lower()
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
 
# greet(shout)
# greet(whisper)

# -- decoraters --
# def hello_decorater(func):
    
#     def inner1():
#         print('this is inner 1')
#         func()
#         print('after function call')
#     return inner1

# @hello_decorater
# def func_to_be_used():
#     print('this is function inside')
    
# # func_to_be_used = hello_decorater(func_to_be_used)
# func_to_be_used()

# -- deep vs shallow copy --
# import copy
# l = [[1,2], [2,3]] 
# # cp = copy.deepcopy(l) # deep copy
# # cp[0][0] = 3
# # print(cp)
# # print(l)

# cp = copy.copy(l)
# cp[0][0] = 3
# print(cp)
# print(l)

# -- random numbers -- #
# import random
# num = random.random()
# print(num)

# num = random.randint(1,20) #int value
# print(num)

# num = random.randrange(1, 20, 2)
# print(num)

# num = random.uniform(50,70) #float value
# print(num)

# numlist = random.sample(range(150, 250), 15)
# print(numlist) # list with random no.s

# numlist = [1, 2, 4 ,7 ,9]
# random.shuffle(numlist)
# print(numlist)

# -- numpy -- #
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)


 