### Slicing String:
- string[start_index:end_index]
- string[start_index:end_index:step_index]
    ```
    text = "nandrahulbeena"
    print(text[0:4]) # nand
    ```

### Slicing List:
- string[start_index:end_index]
- string[start_index:end_index:step_index]
    ```
    my_list = ['apple', 'banana', 'cherry', 'date']
    print(my_list[1:3]) #['banana', 'cherry']
    print(my_list[:2]) #['apple', 'banana']
    print(my_list[2:]) #['cherry', 'date']
    ```

### Slicing List of Numbers
- number_list[start_index:end_index:step_size]
    ```
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd_numbers = numbers[::2] #[1, 3, 5, 7, 9]
    ```

### Dictionary
- Dictionary: Key of an element in the dictionary should be immmutable
- string => immutable => hashable => ok
- int => immutable => hashable => ok
- float => immutable => hashable => ok
- tuple => immutable => hashable => ok
- list => mutable => unhashable => compile error

### Range Syntax
- for i in range(3):
- values of i in above range are -> 0, 1, 2

## Revision
10, 13 
