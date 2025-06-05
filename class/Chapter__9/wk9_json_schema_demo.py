import jsonschema, json

# Define a JSON schema.
schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname" : {"type": "string"},
        "age": {"type": "integer"},
        "state": {"type": "string"}
    },
    "required": ["firstname", "lastname", "age", "state"]
}

#JSON document
document = {"firstname" : "ABC",
            "lastname" : "XYZ",
            "age" : "12",
            "hobbies" : "Reading",
            "state":"Wisconsin"
            }

try:
    jsonschema.validate(document, schema)
except jsonschema.exceptions.ValidationError as x:
    print(x)
                       