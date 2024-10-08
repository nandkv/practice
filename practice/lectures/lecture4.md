# Topic 1: Problem Solving with Functions

## Summary
Functions are reusable pieces of code that perform a specific task. They help break down complex problems into smaller, manageable parts and promote code reusability and modularity.

## Detailed Explanation
**Defining Functions:**
Functions are defined using the `def` keyword, followed by the function name, parentheses for parameters, and a colon. The function body is indented and contains the statements to be executed when the function is called.

```python
def function_name(parameters):
    # Function body
    # Statement(s)
    return value
```

**Calling Functions:**
To use a function, you call or invoke it by its name, followed by parentheses with any required arguments.

```python
result = function_name(arguments)
```

**Parameters and Arguments:**
Functions can accept input data as parameters, which act as placeholders for the actual values (arguments) passed when the function is called.

**Return Statement:**
Functions can return a value using the `return` statement, which allows the function to produce an output that can be used in other parts of the program.

**Scope:**
Variables defined inside a function have a local scope and are only accessible within that function. Variables defined outside functions have a global scope and can be accessed anywhere in the program.

## Examples
1. **Defining and Calling a Function:**
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

2. **Function with Multiple Parameters:**
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: 8
```

3. **Function with Default Parameter Value:**
```python
def greet(name, message="Good morning"):
    print(f"{message}, {name}!")

greet("Bob")            # Output: Good morning, Bob!
greet("Charlie", "Hi")  # Output: Hi, Charlie!
```

## Practice Questions/Exercises
1. What is the output of the following code?
```python
def multiply(a, b):
    return a * b

result = multiply(4, 3)
print(result)
```
a) 7
b) 12
c) 16
d) Error

2. Write a function that takes a list of numbers and returns the sum of all even numbers in the list.

3. What is the purpose of the `return` statement in a function?
a) To exit the function
b) To output a value from the function
c) To define a function
d) Both a and b

4. What is the difference between parameters and arguments in Python functions?

5. Write a function that takes a string and returns the reverse of that string.

6. Multiple Choice: What is the output of the following code?
```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")
greet("Bob", "Hi")
```
a) Hello, Alice!
   Hi, Bob!
b) Hello, Alice!
   Hello, Bob!
c) Hi, Alice!
   Hi, Bob!
d) Error

7. Write a function that takes a list of strings and returns a new list with all the strings capitalized.

8. Multiple Choice: What is the scope of a variable defined inside a function?
a) Local
b) Global
c) Both local and global
d) None of the above

9. Write a function that takes two numbers and returns their greatest common divisor (GCD).

10. Multiple Choice: What is the output of the following code?
```python
def add(a, b):
    c = a + b
    return c

result = add(3, 4)
print(result)
```
a) 7
b) None
c) Error
d) No output

# Topic 2: Problem Solving with Loops

## Summary
Loops are a control flow structure that allows you to execute a block of code repeatedly, either a specific number of times or until a certain condition is met. They are essential for automating repetitive tasks and processing collections of data.

## Detailed Explanation
**For Loop:**
The `for` loop is used to iterate over a sequence (such as a list, string, or range) or any iterable object. It executes a block of code for each item in the sequence.

```python
for item in iterable:
    # Block of code
```

**While Loop:**
The `while` loop executes a block of code repeatedly as long as a given condition is true. It is useful when you don't know the exact number of iterations needed beforehand.

```python
while condition:
    # Block of code
```

**Loop Control Statements:**
- `break`: Terminates the loop prematurely and exits it.
- `continue`: Skips the current iteration and moves to the next one.

**Nested Loops:**
Loops can be nested inside other loops, allowing you to iterate over multidimensional data structures or perform complex operations.

**Loop Else Clause:**
The `else` clause in a loop is executed if the loop completes normally (without encountering a `break` statement).

## Examples
1. **For Loop with a List:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

2. **While Loop:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

3. **Nested Loops:**
```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

4. **Loop with Break and Continue:**
```python
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

5. **Loop with Else Clause:**
```python
num = 7
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
```

## Practice Questions/Exercises
1. What is the output of the following code?
```python
for i in range(3):
    print(i)
```
a) 0 1 2
b) 1 2 3
c) 0 0 0
d) Error

2. Write a program to find the sum of all numbers in a given list.

3. Multiple Choice: What is the purpose of the `break` statement in a loop?
a) To skip the current iteration and move to the next one
b) To terminate the loop prematurely
c) To start a new loop
d) To define a loop

4. Explain the difference between a `for` loop and a `while` loop in Python.

5. Write a program to find the factorial of a given number using a loop.

6. Multiple Choice: What is the output of the following code?
```python
count = 0
while True:
    print(count)
    count += 1
    if count > 5:
        break
```
a) 0 1 2 3 4 5
b) 0 1 2 3 4 5 6
c) Infinite loop
d) Error

7. Write a program to print the pattern of a pyramid using nested loops.

8. Multiple Choice: What is the purpose of the `else` clause in a loop?
a) To define an alternative condition for the loop
b) To execute code if the loop completes normally
c) To skip the current iteration and move to the next one
d) To terminate the loop prematurely

9. Write a program to check if a given string is a palindrome using a loop.

10. Multiple Choice: What is the output of the following code?
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```
a) 0 1 2 4
b) 0 1 2 3 4
c) 3
d) Error

