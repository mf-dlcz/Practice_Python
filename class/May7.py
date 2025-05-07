# Function Definitions:

def feed_animals():
    food = "bananas"
    print(f"Feeding animals {food} at {zoo_name}")

def rename_zoo():
    global zoo_name
    zoo_name = "AWS Cloud Institute Zoo"
    print("Inside the function!")
    print("Almost done!")
   
#global variable
zoo_name = input("Enter a name for the Zoo: ")

print(f"Welcome to {zoo_name}!")
feed_animals()
rename_zoo() 
print("The zoo has been renamed to: ", zoo_name)

print("End of zoo exercise!")