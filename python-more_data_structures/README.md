# Python - More Data Structures: Set, Dictionary

## Learning Objectives

### General

1. Why Python programming is awesome
2. What are set and how to use them
3. What are the most common methods of set and how to use them
4. When to use sets versus lists
5. How to iterate into a set
6. What are dictionary and how to use them
7. When to use dictionaries versus lists or sets
8. What is a key in a dictionary
9. How to iterate into a dictionary
10. What is a lambda function
11. What is map, reduce and filter functions

## Requirements

1. Recommended editors: Visual studio code
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. A README.md file, at the root of the folder of the project, is mandatory
5. Your code should use the PEP 8 style (version 1.7.*)
6. The length of your files will be tested using wc

## Tasks

### 0.  Squared simple

Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):

matrix is a 2 dimensional array

Returns a new matrix:

Same size as matrix

Each value should be the square of the value of the input

Initial matrix should not be modified

You are not allowed to import any module

You are allowed to use regular loops, map, etc.

    guillaume@ubuntu:~/$ cat 0-main.py

    #!/usr/bin/python3

    square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)

    print(new_matrix)

    print(matrix)

    guillaume@ubuntu:~/$ ./0-main.py

    [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    guillaume@ubuntu:~/$ 

### 1.  Present in both

Write a function that returns a set of common elements in two sets.

Prototype: def common_elements(set_1, set_2):

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 1-main.py

    #!/usr/bin/python3

    common_elements = __import__('1-common_elements').common_elements

    set_1 = { "Python", "C", "Javascript" }

    set_2 = { "Bash", "C", "Ruby", "Perl" }

    c_set = common_elements(set_1, set_2)

    print(sorted(list(c_set)))

    guillaume@ubuntu:~/$ ./1-main.py

    ['C']

    guillaume@ubuntu:~/$ 

### 2. Update dictionary

Write a function that replaces or adds key/value in a dictionary.

Prototype: def update_dictionary(a_dictionary, key, value):

key argument will be always a string

value argument will be any type

If a key exists in the dictionary, the value will be replaced

If a key doesn’t exist in the dictionary, it will be created

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 2-main.py
    
    #!/usr/bin/python3
    
    update_dictionary = __import__('2-update_dictionary').update_dictionary

    def print_sorted_dictionary(my_dict):
    
        """ Print sorted dictionary """
    
        keys = sorted(my_dict.keys())
    
        for k in keys:
            print("{}: {}".format(k, my_dict[k]))

    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    
    print_sorted_dictionary(new_dict)
    
    print("--")

    print_sorted_dictionary(a_dictionary)

    print("--")
    
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    
    print_sorted_dictionary(new_dict)
    
    print("--")
    
    print_sorted_dictionary(a_dictionary)

    guillaume@ubuntu:~/$ ./2-main.py
    
    language: Python
    
    number: 89
    
    track: Low level
    
    --
    
    language: Python
    
    number: 89
    
    track: Low level
    
    --
    
    --
    
    city: San Francisco
    
    language: Python

    number: 89

    track: Low level

    --

    city: San Francisco

    language: Python

    number: 89

    track: Low level

    guillaume@ubuntu:~/$ 

### 3.  Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):

You can assume that all values are only integers

If no score found, return None

You can assume all students have a different score

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 3-main.py
    
    #!/usr/bin/python3
    
    best_score = __import__('3-best_score').best_score

    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    
    best_key = best_score(a_dictionary)
    
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    
    print("Best score: {}".format(best_key))

    guillaume@ubuntu:~/$ ./3-main.py
    
    Best score: Molly
    
    Best score: None
    
    guillaume@ubuntu:~/$ 

### 4.  Multiply by using map

Write a function that returns a list with all values multiplied by a number without using any loops.

Prototype: def multiply_list_map(my_list=[], number=0):

Returns a new list:

Same length as my_list

Each value should be multiplied by number

Initial list should not be modified

You are not allowed to import any module

You have to use map

Your file should be max 3 lines

    guillaume@ubuntu:~/$ cat 4-main.py
    
    #!/usr/bin/python3
    
    multiply_list_map = __import__('4-multiply_list_map').multiply_list_map

    
    my_list = [1, 2, 3, 4, 6]
    
    new_list = multiply_list_map(my_list, 4)
    
    print(new_list)
    
    print(my_list)

    guillaume@ubuntu:~/$ ./4-main.py
    
    [4, 8, 12, 16, 24]
    
    [1, 2, 3, 4, 6]
    
    guillaume@ubuntu:~/$ 

## Contributing

Contributions make the open source community such an amazing place to learn, create and more. Any contributions you make are appreciated.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/GreatPiece)
3. Commit your Changes (git commit -m 'Adding a GreatPiece')
4. Push to the Branch (git push origin feature/GreatPiece)
5. Open a Pull Request

## License & Copyright

Distributed under MIT license. See LICENSE.txt for more information.

In regards with copyright, all lie with the developer

## Contact

Hezrone Okoth - @that_heazrone - hezrone.okoth@icloud.com

Project Link: https://github.com/hezroneokoth/alx_python

## Acknowledgments

This is a list of resources that I have used during the course of this project;

ALX School Concept Page

https://docs.python.org/3/tutorial/datastructures.html

https://python-course.eu/advanced-python/lambda-filter-reduce-map.php

https://www.youtube.com/watch?v=1GAC6KQUPeg