# Topic 3: Data Structures - Lists, Tuples, and Dictionaries

## Summary
Python provides several built-in# Topic 3: Data Structures - Lists, Tuples, and Dictionaries

## Summary
Python provides several built-in data structures for storing and manipulating collections of data. The three main data structures are lists, tuples, and dictionaries, each with its own characteristics and use cases.

## Detailed Explanation

### Lists

Lists are ordered, mutable collections of items. They can store elements of different data types, including numbers, strings, and even other lists.

**Creating Lists:**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.14, [4, 5]]
```

**Accessing Elements:**
```python
print(fruits[0])    # Output: "apple"
print(numbers[-1])  # Output: 5 (negative indexing)
```

**Modifying Lists:**
```python
fruits[1] = "orange"  # Replacing an element
fruits.append("grape") # Adding an element
fruits.remove("apple") # Removing an element
```

**Common List Methods and Operations:**
- `len(list)`: Returns the length of the list
- `list.append(item)`: Adds an item to the end of the list
- `list.insert(index, item)`: Inserts an item at a specific index
- `list.remove(item)`: Removes the first occurrence of an item
- `list.sort()`: Sorts the list in ascending order
- `list + other_list`: Concatenates two lists
- `item in list`: Checks if an item is present in the list

### Tuples

Tuples are ordered, immutable collections of items. They are similar to lists but cannot be modified after creation.

**Creating Tuples:**
```python
point = (3, 4)
empty = ()
single = (1,)  # Note the trailing comma
mixed = (1, "two", 3.14)
```

**Accessing Elements:**
```python
print(point[0])    # Output: 3
print(mixed[-1])   # Output: 3.14
```

**Tuples are Immutable:**
```python
point[0] = 5  # Error: Tuples are immutable
```

**Common Tuple Operations:**
- `len(tuple)`: Returns the length of the tuple
- `item in tuple`: Checks if an item is present in the tuple
- `tuple + other_tuple`: Concatenates two tuples

### Dictionaries

Dictionaries are unordered collections of key-value pairs. They are mutable and allow for efficient data retrieval based on keys.

**Creating Dictionaries:**
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}
nested = {"data": [1, 2, 3], "info": {"name": "Bob", "age": 25}}
```

**Accessing Values:**
```python
print(person["name"])    # Output: "Alice"
print(nested["info"]["age"])  # Output: 25
```

**Modifying Dictionaries:**
```python
person["age"] = 31  # Updating a value
person["email"] = "alice@example.com"  # Adding a new key-value pair
del person["city"]  # Removing a key-value pair
```

**Common Dictionary Methods and Operations:**
- `len(dict)`: Returns the number of key-value pairs
- `dict.keys()`: Returns a view of the dictionary's keys
- `dict.values()`: Returns a view of the dictionary's values
- `dict.items()`: Returns a view of the dictionary's key-value pairs
- `key in dict`: Checks if a key is present in the dictionary

## Practice Questions/Exercises

### Lists

1. What is the output of the following code?
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[2:4])
```
a) [3, 4]
b) [2, 3]
c) [1, 2, 3, 4]
d) Error

2. Write a Python function to find the largest number in a list.

3. Multiple Choice: What is the output of the following code?
```python
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)
```
a) [1, 2, 10, 4, 5]
b) [1, 2, 3, 4, 5]
c) Error
d) None

4. Explain the difference between `list.append(item)` and `list.extend(iterable)` methods in Python.

5. Write a Python program to remove all occurrences of a specific element from a list.

### Tuples

6. What is the output of the following code?
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2:])
```
a) (3, 4, 5)
b) (1, 2, 3, 4, 5)
c) (2, 3, 4, 5)
d) Error

7. Write a Python function to find the second-largest number in a tuple.

8. Multiple Choice: What is the output of the following code?
```python
my_tuple = (1, 2, 3, 2, 1)
print(my_tuple.count(1))
```
a) 1
b) 2
c) 3
d) Error

9. Explain the purpose of the `tuple` data structure in Python and its advantages over lists.

10. Write a Python program to swap the first and last elements of a tuple.

### Dictionaries

11. What is the output of the following code?
```python
my_dict = {"apple": 2, "banana": 3, "cherry": 1}
print(my_dict["banana"])
```
a) 2
b) 3
c) 1
d) Error

12. Write a Python function to find the most common value in a dictionary.

13. Multiple Choice: What is the output of the following code?
```python
my_dict = {"name": "Alice", "age": 30}
my_dict["age"] = 31
print(my_dict)
```
a) {"name": "Alice", "age": 30}
b) {"name": "Alice", "age": 31}
c) Error
d) None

14. Explain the difference between `dict.keys()`, `dict.values()`, and `dict.items()` methods in Python.

15. Write a Python program to remove all key-value pairs from a dictionary where the value is greater than a given number.
