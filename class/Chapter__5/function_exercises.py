# def <function_name>(<parameters>):
def add(x, y):
    return x + y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    return x / y

def compute(equation):
    data = equation.split()
    print(data)
    operation, x, y = data
    x = int(x)
    y = int(y)
    if operation == 'add':
        return add(x,y)
    elif operation == 'mult':
        return multiply(x,y)
    elif operation == 'div':
        return divide(x,y)
    

eq1 = 'add 2 3'
eq2 = 'div 15 5'
eq3 = 'mult 2 3'

a = compute(eq1)
b = compute(eq3)
c = compute(eq2)

print(a, b, c)
print(add(a, b))

# add(num1, num2)
# multiply(num1, num2)









# num1 = 5
# num2 = 6
# # answer = x + y
# # print(answer)
# add(num1, num2)

# num1 = 12
# num2 = 14
# # answer = x + y
# # print(answer)
# add(num1, num2)


# be VERY careful not to name your functions after built-in functions
# values = [1, 4, 3, 5, 6, 9]
# print(sum(values))