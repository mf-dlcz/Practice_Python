# Practice exercises:

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

class SimpleCounter:
    """
    A simple counter class to demonstrate basic object-oriented programming
    and provide a target for unit testing.
    """
    def __init__(self, initial_count=0):
        """
        Initializes the counter with a given starting value.
        If no initial value is provided, it defaults to 0.
        """
        if not isinstance(initial_count, int) or initial_count < 0:
            raise ValueError("Initial count must be a non-negative integer.")
        self._count = initial_count # Using a protected attribute for the count

    def increment(self):
        """
        Increments the counter by 1.
        """
        self._count += 1

    def decrement(self):
        """
        Decrements the counter by 1.
        The counter cannot go below 0.
        """
        if self._count > 0:
            self._count -= 1
        else:
            # Optionally, you could raise an error here or just do nothing
            # For this beginner example, doing nothing is simpler.
            pass

    def reset(self):
        """
        Resets the counter to 0.
        """
        self._count = 0

    def get_count(self):
        """
        Returns the current value of the counter.
        """
        return self._count


################################################################################


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