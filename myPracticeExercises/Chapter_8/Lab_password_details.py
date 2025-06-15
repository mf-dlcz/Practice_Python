'''
Create the module file. Define functions to check if the user included 
✔ special characters, 
✔ uppercase letters, 
✔ lowercase letters, and 
✔ numbers. 
Each check should add a point to the overall strength score if the 
check is successful.
'''

def get_strength(password):
    score = 0
    if contains_uppercase_letter(password):
        score = score + 2

    if contains_lowercase_letter(password):
        score = score + 1

    if contains_nums(password):
        score = score + 3

    if contains_special_char(password):
        score = score + 4

    if len(password) >= 12:
        score = score + 5

    return score

# Checks if my password contains an uppercase letter
def contains_uppercase_letter(str):
    for letter in str:
        if letter.isupper():
            return True
    return False

# Checks if my password contains a lowercase letter
def contains_lowercase_letter(str):
    for letter in str:
        if letter.islower():
            return True
    return False

# Checks if my password contains a number
def contains_nums(str):
    for char in str:
        if char.isnumeric():
            return True
    return False

# Checks if my password contains a special char
def contains_special_char(str):
    specials = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''
    for special_char in str:
        if special_char in specials:
            return True
    return False



#           TESTS:
pw1 = 'passworddddd'
pw2 = 'PasswordDDDD'
pw3 = 'Password1234'
pw4 = 'Password1_2^3'

print(pw1, 'Points: ', get_strength(pw1))
print(pw2, 'Points: ', get_strength(pw2))
print(pw3, 'Points: ', get_strength(pw3))
print(pw4, 'Points: ', get_strength(pw4))