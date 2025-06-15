# Checking Passwords:
import Lab_password_details

def password_score(password):
    return Lab_password_details.get_strength(password)

pw = input('\nEnter password: ')

while password_score(pw) < 3:
    print('\nWeak password. Password score = ', password_score(pw))
    pw = input('Enter a better password: ')

if password_score(pw) > 4:
    print('\nStrong password! Score: ', password_score(pw))
else:
    print('\nAcceptable password. Score: ', password_score(pw))