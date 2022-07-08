"""
  PYTHON PROGRAMMING LANGUAGE
  Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido Van Rossum around 1985 - 1990, python it uses english keywords frequently where as other languages use punctuation, and it has a good and easy way to understand due to it syntactical contructions.
  
  With python one can do many things in many field such as web development, data science, back-end, system administration, automation and much-much-more.
  
  Python is case-sensitive, it works on different platforms such as linux, unix, windows, etc. To download and start using python, you can go to python official website @ "https://www.python.org/" to download it. Once the installation finish, to verify go to command prompt (windows) or terminal (linux/unix) and type "python --version" if the installation is successfull it will show you the version depending on which version you install.
"""


def welcome(name):
    author = "Usman Musa"
    message = "welcome to python series for"
    print("Nice to see you {}, in this series".format(name.split(" ")[0]))
    return "{0} {1} {2}".format(name, message, author)
  
print(welcome("Muhammad Ali"))
