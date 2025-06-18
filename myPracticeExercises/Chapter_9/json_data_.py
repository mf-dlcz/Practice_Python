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
'''

#####################################################                    Attribute Dictionary(namespace dictionary)

'''
                    __dict__
.   is the attribute or namespace dictionary of an object. 
.   It is a special dictionary that contains all the writable attributes of an object, including
    methods and properties.
.   The keys in the dictionary are the attribute names(as strings), and the values are the
    corresponding attribute values.
.   Contains all the attributes defined for that particular instance.
'''


'''
Serialization:  is the process of converting an object into a format that can be easily stored or 
                transmitted, such as a JSON string. This allows the object's data to be saved to a 
                file, sent over a network, or used in other applications. Deserialization is the 
                reverse process, where the stored or transmitted data is converted back into an object. 

Direct Serialization:   json.dumps() can directly serialize dictionaries, lists, and other basic 
                        data types, but NOT custom objects.

Custom Serialization:   To serialize custom objects, you can either convert the object to a dictionary 
                        manually or implement a custom serializer method.

Deserialization:    is the reverse process, where the stored or transmitted data is converted back into an object.
'''

###################################################                     LOOPING OVER DICTIONARIES & JSON

'''
# import the JSON module
import json

# define JSON string
x = '{"name": "John", "lasname": "Stiles", "city": "NY"}'

# parse JSON data into Python dictionary
json_to_python = json.loads(x)

# loop through the Python dictionary
for key, value in json_to_python.items():
    print(key, ':', value)
'''
