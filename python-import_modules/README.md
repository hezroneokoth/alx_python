# Python - import & modules

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

1. Why Python programming is awesome
2. How to import functions from another file
3. How to use imported functions
4. How to create a module
5. How to use the built-in function dir()
6. How to prevent code in your script from being executed when imported
7. How to use command line arguments with your Python programs
8. What’s the difference between errors and exceptions
9. What are exceptions and how to use them
10. When do we need to use exceptions
11. How to correctly handle an exception
12. What’s the purpose of catching exceptions
13. How to raise a builtin exception
14. When do we need to implement a clean-up action after an exception

## Requirements

1. Recommended editors: Visual studio code
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. A README.md file, at the root of the folder of the project, is mandatory
5. Your code should use the PEP 8 style (version 1.7.*)
6. The length of your files will be tested using wc

## Tasks

### 0. Import a simple function from a simple file

Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

You have to use print function with string format to display integers

You have to assign:

the value 1 to a variable called a

the value 2 to a variable called b

and use those two variables as arguments when calling the functions add and print

a and b must be defined in 2 different lines: a = 1 and another b = 2

Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line

You can only use the word add_0 once in your code

You are not allowed to use * for importing or __import__

Your code should not be executed when imported - by using __import__, like the example below

### 1. How to make a script dynamic

Write a program that prints the number of and the list of its arguments.

The output should be:

Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by

: (or . if no arguments were passed) followed by

a new line, followed by (if at least one argument),

one line per argument:

the position of the argument (starting at 1) followed by :, followed by the argument value and a new line

Your code should not be executed when imported

The number of elements of argv can be retrieved by using: len(argv)

You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it.

There are other ways (which will be preferred for future project tasks), if you know them you can use them.

### 2. Everything can be imported

Write a program that imports the variable a from the file variable_load_2.py and prints its value.

You are not allowed to use * for importing or __import__

Your code should not be executed when imported

### 3. Integers division with debug

Write a function that divides 2 integers and prints the result.

Prototype: def safe_print_division(a, b):

You can assume that a and b are integers

The result of the division should print on the finally: section preceded by Inside result:

Returns the value of the division, otherwise: None

You have to use try: / except: / finally:

You have to use "{}".format() to print the result

You are not allowed to import any module

### 4. Raise exception

Write a function that raises a type exception.

Prototype: def raise_exception():

You are not allowed to import any module

### 5.  Raise a message

Write a function that raises a name exception with a message.

Prototype: def raise_exception_msg(message=""):

You are not allowed to import any module

## Collaborators

This is solely the work of Hezrone Okoth

## License & Copyright

Students and Developers can use this code however they can so long as it does not infringe on exsting regulations

Caution should be exercised

In regards with copyright, all lie with the developer
