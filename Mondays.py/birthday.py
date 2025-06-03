day = 15
month = 'September'
year = 1978
name = 'Terry Whitlock'


def print_full_birthday(d, m, y):
    print(f'{name} was born on {m} {d}, {y}')

def print_birthday(d, m):
    print(f"{name}'s birthday is on {m} {d}")

if __name__ == '__main__':
    # this will run only when the file runs by itself directly
    bday = print_full_birthday(day, month, year)
    print(bday)
else:
    # this code will run when the file is imported as a module
    bday = print_birthday(day, month)