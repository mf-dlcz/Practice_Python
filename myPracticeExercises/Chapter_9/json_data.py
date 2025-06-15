#           WORKING WITH JSON

'''
#*  PYTHON:             JSON:
    dic:                object

    list
    tuple:              array

    str:                string

    int
    float:              number

    True                true

    False               false

    None                null
'''

###########################################################                 json.loads() & json.dumps()

'''
*******    These methods convert JSON data to and from Python objects.  *******

json.dump()    encodes a Python object as JSON and writes it to a file.

json.dumps()    encodes a Python object as a JSON-formatted string.

json.load()     decodes JSON data from a file and returns a Python object.

json.loads()    decodes a JSON-formatted string into a Python object.
'''

##########################################################                  CONVERTING FROM JSON TO PYTHON:

# import the JSON module
import json

# define a JSON-formatted string
x = '{"name": "John", "lastname": "Stiles", "city": "Vancouver"}'

# convert the json string into a Python object
y = json.loads(x)

# print the value of 'city'
print(y['city'])