'''
calc_demo.py
Example to demonstrate loading a module for reuse
'''
import wk8_calc_module as calc


def resolve(equation):
    op, num1, num2 = equation.split()
    num1 = int(num1)
    num2 = int(num2)
    if op == 'add':
        return calc.add(num1, num2)
    elif op == 'subtract':
        return calc.subtract(num1, num2)
    elif op == 'multiply':
        return calc.multiply(num1, num2)
    elif op == 'divide':
        return calc.divide(num1, num2)
    else:
        print("Unsupported operation")
        return None
        

equations = [
    'add 6 4',
    'divide 3 2',
    'multiply 7 3'
]

for equation in equations:
    result = resolve(equation)
    print(f'"{equation}" resolves to {result}')