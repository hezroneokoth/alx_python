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

## Quiz

### Question #0

What do these lines print?

    >>> def my_function(counter):

    >>>     print("Counter: {}".format(counter))

    >>> 

    >>> my_function(12)

Counter: 12

### Question #1

What do these lines print?

    >>> def my_function():

    >>>     print("In my function")

    >>> 

    >>> my_function()

In my function

### Question #2

What do these lines print?

    >>> def my_function(counter=89):

    >>>     print("Counter: {}".format(counter))

    >>> 

    >>> my_function()

Counter: 89

### Question #3

What do these lines print?

    >>> def my_function():

    >>>     print("In my function")

    >>> 

    >>> my_function

function my_function at …

### Question #4

What do these lines print?

    >>> def my_function(counter=89):

    >>>     return counter + 1

    >>> 

    >>> print(my_function())

90

### Question #5

What do these lines print?

    >>> def my_function(counter=89):

    >>>     print("Counter: {}".format(counter))

    >>> 

    >>> my_function(12)

Counter: 12

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

    guillaume@ubuntu:~/$ cat add_0.py

    #!/usr/bin/python3

    def add(a, b):
    
        """My addition function

        Args:
        
            a: first integer
        
            b: second integer

        Returns:
        
            The return value. a + b
    
        """
    
        return (a + b)

    guillaume@ubuntu:~/$ ./0-add.py

    1 + 2 = 3

    guillaume@ubuntu:~/$ cat 0-import_add.py

    __import__("0-add")

    guillaume@ubuntu:~/$ python3 0-import_add.py 

    guillaume@ubuntu:~/$ 

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

    guillaume@ubuntu:~/$ ./1-args.py 

    0 arguments.

    guillaume@ubuntu:~/$ ./1-args.py Hello

    1 argument:

    1: Hello

    guillaume@ubuntu:~/$ ./1-args.py Hello Holberton School 98 Battery street

    6 arguments:

    1: Hello

    2: Holberton

    3: School

    4: 98

    5: Battery

    6: street

    guillaume@ubuntu:~/$ 

### 2. Everything can be imported

Write a program that imports the variable a from the file variable_load_2.py and prints its value.

You are not allowed to use * for importing or __import__

Your code should not be executed when imported

    guillaume@ubuntu:~/$ cat variable_load_2.py

    #!/usr/bin/python3

    a = 98

    """Simple variable

    """


    guillaume@ubuntu:~/$ ./2-variable_load.py

    98

    guillaume@ubuntu:~/$

### 3. Integers division with debug

Write a function that divides 2 integers and prints the result.

Prototype: def safe_print_division(a, b):

You can assume that a and b are integers

The result of the division should print on the finally: section preceded by Inside result:

Returns the value of the division, otherwise: None

You have to use try: / except: / finally:

You have to use "{}".format() to print the result

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 3-main.py

    #!/usr/bin/python3

    safe_print_division = __import__('3-safe_print_division').safe_print_division


    a = 12

    b = 2

    result = safe_print_division(a, b)

    print("{:d} / {:d} = {}".format(a, b, result))


    a = 12

    b = 0

    result = safe_print_division(a, b)

    print("{:d} / {:d} = {}".format(a, b, result))


    guillaume@ubuntu:~/$ ./3-main.py

    Inside result: 6.0

    12 / 2 = 6.0

    Inside result: None

    12 / 0 = None

    guillaume@ubuntu:~/$ 

### 4. Raise exception

Write a function that raises a type exception.

Prototype: def raise_exception():

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 4-main.py

    #!/usr/bin/python3

    raise_exception = __import__('4-raise_exception').raise_exception

    try:
    
        raise_exception()

    except TypeError as te:
    
        print("Exception raised")


    guillaume@ubuntu:~/$ ./4-main.py

    Exception raised

    guillaume@ubuntu:~/$ 

### 5.  Raise a message

Write a function that raises a name exception with a message.

Prototype: def raise_exception_msg(message=""):

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 5-main.py

    #!/usr/bin/python3

    raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg


    try:
    
        raise_exception_msg("C is fun")

    except NameError as ne:
    
        print(ne)


    guillaume@ubuntu:~/$ ./5-main.py

    C is fun

    guillaume@ubuntu:~/$ 

## Contributing

Contributions make the open-source community such an amazing place to learn, create and more. Any contributions you make are appreciated.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/GreatCode)
3. Commit your Changes (git commit -m 'Adding a GreatCode')
4. Push to the Branch (git push origin feature/GreatCode)
5. Open a Pull Request

## License & Copyright

Distributed under MIT license. See LICENSE.txt for more information.

In regards with copyright, all lie with the author.

## Contact

Hezrone Okoth

twitter @that_heazrone

Blog - wordpress/lifesoddity.com

Project Link: https://github.com/hezroneokoth/alx_python

## Acknowledgments

This is a list of resources that I have used during the course of this project;

ALX School Concept Page

Modules - https://docs.python.org/3/tutorial/modules.html

Command line arguments - https://docs.python.org/3.4/tutorial/stdlib.html#command-line-arguments 

Errors and exceptions - https://docs.python.org/3/tutorial/errors.html

Learn to Program 11 Static & Exception Handling (starting a min 7) - https://www.youtube.com/watch?v=7vbgD-3s-w4 

PEP 8 Styles Guide for Python Code - https://peps.python.org/pep-0008/

Intro Session - https://youtu.be/OomtzlGVnVM

Live Learning Session - https://youtu.be/riP8gMnZX6Q