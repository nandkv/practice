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

6. What is the purpose of the `return` statement in a function?
   a. To exit the function
   b. To output a value from the function
   c. To define a function
   d. Both a and b

7. What is the output of the following code?
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

8. What is the purpose of the `break` statement in a loop?
   a. To terminate the loop immediately
   b. To skip the current iteration and move to the next one
   c. To start a new loop
   d. None of the above

9. What is the output of the following code?
   ```python
   count = 0
   while True:
       print(count)
       count += 1
       if count > 5:
           break
   ```
   a. 0 1 2 3 4 5
   b. 0 1 2 3 4 5 6
   c. Infinite loop
   d. Error

10. What is the purpose of the `else` clause in a loop?
    a. To define an alternative condition for the loop
    b. To execute code if the loop completes normally
    c. To skip the current iteration and move to the next one
    d. To terminate the loop prematurely

11. What is the output of the following code?
    ```python
    for i in range(5):
        if i == 3:
            continue
        print(i)
    ```
    a. 0 1 2 4
    b. 0 1 2 3 4
    c. 3
    d. Error

12. What is the purpose of the `open()` function in Python?
    a. To create a new file
    b. To open an existing file
    c. To write to a file
    d. Both a and b

13. What mode should be used to open a file for appending content?
    a. 'r'
    b. 'w'
    c. 'a'
    d. 'x'

14. What is the output of the following code?
    ```python
    my_list = [1, 2, 3, 4, 5]
    my_list[2] = 10
    print(my_list)
    ```
    a. [1, 2, 10, 4, 5]
    b. [1, 2, 3, 4, 5]
    c. Error
    d. None

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

1. Write a Python function to find the second-largest number in a list.

2. Write a Python program to reverse a string using recursion.

3. Write a Python function to calculate the greatest common divisor (GCD) of two numbers using recursion.

4. Write a Python program to print the pattern of a pyramid using nested loops.

5. Write a Python function to find the most common value in a dictionary.

6. Write a Python program to remove all key-value pairs from a dictionary where the value is greater than a given number.

7. Write a Python program to generate all possible combinations of a given length from a list of elements using nested loops.

8. Write a Python program to check if a given string is a palindrome using recursion.

9. Write a Python function to find the sum of digits of a given number using recursion.

10. Write a Python program to transpose a matrix (a list of lists) using nested loops.

Answers:

Multiple Choice Questions:

1. d
2. b
3. d
4. a
5. a
6. b
7. c
8. a
9. a
10. b
11. a
12. d
13. c
14. a
15. b

Coding Problems:

1. ```python
   def find_second_largest(lst):
       if len(lst) < 2:
           return None
       largest = max(lst)
       lst.remove(largest)
       second_largest = max(lst)
       return second_largest
   ```

2. ```python
   def reverse_string(s):
       if len(s) == 0:
           return s
       else:
           return reverse_string(s[1:]) + s[0]
   ```

3. ```python
   def gcd(a, b):
       if b == 0:
           return a
       else:
           return gcd(b, a % b)
   ```

4. ```python
   def print_pyramid(n):
       for i in range(n):
           for j in range(n - i - 1):
               print(" ", end="")
           for j in range(i + 1):
               print("* ", end="")
           print()
   ```

5. ```python
   def most_common_value(d):
       values = d.values()
       max_count = max(values.count(value) for value in set(values))
       return [value for value in set(values) if values.count(value) == max_count]
   ```

6. ```python
   def remove_greater(d, threshold):
       return {k: v for k, v in d.items() if v <= threshold}
   ```

7. ```python
   def generate_combinations(elements, length):
       def backtrack(start, combination):
           if len(combination) == length:
               result.append(combination[:])
               return
           for i in range(start, len(elements)):
               combination.append(elements[i])
               backtrack(i + 1, combination)
               combination.pop()

       result = []
       backtrack(0, [])
       return result
   ```

8. ```python
   def is_palindrome(s):
       if len(s) <= 1:
           return True
       else:
           return s[0] == s[-1] and is_palindrome(s[1:-1])
Here are the last 2 coding problem answers:

9. ```python
   def sum_of_digits(n):
       if n < 10:
           return n
       else:
           return n % 10 + sum_of_digits(n // 10)
   ```

10. ```python
    def transpose_matrix(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[0 for j in range(rows)] for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed
    ```

Explanation:

9. **Sum of Digits (Recursion):**
   - The `sum_of_digits` function takes an integer `n` as input.
   - The base case is when `n` is less than 10, in which case the function simply returns `n`.
   - In the recursive case, the function extracts the last digit of `n` using `n % 10` and recursively calls `sum_of_digits` with `n // 10` (integer division to remove the last digit).
   - The sum of the last digit and the recursive call result is returned as the final answer.

10. **Transpose Matrix (Nested Loops):**
    - The `transpose_matrix` function takes a matrix (list of lists) as input.
    - The number of rows and columns in the matrix is determined using `len(matrix)` and `len(matrix[0])`, respectively.
    - A new matrix `transposed` is created with the dimensions swapped (cols x rows).
    - Two nested loops iterate over the original matrix, and the elements are swapped between the original and the transposed matrix.
    - The final transposed matrix is returned.

These solutions demonstrate the use of recursion and nested loops to solve complex problems involving strings, numbers, and data structures like matrices and dictionaries.
