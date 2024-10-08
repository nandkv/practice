
# my_list[start_index:end_index]

# text = "nandrahulbeena"
# print(text[0:4])
# print(text[4:9])
# print(text[9:])

# my_list = ['apple', 'banana', 'cherry', 'date']
# print(my_list[1:3])
# print(my_list[:2])
# print(my_list[2:])

# my_list[start_index:end_index:step_size]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_numbers = numbers[::2]
# even_numbers = numbers[1::2]
# print(odd_numbers)
# print(even_numbers)

# text = "hello"
# text[0] = "J"

# a = 3
# a = 4
# print(a)

# student = {
#     'name': 'Alice', 
#     'age': 20, 
#     'courses': ['Math', 'Physics'], 
#     1: 'one',
#     2.5: 'float',
#     (1, 2): 'tuple'
# }
# Dictionary: Key of an element in the dictionary (key,value) should be immmutable
# string => immutable => hashable
# numbers => immutable => hashable
# tuple => immutable => hashable
# list => mutable => unhashable

# print(student['name'])



# for i in range(3):
#     # print(i)
# dic = {0:1 ,1:2 ,2:0 ,3:1}

# i   dic[i]  dic[dic[i]] dic[dic[i] +1]

# 0   1       2           0
# 1   2       0           1
# 2   0       1           1

 
# for i in range(10):
#     print(i)



# x = [1,2,3]
# y = [2]
# for i in x:
#     y[i] = [y[0]*x[i-1]]
# print(y)

inventory = {'dog toy': 3,'cat toy': 0, 'remote car':4} 

# print(inventory.keys())

# for _ in range(3):
#     print(_);

# inventory = {'dog toy': 3,'cat toy': 0, 'remote car':4, 'toy robot': 1} 

# inventory = {'dog toy': 3,'cat toy': 0, 'remote car':3, 'toy robot': 1} 

# for k in inventory.keys():
#     print(k)

# dog toy, 3
# cat toy, 0 
# remote car, 3
# toy robot, 1

# inventory = {'dog toy': 3,'cat toy': 0, 'remote car':4} 
# def u(inventory , item):
#     if item in inventory.keys():
#         inventory[item] += 1 
#     else:
#         inventory[item] = 1

# def c(inventory , item):
#     return inventory[item] if item in inventory.keys() else False

# def r(inventory , item):
#     result = False
#     if item in inventory.keys():
#         inventory[item] -= 1
#         result = 1 
#     return result

# for _ in range(3):
#     u(inventory , "toy robot") 
#     r(inventory , "remote car")
    
# for k in inventory.keys(): 
#     print(k, c(inventory ,k))

#dict = {k, v}
# grade = {'rahul': 3,'nand': 0, 'beena':4} 

# print(grade.keys())
# print(grade["rahul"])

# def f(lst):
#     if len(lst) > 1:
#         tmp = []
#         for i in range(len(lst)-1):
#             if lst[i] >= lst[i+1]: 
#                 tmp += [1]
#             else:
#                 tmp += [0]
#             return tmp 
#         else:
#             return False

# data = [[3 ,2 ,4 ,1 ,2] ,[1 ,2] ,[1]]
# for d in data:
#     #print(f(d))
#     print(d)
#     #print(data[0] >= data[1])

# data = ['rahul', 'nand', 'beena']
# for d in data:
#     print(d)

# for i in range(10):
#     print(i)

# import math


# def add(x):
#     return math.sqrt(x+1)

# # def addNumbers(x,y):
# #     return x+y;

# x = -5 
# print(add(x))

numbers = [1, 2, 3, 4]

# pseudo code

# input -> numbers
# output -> [4, 3, 2, 1]
# code -> reversed


# index = len(numbers) - 1

# while index >= 0:
#     print(numbers[index])
#     index -= 1

# i = len(numbers)
# while i > 0:
#     print(numbers[i-1])
#     i-=1

# for i in range(len(numbers)-1, -1, -1):
#     print(numbers[i])

# numbers = [1, 2, 3, 4]
# reversed_numbers = []

# for i in numbers[::-1]:
#     reversed_numbers.append(i)

# print(reversed_numbers)

# inventory = {'dog toy': 3,'cat toy': 0, 'remote car':4} 
# def u(inventory , item):
#     if item in inventory.keys():
#         inventory[item] += 1 
#     else:
#         inventory[item] = 1

# def c(inventory , item):
#     return inventory[item] if item in inventory.keys() else False

# def r(inventory , item):
#     result = False
#     if item in inventory.keys():
#         inventory[item] -= 1
#         result = 1 
#     return result

# for _ in range(3):
#     u(inventory , "toy robot") 
#     r(inventory , "remote car")

# for k in inventory.keys(): 
#     print(k, c(inventory ,k))