# Topic 1: Non-Recursive Bounded Loops

## Summary
Non-recursive bounded loops are loops that have a fixed, predetermined number of iterations. They are useful for solving problems that require iterating over a collection of objects or performing a specific set of operations a known number of times.

## Detailed Explanation
In Python, non-recursive bounded loops can be implemented using the `for` loop or the `while` loop with a condition that ensures the loop terminates after a fixed number of iterations. The `for` loop is typically used to iterate over iterable objects such as lists, tuples, strings, or other sequences. The `while` loop is useful when the number of iterations depends on a specific condition being met.

### Examples

#### Example 1: Using a `for` loop to iterate over a list
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

#### Example 2: Using a `while` loop with a counter
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
Output:
```
0
1
2
3
4
```

## Questions

### Multiple Choice Questions

1. Which loop is typically used to iterate over a collection of objects in Python?
   a. `for` loop
   b. `while` loop
   c. `do-while` loop
   d. `repeat` loop

2. What is the purpose of the `range()` function in Python?
   a. To create a sequence of numbers
   b. To iterate over a list
   c. To create a new list
   d. To sort a list

3. Which loop construct is better suited for iterating over a sequence of objects when the number of iterations is known in advance?
   a. `for` loop
   b. `while` loop
   c. Both `for` and `while` loops are equally suitable
   d. Neither `for` nor `while` loop is suitable

### Coding Exercises

4. Write a Python program that prints the even numbers from 1 to 10 using a `for` loop.

5. Write a Python program that calculates the sum of all numbers from 1 to 100 using a `while` loop.

6. Write a Python program that prints the elements of a list in reverse order using a `for` loop.

7. Write a Python program that calculates the factorial of a given number using a `while` loop.

8. Write a Python program that prints the first 10 Fibonacci numbers using a `for` loop.

9. Write a Python program that finds the largest number in a list of integers using a `for` loop.

10. Write a Python program that counts the number of vowels in a given string using a `for` loop.

# Topic 2: Recursive Bounded Loops

## Summary
Recursive bounded loops are a type of recursion where the recursive function calls itself a fixed number of times, and the recursion terminates after a predetermined number of iterations. These loops are useful when the problem can be broken down into smaller subproblems that have a similar structure.

## Detailed Explanation
In Python, recursive bounded loops are implemented using recursive functions. A recursive function is a function that calls itself with a different set of input parameters until a base case is reached. The base case is the condition that stops the recursion and provides a solution to the problem.

Recursive bounded loops typically involve two parts: the base case and the recursive case. The base case is the terminating condition that stops the recursion, while the recursive case is the step that breaks down the problem into smaller subproblems and calls the function again with new input parameters.

### Examples

#### Example 1: Calculating the factorial of a number using recursion
```python
def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120
```

#### Example 2: Printing numbers in reverse order using recursion
```python
def print_reverse(n):
    if n > 0:
        print(n)
        print_reverse(n - 1)  # Recursive case
    else:
        return  # Base case

print_reverse(5)
```
Output:
```
5
4
3
2
1
```

## Questions

### Multiple Choice Questions

1. Which of the following is a necessary component of a recursive function?
   a. Base case
   b. Recursive case
   c. Both base case and recursive case
   d. Neither base case nor recursive case

2. What is the purpose of the base case in a recursive function?
   a. To provide a solution to the problem
   b. To call the function again with different input parameters
   c. To break down the problem into smaller subproblems
   d. None of the above

3. Which of the following is an advantage of using recursion over iterative approaches?
   a. Recursion is generally more efficient than iterative approaches
   b. Recursive solutions are often easier to understand and implement
   c. Recursion can handle problems with unknown or unbounded input sizes
   d. All of the above

### Coding Exercises

4. Write a Python function that calculates the nth Fibonacci number using recursion.

5. Write a Python function that returns the sum of digits of a given number using recursion.

6. Write a Python function that reverses a given string using recursion.

7. Write a Python function that calculates the greatest common divisor (GCD) of two numbers using recursion.

8. Write a Python function that checks if a given string is a palindrome using recursion.

9. Write a Python function that finds the sum of elements in a list using recursion.

10. Write a Python function that calculates the power of a number raised to a given exponent using recursion.

# Topic 3: Non-Recursive Unbounded Loops

## Summary
Non-recursive unbounded loops are loops that do not have a predetermined or fixed number of iterations. Instead, the number of iterations depends on a specific condition being met, which can be unknown or variable. These loops are useful when solving problems where the input size or the number of iterations required is not known in advance.

