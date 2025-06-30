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
        
    def divide(self, value):
        # if value == 0: 
        #     raise ZeroDivisionError
        self.result /= value

    def get_result(self):
        return self.result
        
# test case class
class TestMathOperations(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.result = 1138
    
    
    # test the functions ("global")
    def test_multiply(self):
        # print('multiply')
        self.assertEqual(multiply(6, 7), 42)
    
    def test_add(self):
        # print('add')
        result = add(2, 3)
        self.assertEqual(result, 5)
        self.assertNotEqual(result, 4)
        
    def test_divide(self):
        # print('divide')
        result = divide (2, 3)
        # print(result)
        self.assertAlmostEqual(result, .66666, places = 4)
        
        
    # Tests the calculator class
    def test_Calculator_substract(self):
        print('subtract')
        
    def test_Calculator_add(self):
        # print('add')
        # print(self.calc.get_result())
        # self.calc.result = 42
        # print(self.calc.get_result())
        self.calc.add(12)
        self.assertEqual(self.calc.result, 1150)
        
    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0)
        
        
if __name__ == '__main__':
    unittest.main()