AirBnB clone Team Project

![AirBnB](image/hbnblogo.png)

## DESCRIPTION   
**AirBnB** is a complete web application, integrating database storage, a back-end API, and front-end interface. The purpose of this project is to make a command interpreter that manages our AirBnb objects.

#### Data Diagram

![data_diagram](image/data_diagram.jpg)

## Learning Objectives

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function



## Enviroment( Style guidelines )
 - pycodestyle (version 2.7.*)
 - PEP8

# Installation

git clone https://github.com/Lique007/AirBnB_clone.git 

change to the AirBnb directory and run the command : ./console.py 

## Starting the Commandline Interpreter
The Commandline Interpreter can be started by executing the command ./console.py. The console can create, destroy, and update objects. Type help within the console to get a list of command options and its function.

# In interactive mode
**Example:**                                                                                                             
``` bash                                                                                                                 
root@404593d78d60:~$ ./console.py                                                                                        
(hbnb) help                                                                                                              
Documented commands (type help <topic>):                                                                                                           ========================================                                                                                                         EOF  create  help  quit
Undocumented commands:                                                                                                   
======================                                                                                                   
all  destroy  show  update                                                                                               
(hbnb) help quit       

# Non Interactive mode
** Example **

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

## Testing 

- All tests are defined in the tests folder
# Documentation
- Modules :
 
 python3 -c 'print(__import__("my_module").__doc__)'

- Classes : 

 python3 -c 'print(__import__("my_module").MyClass.__doc__)' 

- Functions(inside and outside a class):

python3 -c 'print(__import__("my_module").my_function.__doc__)'

and 

python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'


## Python Unit Tests 
- unittest module
- File extension .py
- Files and folders star with test_
- Organization: for models/base.py , unit tests in: tests/tests_models/test_base.py
- Execution command: python3 -m unittest discover tests
- or: python3 -m unittest tests/tests_models/test_base.py
