# Python - Object-relational mapping

## Python

## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code.

Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database

    query_rows = cur.fetchall()

    for row in query_rows:
    
        print(row)

    cur.close()

    conn.close()

With an ORM:

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)

    Base.metadata.create_all(engine)


    session = Session(engine)

    for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    
        print("{}: {}".format(state.id, state.name))

    session.close()

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Learning Objectives

### General

1. Why Python programming is awesome
2. How to connect to a MySQL database from a Python script
3. How to SELECT rows in a MySQL table from a Python script
4. How to INSERT rows in a MySQL table from a Python script
5. What ORM means
6. How to map a Python Class to a MySQL table

## Requirements

1. Recommended editors: Visual studio code
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. Your files will be executed with MySQLdb version 1.3.x
4. Your files will be executed with SQLAlchemy version 1.2.x
5. All your files should end with a new line
6. A README.md file, at the root of the folder of the project, is mandatory
7. Your code should use the PEP 8 style (version 1.7*)
8. The length of your files will be tested using wc
9. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
10. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
11. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
12. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
13. You are not allowed to use execute with sqlalchemy

## Tasks

### 0. Get all states

Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported

    guillaume@ubuntu:~/$ cat 0-select_states.sql

    -- Create states table in hbtn_0e_0_usa with some data

    CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

    USE hbtn_0e_0_usa;

    CREATE TABLE IF NOT EXISTS states ( 
    
        id INT NOT NULL AUTO_INCREMENT, 
    
        name VARCHAR(256) NOT NULL,
    
        PRIMARY KEY (id)

    );

    INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

    guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p

    Enter password: 

    guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa

    (1, 'California')

    (2, 'Arizona')

    (3, 'Texas')

    (4, 'New York')

    (5, 'Nevada')

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