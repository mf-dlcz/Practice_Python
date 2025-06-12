try:
    age = int(input("Please enter your age:"))
except Exception as e:
    print(f"Exception caught: {e}")
else:
    print("No exception was raised...Continuing with program execution as normal")
    if age >10 and age <18:
        print("You are not an adult yet.")
    elif age >= 18:
        print("You are an adult.")
finally:
    print("This is the end of the program.")