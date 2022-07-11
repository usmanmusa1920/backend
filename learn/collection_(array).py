"""
  COLLOECTION (ARRAY) IN PYTHON
  Array are used to store multiple values in one single variabel, and the  variable can be a list, set, tuple, or dictionary. There are four collection data type in python programming language.
"""

"""
  LIST
  List is a collection which is ordered and changeable, it also allow duplicate of data: e.g
    students = ['Samir', 'Amir', 'Muhammad', 'John', 'Marry']
  To access item in a list, you are to use the index number of the item. And by default the index number start from zero (0). e.g
  
    samir = students[0]
    amir = students[1]
    
  To cahnge an item value in list, you are to use the index number of the item, and then assign it to what you want it to be. e.g
    students[2] = 'Ahmad'
  Now if we print our list, it will replace 'Muhammad' with 'Ahmad'
    print(studenst)
    #output: ['Samir', 'Amir', 'Ahmad', 'John', 'Marry']
    
  You can also make a list by:
    list(['Samir', 'Amir', 'Muhammad', 'John', 'Marry'])
"""

"""
  TUPLE
  Tuple is a collection which is ordered and unchangeable and it allow duplicate member. If you will have only one value in a tuple, make sure after that value you put comma else it will take it as a string, but if they are more than one that will be fine no need of comma at the end: e.g
  
    item = ('pencil')
    print(type(item))
    # output: <class 'str'>
    
    item = ('pencil',)
    print(type(item))
    # output: <class 'tuple'>
  
    staffs = ('teacher', 'security officer', 'principal', 'cleaner')
    print(type(staffs))
    # output: <class 'tuple'>
"""

"""
  SET
  Set is a collection which is used to store unordered, unchangeable and unindex also duplicate will be ignore (no duplicate member), you can loop over a set. Below is an example set of countries.
    countries = {"Iran", "Nigeria", "South Africa", "India", "Ghana", "Canada"}
"""

"""
  DICTIONARY
  Dictionary is a collection which is unordered, changeable and indexed. In python dictionaries are written in curly brackets, and they have keys and values. e.g
    book = {"Name":"Python book", "Level":"For beginners", "rank":1, "Is_available": True}
  If you want to access item in a dictionary, you are to access it by the key name of the item inside a square brackets. e.g
    rank = book["rank"]
    
  Also you can loop over a dictionary (with keys and values) by:
    for k, v in book.items():
      print(k, v)
      
  To loop over only the keys:
    for k in book.keys():
      print(k)
      
  To loop over only the values:
    for k in book.values():
      print(k)
"""
