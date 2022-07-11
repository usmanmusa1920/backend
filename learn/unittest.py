import unittest

def add(x, y):
  return x + y
  
def subt(x, y):
  return x - y
  
def mul(x, y):
  return x * y
  
def div(x, y):
  return x / y

"""
    Naming convension of a test module  is required, it has to start with 'test' e.g 'test_users.py' (concatenating it with the file name you want to test)
    
    NB: test don't actually run in order, keep each test isolated from other
    
    To run a test file which has no namespace (if __name__ == '__main__'), you are to run it making unittest as the main module by:
      python-m unittest <test_file.py>
      
    But if you apply the below code at the very bottom of your test file, you can run it just like the way you run every python file on the terminal:
      if __name__ == '__main__':
        unittest.main()

"""

class TestAdd(unittest.TestCase):
  
  # setUpClass method run it code before the test start, and the method is in camel-case.
  @classmethod
  def setUpClass(cls):
    print("Starting testing... (setUpClass)")
    
  # teaarDownClass method run it code afte every single test, and the method is in camel-case.
  @classmethod
  def tearDownClass(cls):
    print("End of test (tearDownClass)")
  
  # setUp method run it code before every single test, we use this if there are repeated code fore every test in other to make our code DRY (Don't repeat yourself), and the method is in camel-case.
  def setUp(self):
    print("Starting a test... (setUp)")
  
  # teaarDown method run it code afte every single test, we use this if there are repeated code fore every test in other to make our code DRY (Don't repeat yourself), and the method is in camel-case.
  def tearDown(self):
    print("Ending a test... (tearDown)")
  
  def test_add(self):
    self.assertEqual(add(4, 6), 10)
    self.assertEqual(add(4, 6), 10)
    self.assertEqual(add(4, 6), 10)
    
  def test_subt(self):
    self.assertEqual(subt(6, 4), 2)
    self.assertEqual(subt(6, 3), 3)
    self.assertEqual(subt(9, 8), 1)
    
  def test_mul(self):
    self.assertEqual(mul(4, 6), 24)
    self.assertEqual(mul(4, 6), 24)
    self.assertEqual(mul(4, 6), 24)
    
  def test_div(self):
    self.assertEqual(div(80, 2), 40)
    self.assertEqual(div(9, 3), 3)
    self.assertEqual(div(10, 2), 5)
    
if __name__ == '__main__':
  unittest.main()
