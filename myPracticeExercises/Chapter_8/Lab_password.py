# Checking Passwords:

def password_score(password):
    if password == 'password':
        return 5
    return 0

pw = input('Enter password: ')
while password_score(pw) < 3:
    print('Weak password. Password score = ', password_score(pw))
if password_score(pw) > 4:
    print('Strong password! Score: ', password_score(pw))
else:
    print('Acceptable password. Score: ', password_score(pw))