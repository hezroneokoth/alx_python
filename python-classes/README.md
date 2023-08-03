# Python - Classes and Objects

## Python      OOP

## Background Context

OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

## Learning Objectives

### General

1. Why Python programming is awesome
2. What is OOP
3. “first-class everything”
4. What is a class
5. What is an object and an instance
6. What is the difference between a class and an object or instance
7. What is an attribute
8. What are and how to use public, protected and private attributes
9. What is self
10. What is a method
11. What is the special __init__ method and how to use it
12. What is Data Abstraction, Data Encapsulation, and Information Hiding
13. What is a property
14. What is the difference between an attribute and a property in Python
15. What is the Pythonic way to write getters and setters in Python
16. How to dynamically create arbitrary new attributes for existing instances of a class
17. How to bind attributes to object and classes
18. What is the __dict__ of a class and/or instance of a class and what does it contain
19. How does Python find the attributes of an object or class
20. How to use the getattr function

## Requirements

1. Recommended editors: Visual studio code
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. A README.md file, at the root of the folder of the project, is mandatory
5. Your code should use the PEP 8 style (version 1.7.*)
6. The length of your files will be tested using wc
7. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
8. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
9. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
10. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 0.   Square with size

Write a class Square that defines a square by:

Private instance attribute: size

Instantiation with size (no type/value verification)

You are not allowed to import any module

Why?

 Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

    guillaume@ubuntu:~/$ cat 0-main.py

    #!/usr/bin/python3

    Square = __import__('0-square').Square

    my_square = Square(3)

    print(type(my_square))

    print(my_square.__dict__)

    try:
    
        print(my_square.size)

    except Exception as e:
    
        print(e)

    try:
    
        print(my_square.__size)

    except Exception as e:
    
        print(e)

    guillaume@ubuntu:~/$ python3 0-main.py

    <class '0-square.Square'>

    {'_Square__size': 3}

    'Square' object has no attribute 'size'

    'Square' object has no attribute '__size'

    guillaume@ubuntu:~/$ 

### 1.   Size validation

Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size

Instantiation with optional size: def __init__(self, size=0):

size must be an integer, otherwise raise a TypeError exception with 
the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 1-main.py

    #!/usr/bin/python3

    Square = __import__('1-square').Square

    my_square_1 = Square(3)

    print(type(my_square_1))

    print(my_square_1.__dict__)

    my_square_2 = Square()

    print(type(my_square_2))

    print(my_square_2.__dict__)

    try:
    
        print(my_square_1.size)

    except Exception as e:
    
        print(e)

    try:
    
        print(my_square_1.__size)

    except Exception as e:
    
        print(e)

    try:
    
        my_square_3 = Square("3")
    
        print(type(my_square_3))
    
        print(my_square_3.__dict__)

    except Exception as e:
    
        print(e)

    try:
    
        my_square_4 = Square(-89)
    
        print(type(my_square_4))
    
        print(my_square_4.__dict__)

    except Exception as e:
    
        print(e)


    guillaume@ubuntu:~/$ python3 1-main.py

    <class '1-square.Square'>

    {'_Square__size': 3}

    <class '1-square.Square'>

    {'_Square__size': 0}

    'Square' object has no attribute 'size'

    'Square' object has no attribute '__size'

    size must be an integer

    size must be >= 0

    guillaume@ubuntu:~/$ 

### 2. Area of a square

Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size

Instantiation with optional size: def __init__(self, size=0):

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0

Public instance method: def area(self): that returns the current square area

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 2-main.py

    #!/usr/bin/python3

    Square = __import__('2-square').Square

    my_square_1 = Square(3)

    print("Area: {}".format(my_square_1.area()))

    try:

        print(my_square_1.size)

    except Exception as e:

        print(e)

    try:

        print(my_square_1.__size)

    except Exception as e:

        print(e)

    my_square_2 = Square(5)

    print("Area: {}".format(my_square_2.area()))

    guillaume@ubuntu:~/$ python3 2-main.py

    Area: 9

    'Square' object has no attribute 'size'

    'Square' object has no attribute '__size'

    Area: 25

    guillaume@ubuntu:~/$ 

### 3. Access and update private attribute

Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size:

property def size(self): to retrieve it

property setter def size(self, value): to set it:

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0

Instantiation with optional size: def __init__(self, size=0):

Public instance method: def area(self): that returns the current square area

You are not allowed to import any module

Why?

   Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

    guillaume@ubuntu:~/$ cat 3-main.py

    #!/usr/bin/python3

    Square = __import__('3-square').Square

    my_square = Square(89)

    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3

    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
    
        my_square.size = "5 feet"
    
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    except Exception as e:
    
        print(e)

    guillaume@ubuntu:~/$ python3 3-main.py

    Area: 7921 for size: 89

    Area: 9 for size: 3

    size must be an integer

    guillaume@ubuntu:~/$  

### 4. Printing a square

Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:

property def size(self): to retrieve it

property setter def size(self, value): to set it:

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0

Instantiation with optional size: def __init__(self, size=0):

Public instance method: def area(self): that returns the current square area

Public instance method: def my_print(self): that prints in stdout the square with the character #:

if size is equal to 0, print an empty line

You are not allowed to import any module

    guillaume@ubuntu:~/$ cat 4-main.py

    #!/usr/bin/python3

    Square = __import__('4-square').Square

    my_square = Square(3)

    my_square.my_print()

    print("--")

    my_square.size = 10

    my_square.my_print()

    print("--")

    my_square.size = 0

    my_square.my_print()

    print("--")

    guillaume@ubuntu:~/$ python3 4-main.py

    ###

    ###

    ###

    --

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    --

    --

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

https://python.swaroopch.com/oop.html

https://python-course.eu/oop/object-oriented-programming.php

https://python-course.eu/oop/properties-vs-getters-and-setters.php

https://www.youtube.com/watch?v=1AGyBuVCTeE&

https://www.youtube.com/watch?v=apACNr7DC_s

https://www.youtube.com/watch?v=-DP1i2ZU9gk