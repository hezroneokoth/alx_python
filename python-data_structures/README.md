# Python - Data Structures: Lists, Tuples

## Learning Objectives

### General

1. Why Python programming is awesome
2. What are lists and how to use them
3. What are the differences and similarities between strings and lists
4. What are the most common methods of lists and how to use them
5. How to use lists as stacks and queues
6. What are list comprehensions and how to use them
7. What are tuples and how to use them
8. When to use tuples versus lists
9. What is a sequence
10. What is tuple packing
11. What is sequence unpacking
12. What is the del statement and how to use it

## Requirements

1. Recommended editors: Visual studio code
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. A README.md file, at the root of the folder of the project, is mandatory
5. Your code should use the PEP 8 style (version 1.7.*)
6. The length of your files will be tested using wc

## Quiz questions

### Question #0

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> a[-3]

2

### Question #1

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> a[0]

1

### Question #2

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> b = a

    >>> b

[1, 2, 3, 4]

### Question #3

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> a.append(5)

    >>> len(a)

5

### Question #4

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> b = a

    >>> a[2] = 10

    >>> a

[1, 2, 10, 4]

### Question #5

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> a[-1]

4

### Question #6

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> b = a

    >>> a[2] = 10

    >>> b

[1, 2, 10, 4]

### Question #7

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> a[2] = 10

    >>> a

[1, 2, 10, 4]

### Question #8

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> a[1:3]

[2, 3]

### Question #9

What do these lines print?

    >>> a = [1, 2, 3, 4]

    >>> len(a)

4

## Tasks

### 0. Can you C me now?

Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):

The function should return the new string

You are not allowed to import any module

You are not allowed to use str.replace()

    guillaume@ubuntu:~/$ cat 0-main.py

    #!/usr/bin/env python3

    no_c = __import__('0-no_c').no_c


    print(no_c("Holberton School"))

    print(no_c("Chicago"))

    print(no_c("C is fun!"))


    guillaume@ubuntu:~/$ ./0-main.py

    Holberton Shool

    hiago
 
    is fun!

    guillaume@ubuntu:~/$ 

### 1.  Lists of lists = Matrix

Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):

Format: see example

You are not allowed to import any module

You can assume that the list only contains integers

You are not allowed to cast integers into strings

You have to use str.format() to print integers

    guillaume@ubuntu:~/$ cat 1-main.py

    #!/usr/bin/python3

    print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer


    matrix = [
    
        [1, 2, 3],
    
        [4, 5, 6],
    
        [7, 8, 9]

    ]


    print_matrix_integer(matrix)

    print("--")

    print_matrix_integer()


    guillaume@ubuntu:~/$ ./1-main.py | cat -e

    1 2 3$

    4 5 6$

    7 8 9$

    --$

    $

    guillaume@ubuntu:~/$ 

### 2. More returns

Write a function that returns a tuple with the length of a string and its first character.

Prototype: def multiple_returns(sentence):

If the sentence is empty, the first character should be equal to None

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 2-main.py

    #!/usr/bin/python3

    multiple_returns = __import__('2-multiple_returns').multiple_returns


    sentence = "At Holberton school, I learnt C!"

    length, first = multiple_returns(sentence)

    print("Length: {:d} - First character: {}".format(length, first))


    guillaume@ubuntu:~/$ ./2-main.py

    Length: 32 - First character: A

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

x - @that_heazrone

blog - wordpress/lifesoddity.com

Project link - https://github.com/hezroneokoth/alx_python

## Acknowledgments

This is a list of resources that I have used during the course of this project;

ALX School Concept Page

3.1.3. Lists - https://docs.python.org/3.4/tutorial/introduction.html#lists

Data Structures - https://docs.python.org/3/tutorial/datastructures.html

Learn to Program 6: Lists - https://www.youtube.com/watch?v=A1HUzrvS-Pw