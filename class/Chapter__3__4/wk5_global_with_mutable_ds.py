
people = {
    'accounting' : 'John Smith',
    'sales' : 'Mabel Martha',
    'ceo' : 'Alice Bradley'
}

places = ['New York', 'Austin', 'Miami', 'Los Angeles']

def a_function():
    print('\n-----Inside function....')
    print('-people')
    print(people)
    # we can't replace the value in a global variable (without declaring it global)
    # people = { 'department' : 'nobody'}
    people['development_lead'] = 'Jason C'
    print(people)
    
    print('-places')
    print(places)
    # we can't replace the value in a global variable (without declaring it global)
    # places = ['College Station']
    places.append('College Station')
    print(places)
    
print('-----Before function ....')
# print(people)
# print()
# print(places)

a_function()

print('\n-----After function ....')
print(people)
print()
print(places)