# simple types - integer, float, Boolean

# compound types -> use simple types
# list, tuple, string -> sequence
# dictionary -> set

# accessing a sequence element -> subscripting or loop

word_list = ['cat', 'dog', 'rabbit']

# #subscripting read using index
print(word_list[0])
print(word_list[1])
print(word_list[2])

# #subscripting update value using index
word_list[0] = 'i'
word_list[1] = 'am'
word_list[2] = 'here'

# #iterative function
for word in word_list:
    print(word)

word_list.append('nand')
print(word_list[3])

double_list = [[1,2], [3,4], [5,6]]                 
for outer_element in double_list:                   #[1,2]
    for inner_element in outer_element:                 #1
        print(inner_element)

# start_index, end_index, step_index
for i in range(3):
    print(i)


word_list = ['cat', 'dog', 'rabbit']
for index in range(len(word_list)):
    print(word_list[index])

for i in range(3, 6, 2):
    print(i)

point = (2, 3)
for value in point:
    print(value)


string = 'hello'
for char in string:
    print(char)

name = 'rahulvenigalla'
print(name[1:6:2])
      

for i in range(3,2,-1):
    print(i)

index = 0
while index < 3:
    print(index)
    index += 2

for i in range(0, 3, 2):
    print(i)


index = 3
while index < 2:
    print(index)
    index += 1

index = 3
while index < 2:
    print(index)
    index -= 1