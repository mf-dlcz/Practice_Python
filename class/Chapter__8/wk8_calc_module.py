'''
calc_module.py
contains a basic calculator module
that can be include in applications that
need calculator functions
'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
        
def divide(a, b):
    if b == 0:
        return None
    return a / b



# Test code
print("Testing calculator functions...")
print(f"2 + 2 = {add(2, 2)}")
print(f"4 - 1 = {subtract(4, 1)}")
print(f"3 * 3 = {multiply(3, 3)}")
print(f"10 / 5 = {divide(10, 5)}")