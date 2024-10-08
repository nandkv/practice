# Lecture 1

## 1. Compound Types

### Summary
Compound types, also known as data structures, are collections of objects or values. They allow you to group multiple pieces of data together, making it easier to work with and manipulate data. Python provides several built-in compound types, including lists, tuples, strings, and dictionaries.

### Detailed Explanation

1. **Lists**: Lists are ordered collections of items, enclosed in square brackets `[]`. They are mutable, meaning you can modify, add, or remove elements after creating the list.

Example:
```python
fruits = ['apple', 'banana', 'cherry']
```

2. **Tuples**: Tuples are ordered collections of items, enclosed in parentheses `()`. They are immutable, meaning you cannot modify or change the elements once the tuple is created.

Example:
```python
point = (3, 4)
```

3. **Strings**: Strings are sequences of characters, enclosed in single quotes `''` or double quotes `""`. They are immutable, but you can create new strings by concatenating or slicing existing ones.

Example:
```python
greeting = "Hello, World!"
```

4. **Dictionaries**: Dictionaries are unordered collections of key-value pairs, enclosed in curly braces `{}`. The keys must be unique and immutable (e.g., strings, numbers, or tuples), and the values can be any data type.

Example:
```python
student = {'name': 'Alice', 'age': 20, 'courses': ['Math', 'Physics']}
```

### Common Operations

- `len(container)`: Returns the length or the number of items in the container.
- `+` and `*`: Concatenation and repetition operators for lists, tuples, and strings.
- Indexing and slicing: Accessing individual items or subsets of items in a container.
- Iterating over containers using loops.

### Multiple Choice Questions

1. Which of the following is an immutable data type in Python?
   a. List
   b. Tuple
   c. Dictionary
   d. Both b and c

2. What is the output of the following code?
   ```python
   fruits = ['apple', 'banana', 'cherry']
   print(fruits[1])
   ```
   a. 'apple'
   b. 'banana'
   c. 'cherry'
   d. IndexError

3. Which of the following is not a valid dictionary key in Python?
   a. 1
   b. 'name'
   c. (1, 2)
   d. [1, 2]

4. How can you get the length of a string `greeting = "Hello, World!"`?
   a. `len(greeting)`
   b. `length(greeting)`
   c. `greeting.length`
   d. `size(greeting)`

5. What is the output of the following code?
   ```python
   colors = ['red', 'green', 'blue']
   print(colors * 2)
   ```
   a. `['red', 'green', 'blue', 'red', 'green', 'blue']`
   b. `['red', 'green', 'blue']`
   c. `['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue']`
   d. Error

### Coding Exercises

1. Write a Python function that takes a list of numbers and returns a new list with only the even numbers.

2. Implement a function that takes a string and returns a dictionary with the count of each character in the string.

3. Given a list of tuples representing student names and grades, write a function that returns the average grade for the class.

4. Write a Python program that takes a sentence as input and returns a dictionary where the keys are the words, and the values are the number of times each word appears in the sentence.

5. Implement a function that takes two lists and returns a new list with the elements that are common to both lists.

6. Given a dictionary representing a person's information (name, age, city, etc.), write a function that returns a new dictionary with only the key-value pairs where the value is a string.

7. Write a Python program that takes a list of strings and returns a new list with only the strings that have a length greater than 5 characters.

8. Implement a function that takes a tuple of tuples representing coordinates (x, y) and returns the distance between the first and last coordinates.

9. Given a string representing a sentence, write a function that returns a new string with the words in reverse order.

10. Write a Python program that takes a dictionary of student names and their scores (subject-wise) and returns the name of the student with the highest overall score.

## 2. Choice and Conditionals

### Summary
Choice and conditionals are fundamental concepts in programming that allow you to execute different blocks of code based on certain conditions. In Python, conditional statements are implemented using the `if`, `elif` (else if), and `else` statements.

### Detailed Explanation

1. **`if` statement**: The `if` statement is used to execute a block of code if a certain condition is true.

Example:
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

2. **`elif` statement**: The `elif` (else if) statement is used to check additional conditions if the previous conditions were false.

Example:
```python
age = 18
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior citizen")
```

3. **`else` statement**: The `else` statement is used to execute a block of code when none of the previous conditions were true.

Example:
```python
grade = 75
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

4. **Conditional expressions**: Python also supports conditional expressions (also known as ternary operators) for simple if-else statements.

Example:
```python
age = 25
is_adult = "Yes" if age >= 18 else "No"
print(is_adult)  # Output: Yes
```

5. **Logical operators**: Conditions in conditional statements can be combined using logical operators such as `and`, `or`, and `not`.

Example:
```python
x = 10
y = 20
if x > 0 and y > 0:
    print("Both x and y are positive")
```

### Multiple Choice Questions

1. What is the output of the following code?
   ```python
   x = 10
   if x > 5:
       print("x is greater than 5")
   else:
       print("x is less than or equal to 5")
   ```
   a. `"x is greater than 5"`
   b. `"x is less than or equal to 5"`
   c. No output
   d. Error

2. Which of the following is a valid logical operator in Python?
   a. `&&`
   b. `||`
   c. `and`
   d. `or`

3. What is the output of the following code?
   ```python
   x = 10
   y = 5
   z = 15
   if x > y and x > z:
       print("x is the largest")
   elif y > x and y > z:
       print("y is the largest")
   else:
       print("z is the largest")
   ```
   a. `"x is the largest"`
   b. `"y is the largest"`
   c. `"z is the largest"`
   d. No output

4. Which of the following represents a valid conditional expression in Python?
   a. `result = x > y ? "Greater" : "Smaller"`
   b. `result = "Greater" if x > y else "Smaller"`
   c. `result = (x > y) ? "Greater" : "Smaller"`
   d. `result = (x > y) => "Greater" : "Smaller"`

5. What is the output of the following code?
   ```python
   x = 10
   y = 20
   if x > 0 or y < 0:
