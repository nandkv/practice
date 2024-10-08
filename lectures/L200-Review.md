Multiple Choice Questions:

1. What is the output of the following code?
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])
```
a) apple
b) banana
c) cherry
d) IndexError

2. In Python, which of the following is an immutable data type?
a) List
b) Tuple
c) Dictionary
d) Both b and c

3. What is the purpose of the `range()` function in Python?
a) To create a sequence of numbers
b) To iterate over a list
c) To create a new list
d) To sort a list

4. How do you add an element to the end of a list `my_list`?
a) `my_list.add(element)`
b) `my_list.append(element)`
c) `my_list.insert(element)`
d) `my_list[-1] = element`

5. Which of the following is not a valid dictionary key in Python?
a) 1
b) 'name'
c) (1, 2)
d) [1, 2]

6. What is the output of the following code?
```python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```
a) "x is greater than 5"
b) "x is less than or equal to 5"
c) No output
d) Error

7. Which of the following is a valid logical operator in Python?
a) `&&`
b) `||`
c) `and`
d) `or`

8. What is the output of the following code?
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")
greet(greeting="Hey", name="Charlie")
```
a) Hello, Alice!
   Hi, Bob!
   Hey, Charlie!
b) Alice, Hello!
   Bob, Hi!
   Charlie, Hey!
c) Hello, Alice!
   Bob, Hi!
   Hey, Charlie!
d) Error

9. What is the purpose of the `return` statement in a function?
a) To exit the function
b) To skip the current iteration
c) To return a value from the function
d) None of the above

10. What is the purpose of the `open()` function in Python?
a) To create a new file
b) To open an existing file
c) To write to a file
d) Both a and b

11. What mode should be used to open a file for appending content?
a) 'r'
b) 'w'
c) 'a'
d) 'x'

12. What is the output of the following code?
```python
for i in range(3):
    print(i)
```
a) 0 1 2
b) 1 2 3
c) 0 0 0
d) Error

13. What is the purpose of the `break` statement in a loop?
a) To skip the current iteration and move to the next one
b) To terminate the loop prematurely
c) To start a new loop
d) To define a loop

14. What is the output of the following code?
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[2:4])
```
a) [3, 4]
b) [2, 3]
c) [1, 2, 3, 4]
d) Error

15. What is the output of the following code?
```python
my_dict = {"apple": 2, "banana": 3, "cherry": 1}
print(my_dict["banana"])
```
a) 2
b) 3
c) 1
d) Error

Coding Problems:

1. Write a Python function to calculate the factorial of a given number.

2. Write a Python program to reverse a list without using the built-in `reverse()` function.

3. Write a Python function to find the greatest common divisor (GCD) of two numbers.

4. Write a Python program to remove duplicates from a list.

5. Write a Python function to reverse a string.

6. Write a Python program to count the frequency of each element in a list.

7. Write a Python program to merge two dictionaries.

8. Write a Python program to read the contents of a file and count the number of lines.

9. Write a Python program to find the sum of all numbers in a given list.

10. Write a Python program to find the second-largest number in a tuple.

Answers:

Multiple Choice Questions:
1. b
2. d
3. a
4. b
5. d
6. a
7. c
8. c
9. c
10. d
11. c
12. a
13. b
14. a
15. b

Coding Problems:

1. ```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

2. ```python
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list
```

3. ```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

4. ```python
def remove_duplicates(lst):
    return list(set(lst))
```

5. ```python
def reverse_string(s):
    return s[::-1]
```

6. ```python
def count_frequencies(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
```

7. ```python
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
```

8. ```python
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)
```

9. ```python
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
```

10. ```python
def second_largest(tup):
    sorted_tup = sorted(set(tup), reverse=True)
    if len(sorted_tup) > 1:
        return sorted_tup[1]
    else:
        return None
```
