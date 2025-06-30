import unittest

def is_even(number):
    """
    Checks if a given number is even.
    """
    return number % 2 == 0

def get_full_name(first_name: str, last_name: str):
    """
    Combines first and last names into a full name.
    """
    return f"{first_name} {last_name}"

def calculate_area_rectangle(length, width):
    """
    Calculates the area of a rectangle.
    """
    return length * width

# Tests the functions above
class Test_functions(unittest.TestCase):

    def test_is_even(self):
        result = is_even(4)
        self.assertEqual(result, True)
        self.assertNotEqual(result, False)

    def test_get_full_name(self):
        result = get_full_name('Maria', 'Black')
        self.assertEqual(result, 'Maria Black')

    def test_calculate_area_rectangle(self):
        result = calculate_area_rectangle(2, 2)
        self.assertEqual(result, 4)
        self.assertNotEqual(result, 5)

# print(get_full_name(Maria, Doe))

if __name__ == '__main__':
    unittest.main()