import json

# Read JSON data from a file
with open('src/myPracticeExercises/Chapter_9/about_me.json', 'r') as f:
    about_me = json.load(f)

# Loop through dictionary and print key_value pairs.
for key, value in about_me.items():
    print(f"{key}: {value}")

# Loop through hobbies list and print each one
for hobby in about_me['hobby']:
    print(hobby)