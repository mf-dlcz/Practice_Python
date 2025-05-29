'''
Create the module file. Define functions to check if the 
user included:
- special characters, 
- uppercase letters, 
- lowercase letters, and 
- numbers. 
Each check should add a point to the overall strength score 
if the check is successful.
'''
import string as string_library

def get_strength(password):
    score = 0
    
    if contains_upper(password):
        score = score + 1
        
    if contains_lower(password):
        score = score + 1
        
    if contains_numbers(password):
        score = score + 1
        
    if contains_special(password):
        score = score + 1
        
    if len(password) >= 8:
        score = score + 1
    
    return score
    
def contains_upper(string):
    for letter in string:
        if letter.isupper():
            return True
    return False
    
def contains_lower(string):
    for letter in string:
        if letter.islower():
            return True
    return False


def contains_numbers(string):
    for character in string:
        if character.isnumeric():
            return True
    return False
    
def contains_special(string):
    # specials = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    for character in string:
        if character in string_library.punctuation:
            return True
    return False


if __name__ == '__main__':
    pw1 = 'password'
    pw2 = 'Password'
    pw3 = 'Password123'
    pw4 = 'Password!'
    pw5 = '1Password!'
    
    print(pw1, get_strength(pw1))
    print(pw2, get_strength(pw2))
    print(pw3, get_strength(pw3))
    print(pw4, get_strength(pw4))
    print(pw5, get_strength(pw5))
