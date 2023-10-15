# Python - functions

## Learning Objectives

### General

1. What are functions
2. How to define and call a function
3. What are parameters and arguments
4. The role of the return statement in functions
5. Difference between built in functions and user-defined functions
6. How to write functions to solve specific tasks and improve code reusability

## Requirements

### Python Scripts

1. Recommended editors: Visual studio code
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. A README.md file at the root of the python-coding repo, containing a description of the repository
5. A README.md file, at the root of the folder of this project, is mandatory
6. The length of your files will be tested using wc

## Tasks

### 0. 0. a + b

Write a function that adds two integers and returns the result.

Prototype: def add(a, b):

Returns the value of a + b

You are not allowed to import any module

You don’t need to understand __import__

    guillaume@ubuntu:~/$ cat 0-main.py

    #!/usr/bin/env python3

    add = __import__('0-sum').add

    print(add(1, 2))

    print(add(98, 0))

    print(add(100, -2))


    guillaume@ubuntu:~/$ ./0-main.py

    3

    98

    98

    guillaume@ubuntu:~/$ 

### 1. a ^ b

Write a function that computes a to the power of b and return the value.

Prototype: def pow(a, b):

Returns the value of a ^ b

You are not allowed to import any module

You don’t need to understand __import__

    guillaume@ubuntu:~/$ cat 1-main.py

    #!/usr/bin/env python3

    pow = __import__('1-power').pow

    print(pow(2, 2))

    print(pow(98, 2))

    print(pow(98, 0))

    print(pow(100, -2))

    print(pow(-4, 5))

    guillaume@ubuntu:~/$ ./1-main.py

    4

    9604

    1

    0.0001

    -1024

    guillaume@ubuntu:~/$ 

### 2. Temperature Converter Function

Write a Python function called convert_to_celsius that takes a temperature in Fahrenheit as input and returns the temperature in Celsius.

Prototype: def convert_to_celsius(fahrenheit)

Returns the temperature in Celsius

You are not allowed to import any module.

You don’t need to understand __import__

    guillaume@ubuntu:~/$ cat 2-main.py

    #!/usr/bin/env python3

    convert_to_celsius = __import__('2-temperature').convert_to_celsius


    print(convert_to_celsius(100))

    print(convert_to_celsius(-40))

    print(convert_to_celsius(-459.67))

    print(convert_to_celsius(32))


    guillaume@ubuntu:~/$ python3 2-main.py

    37.77777777777778

    -40

    -273.15

    0.0


    guillaume@ubuntu:~/$ 

### 3. String Manipulation Function

Write a Python function called reverse_string that takes a string as input and returns the reverse of that string.

Prototype: def reverse_string(string)

Returns the reversed string.

You are not allowed to import any module.

You don’t need to understand __import__

    guillaume@ubuntu:~/$ cat 3-main.py

    #!/usr/bin/env python3

    reverse_string = __import__('3-string').reverse_string
​
    print(reverse_string("Hello"))

    print(reverse_string(""))

    print(reverse_string("madam"))

    print(reverse_string("Hello, World!"))

​
    guillaume@ubuntu:~/$ python3 3-main.py

    olleH


    madam

    !dlroW ,olleH
​
    guillaume@ubuntu:~/$

### 4. Fibonacci Sequence Function

Write a Python function called fibonacci_sequence that takes a number n as input and returns a list of the first n Fibonacci numbers.

Prototype: def fibonacci_sequence(n)

Returns a list of the first n Fibonacci numbers.You are not allowed to import any module.

Return an empty list if the it is not possible to generate the Fibonacci numbers for n

You don’t need to understand __import__

    guillaume@ubuntu:~/$ cat 4-main.py

    #!/usr/bin/env python3

        fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence
​
    print(fibonacci_sequence(6))

    print(fibonacci_sequence(1))

    print(fibonacci_sequence(0))

    print(fibonacci_sequence(20))

​
    guillaume@ubuntu:~/$ python3 4-main.py

    [0, 1, 1, 2, 3, 5]

    [0]

    []

    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
​

    guillaume@ubuntu:~/$ 

### 5. Prime Number Function

Write a Python function called is_prime that takes a number as input and returns True if the number is prime, and False otherwise.

Prototype: def is_prime(number)

Returns True if the number is prime, and False otherwise.

You are not allowed to import any module.

You don’t need to understand __import__

    guillaume@ubuntu:~/$ cat 5-main.py

    #!/usr/bin/env python3

    is_prime = __import__('5-prime').is_prime
​
    print(is_prime(17))

    print(is_prime(15))

    print(is_prime(-5))

    print(is_prime(0))
​
    guillaume@ubuntu:~/$ python3 5-main.py

    True

    False

    False

    False
​
    guillaume@ubuntu:~/$

### 6. Password Validation Function

Write a Python function called validate_password that takes a password as input and performs the following checks:

The password should be at least 8 characters long.

The password should contain at least one uppercase letter, one lowercase letter, and one digit.

The password should not contain spaces.

Prototype: def validate_password(password)

Returns True if the password passes all the checks, and False otherwise.

You are not allowed to import any module.

You don’t need to understand __import__

    guillaume@ubuntu:~/$ cat 6-main.py

    #!/usr/bin/env python3
 
    validate_password = __import__('6-password').validate_password
​
    print(validate_password("Password123"))

    print(validate_password("abc123"))

    print(validate_password("Password 123"))

    print(validate_password("password123"))


    guillaume@ubuntu:~/$ python3 6-main.py

    True

    False

    False

    False
​
    guillaume@ubuntu:~/$

### Contributing

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

Project Link: https://github.com/hezroneokoth/alx_python

## Acknowledgments

This is a list of resources that I have used during the course of this project;

ALX School Concept Page

Python for Absolute beginners - https://www.digitalocean.com/community/tutorials/python-tutorial-beginners

Python Keywords Identifiers - https://www.digitalocean.com/community/tutorials/python-keywords-identifiers

Python Data Types - https://www.digitalocean.com/community/tutorials/python-keywords-identifiers

How to Code in Python3 - https://www.digitalocean.com/community/tutorial-series/how-to-code-in-python-3

The Python Tutorial - https://docs.python.org/3/tutorial/index.html

Whetting Your Appetite - https://docs.python.org/3/tutorial/appetite.html

Using the Python Interpreter - https://docs.python.org/3/tutorial/interpreter.html

An Informal Introduction to Python - https://docs.python.org/3/tutorial/introduction.html

How to Use String Formatters in Python3 - https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

Learn to Program - https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt

More Control Flow Tools - https://docs.python.org/3/tutorial/controlflow.html

Myths about indentation - https://www.meetup.com/

IdentationError - Video - https://www.youtube.com/watch?v=1QXOd2ZQs-Q

How To Use String Formatters in Python 3 - https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

Learn to Program - video - https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt

Learn to Program 2: Looping - video - https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt

PEP 8 - Style Guide for Python Code - https://peps.python.org/pep-0008/

Introductory Session - https://www.youtube.com/watch?time_continue=272&v=VufXHNY_Fz8&embeds_referring_euri=https%3A%2F%2Fintranet.alxswe.com%2F&source_ve_path=Mjg2NjY&feature=emb_logo

Live Learning Session - https://www.youtube.com/watch?time_continue=97&v=P2khHYKKZv8&embeds_referring_euri=https%3A%2F%2Fintranet.alxswe.com%2F&feature=emb_logo 