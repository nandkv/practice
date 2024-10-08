Multiple Choice Questions:

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

6. What is the output of the following code?
   ```python
   x = 10
   y = 20
   if x > 0 or y < 0:
       print("At least one condition is true")
   else:
       print("Both conditions are false")
   ```
   a. "At least one condition is true"
   b. "Both conditions are false"
   c. No output
   d. Error

7. What is the purpose of the `break` statement in a loop?
   a. To terminate the loop immediately
   b. To skip the current iteration and move to the next one
   c. To start a new loop
   d. None of the above

8. What is the output of the following code?
   ```python
   def greet(name, greeting="Hello"):
       print(f"{greeting}, {name}!")

   greet("Alice")
   greet("Bob", "Hi")
   greet(greeting="Hey", name="Charlie")
   ```
   a. Hello, Alice!
      Hi, Bob!
      Hey, Charlie!
   b. Alice, Hello!
      Bob, Hi!
      Charlie, Hey!
   c. Hello, Alice!
      Bob, Hi!
      Hey, Charlie!
   d. Error

9. What mode should be used to open a file for appending content?
   a. 'r'
   b. 'w'
   c. 'a'
   d. 'x'

10. Which loop is typically used to iterate over a collection of objects in Python?
    a. `for` loop
    b. `while` loop
    c. `do-while` loop
    d. `repeat` loop

11. What is the purpose of the `return` statement in a function?
    a. To exit the function
    b. To skip the current iteration
    c. To return a value from the function
    d. None of the above

12. Which of the following is true about nested loops?
    a. The inner loop executes completely for each iteration of the outer loop
    b. The outer loop executes completely for each iteration of the inner loop
    c. Both the inner and outer loops execute completely for each iteration
    d. None of the above

13. What is the output of the following code?
    ```python
    my_list = [1, 2, 3, 4, 5]
    my_list[2] = 10
    print(my_list)
    ```
    a. [1, 2, 10, 4, 5]
    b. [1, 2, 3, 4, 5]
    c. Error
    d. None

14. What is the output of the following code?
    ```python
    my_tuple = (1, 2, 3, 2, 1)
    print(my_tuple.count(1))
    ```
    a. 1
    b. 2
    c. 3
    d. Error

15. What is the output of the following code?
    ```python
    my_dict = {"name": "Alice", "age": 30}
    my_dict["age"] = 31
    print(my_dict)
    ```
    a. {"name": "Alice", "age": 30}
    b. {"name": "Alice", "age": 31}
    c. Error
    d. None

Coding Problems:

1. Write a Python function that takes a list of numbers and returns a new list with only the even numbers.

2. Implement a function that takes a string and returns a dictionary with the count of each character in the string.

3. Given a list of tuples representing student names and grades, write a function that returns the average grade for the class.

4. Write a Python program that takes a sentence as input and returns a dictionary where the keys are the words, and the values are the number of times each word appears in the sentence.

5. Write a function that takes two numbers and returns their greatest common divisor (GCD).

6. Write a Python program to read the contents of a file and count the number of lines.

7. Write a program to find the sum of all numbers in a given list.

8. Write a Python function to find the largest number in a list.

9. Write a Python function to reverse a string.

10. Write a Python program to remove all occurrences of a specific element from a list.

Answers:

Multiple Choice Questions:

1. d
2. b
3. d
4. a
5. a
6. a
7. a
8. c
9. c
10. a
11. c
12. a
13. a
14. b
15. b

Coding Problems:

1. ```python
   def get_even_numbers(numbers):
       return [num for num in numbers if num % 2 == 0]
   ```

2. ```python
   def count_characters(string):
       char_count = {}
       for char in string:
           char_count[char] = char_count.get(char, 0) + 1
       return char_count
   ```

3. ```python
   def calculate_average_grade(students):
       total_grades = 0
       num_students = 0
       for name, grade in students:
           total_grades += grade
           num_students += 1
       return total_grades / num_students
   ```

4. ```python
   def count_word_frequency(sentence):
       word_count = {}
       words = sentence.split()
       for word in words:
           word_count[word] = word_count.get(word, 0) + 1
       return word_count
   ```

5. ```python
   def gcd(a, b):
       while b != 0:
           a, b = b, a % b
       return a
   ```

6. ```python
   def count_lines(file_path):
       with open(file_path, 'r') as file:
           lines = file.readlines()
           return len(lines)
   ```

7. ```python
   def sum_of_list(numbers):
       total = 0
       for num in numbers:
           total += num
       return total
   ```

8. ```python
   def find_largest(numbers):
       largest = numbers[0]
       for num in numbers:
           if num > largest:
               largest = num
       return largest
   ```

9. ```python
   def reverse_string(string):
       return string[::-1]
   ```

10. ```python
    def remove_element(lst, element):
        return [item for item in lst if item != element]
    ```
