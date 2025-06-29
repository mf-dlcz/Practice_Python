#                       Working With Tests:

#           EXAMPLE:

'''
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)

if __name__ == '__main__':
    unittest.main()
'''

####################################################

#               Writing Unit Tests:
'''
The first test method tests that the function correctly adds two positive numbers,
the second tests that it correctly adds two negative numbers.
'''


'''
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)

    def test_adding_negative_ints(self):
        self.assertEqual(add(-15, -10), -25)

if __name__ == '__main__':
    unittest.main()
'''

#################################################

#               Test Fixtures:

'''
setUp()     - It's called before every individual test method within
            a test case.
            - Helps avoid duplicate code in each individual test method.

setUpClass()    - Call it once before any test method within the class is run.
                - It's purpose is to configure any shared resources or state
                required by multiple test methods in the class.
                - It's useful when you need to run expensive setup operations
                that can be reused by multiple tests.

tearDown()
tearDownClass()     - Used for the cleanup phase of unit testing.
                    - Cleans up any resources that you set up while running a test.
'''

###############################################

#           EXAMPLE:

'''
import unittest

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 100
        self.y = 50
    def tearDown(self):
        self.x = None
        self.y = None
    def test_addition(self):
        result = self.x + self.y
        self.assertEqual(result, 150)
    def test_subtraction(self):
        result = self.x - self.y
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
'''

###############################################

'''
Method:                             Description:

assertEqual(x, y)                   Verify that x == y

assertNotEqual(x, y)                Verify that x != y

assertTrue(x)                       Verify that x is True

assertFalse(x)                      Verify that x is False
'''

#################################################

#           

    