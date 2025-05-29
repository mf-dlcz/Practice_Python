def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
if __name__=="__main__":
    #This code only runs when the calculator.py file is run directly
    print("Running calculator.py file directly")
    print("Testing the functions.....")
    print(f"Addition: {add(5, 3)}")
    print(f"Subtraction: {subtract(18, 10)}")
else:
    print("The calculator module has been imported")
    