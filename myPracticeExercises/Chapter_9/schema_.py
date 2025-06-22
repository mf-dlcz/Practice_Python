# JSON document
import jsonschema
import json

# Defining a schema
schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname" : {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["firstname", "lastname", "age"]
}

# Dictionary
document = {
    'firstname': 'María',
    'lastname': 'Fish',
    'age': 99,
    'hobbies': 'reading'
}

# validating the schema
try:
    jsonschema.validate(document, schema)
except jsonschema.exceptions.ValidationError as x:
    print(x)