"""
  GETTING STARTED WITH PYTHON
  To get started with python, since python is an interpreted programming language, that mean you can write python script in a file and then run that file into the python interpreter, OR you can simply run python code on it interpreter, which is very quick, easiest way, and the most recomended way for a beginners to start with.
  
  Instructions that python interpreter can execute are called statements. For example, a = 1 is an assignment statement. if statement, for statement, while statement etc. There are other kinds of statements which will be discussed later. One more thing to know about python is indentation, put in mind that indentation in python is required (it is a back bone if you will use conditional statement, creating a class, or define a function etc), if you mis-lead indentation in python definately you will get an error.
  
  PRINT
  Print is a built-in function in python which is used to print some text or our executed command on terminal. If you care to write some short amount of python code on terminal, you are to start python interpreter by typing "python" and then hit enter. That will take you to python interpreter by showing you the version you are using and some other information, and each line it will prefix with a triple greater sign ">>>" showing you python is ready for your command. Try typing the below code snippet on the first line of python interpreter.
"""
print("Hellow, World")
# output:
# Hellow,  World

"""
  To get out of python interpreter, you are to just call the built-in python exit function, which will automatically get you away from python interpreter to your system terminal, and to do that you are to just type "exit()"
"""

"""
  To run the above python command in a file, is as simple as to create a file first by:
"""
# touch hello_world.py

"""
  The above line is a way to create file in linux and unix like operating system on the terminal, if you don't get it, don't worry just do as we do. After the creation of the file, so we can now write some code in the file, we can do so using any text editor whether vscode, sublime, nano or any other text editor of your choice. Once you open the file in a text editor, paste the below pieces of code into it.
"""
print("Hello world")


"""
  After you paste the above line of code, so you have to run that file. To run a python file on terminal, you are to type "python <file_name>". For example, to run our python file we are to type the below command on our terminal or command prompt and make sure you navigate to the directory you put that file.
"""
# python hello_world.py
# output: Hello world

"""
  VARIABLE
  Now let us move forther to variable, since we know how to print something on terminal. Variable is a container for storing a data values, thank to dynamic type of python which make us not to declare the type of data that we want to store, unlike other programming language like C, C++ of which you have to declare the data type that you want to store. And in python there is two possible way that you can make a string, whether in single qoute ('Hello world') or in double qoute ("Hello world") which are all identical. Now let begin by making two variables:
"""
x = 7
y = 3
print(x + y)
# output: 10

a = "Cat"
b = "Dog"
print(a + " " + b)
# output: Cat Dog

"""
  The above declaration of x and y which are numbers, by convention python knows you want to add, whenever you concatenate two or more numbers which are not in qoute, in the other hand a and b which are string of alphabet quoted in double qoute, in here python knows you are trying to concatenate two string variables, notice in between the a and b in the print function there is a string which contains a space in other to separate the two variables.
"""

"""
  COMMENT
  Comment are use to prevent execution of code when running the program, Comment can be use to explain and make detail about a pieces line of code. There are two type of comment in python (single line comment and multi-line comment).
  
  Single line comment is used if you want to ignore a single line in your python script e.g:
    print("I am not a comment, that is why you see me")
    # print("I am comment you can not see me on terminal")
  
  Multi-line comment are used if you want to ignore multiple-line of code in your script, or if you want to add a doc string at the top of a python object, e.g:
    print("There is multi-line comment below me! you can not see it on terminal")
    '''
      I am line one of the multi-line comment
      I am line two of the multi-line comment
      I am line three of the multi-line comment
      I am line four of the multi-line comment
    '''
    # output: There is multi-line comment below me! you can not see it on terminal
"""


"""
  PYTHON KEYWORDS
  Keywords are the reserved words in python, we cannot use a keyword as variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language. In python, keywords are case sensitive. There are 33 keywords in Python 3.3. This number can vary slightly in course of time. All the keywords except True, False and None are in lowercase and they must be written as it is. The list of keywords are:
    '''
      False, Class, finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while, and, del, global, not, with, as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise
    '''
"""


"""

  DATA TYPE IN PYTHON
  Data type is an important concept in programming, variable can store data of different type, also different type do different things. Python has the following data type:
    For text: str
    For number: int, float, complex
    For sequence: list, tuple, range
    For boolean: bool
    For mapping: dictionary
    For binary: bytes, bytarray, memoryview
    
  If you are curious about what data type is a variable is, you can detect it by 'print(type(<variable_name>))', note that 'type' also is a built-in function in python e.g
"""
  
a = 8
b = "8"
c = 8.0

print(type(a))
# output: <class 'int'>
print(type(b))
# output: <class 'str'>
print(type(c))
# output: <class 'float'>

"""
  To break down the aboove code. The variable "a" which hold a data type of integer, and integer are number(s) which has no decimal. The variable "b" which hold a data type of string because it is in double qoute, it behave just like an alphabet. The variable "c" which hold a data type of float, and float is a number which is in decimal place, even if the decimal place is zero. By most people (beginners) they will take them all as one which is not true in python.
"""
