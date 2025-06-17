import unittest

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value

    def subtract(self, value):
        self.result -= value

    def get_result(self):
        return self.result
        
# test case class
class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
        self.assertNotEqual(result, 4)
        
    def test_divide(self):
        result = divide (2, 3)
        # print(result)
        self.assertAlmostEqual(result, .66666, places = 4)

    def test_multiply(self):
        result = multiply(5, 2)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
        
if __name__ == '__main__':
    unittest.main()