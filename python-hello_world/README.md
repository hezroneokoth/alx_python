# Python - Hello, World

## Python

## Learning Objectives

Why Python programming is awesome
Who created Python
Who is Guido van Rossum
Where does the name ‘Python’ come from
What is the Zen of Python
How to use the Python interpreter
How to print text and variables using print
How to use strings
What are indexing and slicing in Python
What is the official Holberton Python coding style and how to check your code with PEP 8
Why indentation is so important in Python
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use the while and for loops
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them

## Requirements

### Python Scripts

1. Recommended editors: Visual studio code
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. A README.md file at the root of the alx_python repo, containing a description of the repository
5. A README.md file, at the root of the folder of this project, is mandatory
6. The length of your files will be tested using wc

## Tasks

### 0. Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print

    guillaume@ubuntu:~/py/$ python3 0-print.py

    "Programming is like building a multilingual puzzle

    guillaume@ubuntu:~/py/$

### 1. Copy - Cut - Paste

Complete this 1-edges.py

You can find the source code 1-edges.py

You are not allowed to use any loops or conditional statements

Your program should be exactly 8 lines long

word_first_3 should contain the first 3 letters of the variable word

word_last_2 should contain the last 2 letters of the variable word

middle_word should contain the value of the variable word without the first and last letters

    guillaume@ubuntu:~/py/$ python3 1-edges.py

    First 3 letters: Hol

    Last 2 letters: on

    Middle word: olberto

    guillaume@ubuntu:~/py/$ wc -l 1-edges.py

    8 1-edges.py

    guillaume@ubuntu:~/py/$

### 2. Positive anything is better than negative nothing

This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

You can find the source code 2-pon.py

The variable number will store a different value every time you will run this program

You don’t have to understand what import, random. randint do. Please do not touch this code

The output of the program should be:

The number, followed by

if the number is greater than 0: is positive

if the number is 0: is zero

if the number is less than 0: is negative

followed by a new line

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    -4 is negative

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    0 is zero

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    -3 is negative

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    -10 is negative

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    10 is positive

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    -5 is negative

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    6 is positive

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    7 is positive

    guillaume@ubuntu:~/$ python3 2-positive_or_negative.py 

    5 is positive

    guillaume@ubuntu:~/$ 

### 3. The last digit

This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

You can find the source code 3-last_digit.py

The variable number will store a different value every time you will run this program

You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)

The output of the program should be:

The string Last digit of, followed by

the number, followed by

the string is, followed by the last digit of number, followed by

if the last digit is greater than 5: the string and is greater than 5

if the last digit is 0: the string and is 0

if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of 4205 is 5 and is less than 6 and not 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of -626 is -6 and is less than 6 and not 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of 1144 is 4 and is less than 6 and not 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of -9200 is 0 and is 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of 5247 is 7 and is greater than 5

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of -9318 is -8 and is less than 6 and not 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of 3369 is 9 and is greater than 5

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of -5224 is -4 and is less than 6 and not 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of -4485 is -5 and is less than 6 and not 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of 3850 is 0 and is 0

    guillaume@ubuntu:~/$ python3 3-last_digit.py

    Last digit of 5169 is 9 and is greater than 5

    guillaume@ubuntu:~/$ 

### 4. Hexadecimal printing

Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

You can only use one print function with string format

You can only use one loop in your code

You are not allowed to store numbers or strings in a variable

You are not allowed to import any module

    guillaume@ubuntu:~/$ python3 4-print_hexa.py

    0 = 0x0

    1 = 0x1

    2 = 0x2

    3 = 0x3

    4 = 0x4

    5 = 0x5

    6 = 0x6

    7 = 0x7

    8 = 0x8

    9 = 0x9

    10 = 0xa

    11 = 0xb

    12 = 0xc

    13 = 0xd

    14 = 0xe

    15 = 0xf

    16 = 0x10

    17 = 0x11

    18 = 0x12

    ...

    96 = 0x60

    97 = 0x61

    98 = 0x62

    guillaume@ubuntu:~/$

### 5. 00...99

Write a program that prints numbers from 0 to 99.

Numbers must be separated by ,, followed by a space

Numbers should be printed in ascending order, with two digits

The last number should be followed by a new line

You can only use no more than 2 print functions with string format

You can only use one loop in your code

You are not allowed to store numbers or strings in a variable

You are not allowed to import any module

    guillaume@ubuntu:~/$ python3 5-print_comb2.py

    00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99

    guillaume@ubuntu:~/$ 

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need

Write a program that prints all possible different combinations of two digits.

Numbers must be separated by ,, followed by a space

The two digits must be different

01 and 10 are considered the same combination of the two digits 0 and 1

Print only the smallest combination of two digits

Numbers should be printed in ascending order, with two digits

The last number should be followed by a new line

You can only use no more than 3 print functions with string format

You can only use no more than 2 loops in your code

You are not allowed to store numbers or strings in a variable

You are not allowed to import any module

    guillaume@ubuntu:~/$ python3 6-print_comb3.py

    01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89

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

In regards with copyright, all lie with the developer

## Contact

Hezrone Okoth

twitter @that_heazrone

Project Link: https://github.com/hezroneokoth/alx_python

## Acknowledgments

This is a list of resources that I have used during the course of this project;

ALX School Concept Page

How to Install Python - https://realpython.com/installing-python/

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