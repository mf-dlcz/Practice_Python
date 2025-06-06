import json
from pprint import pprint

# Loading settings from the file
with open('user_settings.json', 'r') as file:
    loaded_settings = json.load(file)

pprint(loaded_settings)
# Use the loaded settings
#print(f"User theme preference: {loaded_settings['theme']}")
