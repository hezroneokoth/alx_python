# Python - Web framework

## Python

## Learning Objectives

### General

1. What is a Web Framework
2. How to build a web framework with Flask
3. How to define routes in Flask
4. What is a route
5. How to handle variables in a route
6. What is a template
7. How to create a HTML response in Flask by using a template
8. How to create a dynamic template (loops, conditions…)
9. How to display in HTML data from a MySQL database

## Requirements

### Python Scripts

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

### HTML/CSS Files

1. Recommended editors: Visual studio code
2. All your files should end with a new line
3. A README.md file at the root of the folder of the project is mandatory
4. Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
5. All your CSS files should be in the styles folder
6. All your images should be in the images folder
7. You are not allowed to use !important or id (#... in the CSS file)
8. All tags must be in uppercase
9. Current screenshots have been done on Chrome 56.0.2924.87.
10. No cross browsers

## Tasks

### 0. Hello Flask!

Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000

Routes:

/: display “Hello HBNB!”

You must use the option strict_slashes=False in your route definition

    guillaume@ubuntu:~/AirBnB_v2$ python3 0-hello_route.py

    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

    ....

In another tab:

    guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e

    Hello HBNB!$

    guillaume@ubuntu:~$ 

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
