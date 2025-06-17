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

'''
# import the JSON module
import json

# define a JSON-formatted string
x = '{"name": "John", "lastname": "Stiles", "city": "Vancouver"}'

# convert the json string into a Python object
y = json.loads(x)

# print the value of 'city'
print(type(y['city']))              # When I add the type I received a str
print(type(y))                      # Python Object as a dictionary
print(type(x))                      # receive a str
'''

#########################################################                  USING json.load()

'''
#* THIS DATA WAS MOVED TO mydata.json
{
    "movie": "starwars",
    "genre": "science fiction"
}

import json

# Open the JSON file
f = open('mydata.json, 'r')

# Convert the JSON data into Python.
mydata = json.load(f)

# Close file
f.close()

# mydata contains a Python object representing the JSON file data
print(mydata)

# type = 'dictionary'
print(type(mydata))
'''

########################################################                CONVERTING FROM PYTHON TO JSON

'''
The following types can be converted into JSON

. dict          . list           . tuple            . string
. int           . float          . True             . False
. None
'''

import json

# Define a dictionary with three key-value pairs.
x = {
    "dog": "Jack",
    "breed": "Golden Retriever",
    "city": "Albuquerque"
}

# Convert dictionary into a JSON string using json.dumps().
y = json.dumps(x)

# Print output.         #* type = str
print(y)