## Detailed Explanation
In Python, non-recursive unbounded loops can be implemented using the `while` loop or the `for` loop with an iterable object that has a variable or unknown length. The `while` loop is typically used when the loop condition depends on a specific condition being met, while the `for` loop is often used when iterating over an iterable object with an unknown or variable length.

It's important to ensure that the loop condition eventually becomes false to prevent infinite loops, which can lead to program crashes or excessive resource consumption.

### Examples

#### Example 1: Using a `while` loop to read user input until a specific condition is met
```python
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter some text (or 'quit' to exit): ")
    if user_input.lower() != "quit":
        print("You entered:", user_input)
```

#### Example 2: Using a `for` loop to iterate over a list until a specific condition is met
```python
numbers = []
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    else:
        numbers.append(int(user_input))

for number in numbers:
    print(number)
```

## Questions

### Multiple Choice Questions

1. Which loop construct is typically used for non-recursive unbounded loops in Python?
   a. `for` loop
   b. `while` loop
   c. Both `for` and `while` loops
   d. Neither `for` nor `while` loop

2. What is the purpose of the `break` statement in a loop?
   a. To terminate the loop immediately
   b. To skip the current iteration and move to the next one
   c. To start a new loop
   d. None of the above

3. Which of the following is a common use case for non-recursive unbounded loops?
   a. Iterating over a list of known length
   b. Reading user input until a specific condition is met
   c. Calculating the factorial of a number
   d. Reversing a string

### Coding Exercises


4. Write a Python program that reads numbers from the user until they enter a negative number, then prints the sum of all positive numbers entered.

5. Write a Python program that generates random numbers between 1 and 100 and keeps track of the largest number generated until the user decides to quit.

6. Write a Python program that reads words from the user until they enter an empty string, then prints the longest word entered.

7. Write a Python program that reads integers from the user until they enter 0, then prints the count of even and odd numbers entered.

8. Write a Python program that reads lines of text from the user until they enter an empty line, then prints the text with line numbers.

9. Write a Python program that reads integers from the user until they enter a negative number, then prints the second largest number entered.

10. Write a Python program that reads strings from the user until they enter "quit", then prints the unique strings entered in alphabetical order.

# Topic 4: Nested Loops

## Summary
Nested loops are loops that are placed inside other loops. They are used when you need to iterate over multiple sequences or perform operations that require nested iterations. Nested loops can be used with both bounded and unbounded loops, and they can be recursive or non-recursive.

## Detailed Explanation
In Python, nested loops can be implemented using any combination of `for` and `while` loops. The outer loop controls the outer iteration, while the inner loop controls the inner iteration. Each iteration of the outer loop triggers a complete iteration of the inner loop.

Nested loops can be useful for processing multidimensional data structures like matrices or lists of lists, or for generating combinations or permutations of elements from multiple sequences.

### Examples

#### Example 1: Printing a multiplication table using nested `for` loops
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
```

#### Example 2: Finding all pairs of numbers in two lists that sum to a target value using nested loops
```python
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
target = 9

for num1 in list1:
    for num2 in list2:
        if num1 + num2 == target:
            print(f"({num1}, {num2})")
```

## Questions

### Multiple Choice Questions

1. Which of the following is true about nested loops?
   a. The inner loop executes completely for each iteration of the outer loop
   b. The outer loop executes completely for each iteration of the inner loop
   c. Both the inner and outer loops execute completely for each iteration
   d. None of the above

2. What is a common use case for nested loops?
   a. Iterating over multidimensional data structures
   b. Generating combinations or permutations
   c. Processing nested data structures
   d. All of the above

3. Which loop construct is typically used for the outer loop in nested loops?
   a. `for` loop
   b. `while` loop
   c. Both `for` and `while` loops can be used
   d. Neither `for` nor `while` loop is suitable

### Coding Exercises

4. Write a Python program that prints a square pattern of asterisks using nested loops, where the side length is specified by the user.

5. Write a Python program that finds all pairs of numbers from two lists that have a difference less than a given value using nested loops.

6. Write a Python program that transposes a matrix (a list of lists) using nested loops.

7. Write a Python program that generates all possible combinations of a given length from a list of elements using nested loops.

8. Write a Python program that finds the common elements between two lists using nested loops.

9. Write a Python program that generates a multiplication table up to a given value using nested `while` loops.

10. Write a Python program that finds all prime numbers up to a given value using nested loops.

This covers the topics of non-recursive bounded loops, recursive bounded loops, non-recursive unbounded loops, and nested loops. Each topic includes a summary, detailed explanation, examples, multiple choice questions, and coding exercises to help you master the concepts.
