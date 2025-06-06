import requests, json
from pprint import pprint

#API endpoint for astronauts currently in space
url = "http://api.open-notify.org/astros.json"

#Send GET request to the API
response = requests.get(url)
# print(response)

#Not reading information to a file, reading a string response, use loads() 
if response.status_code == 200:
    #response received is a JSON string
    #print(type(response.text))
    
    #parse JSON string into a dictionary
    data = json.loads(response.text)
    
    # print(type(data))
    # pprint(data)
    
    #extract number of people in space
    print(f"There are {data['number']} people in space currently.")
    
    #print the names and spacecraft of each astronaut
    for each_person in data['people']:
        print(f" {each_person['name']} on {each_person['craft']}")
        
else:
    print(f"Failed to fetch information, status code: {response.status_code}")
    
#to dump json data to a file, use json.dump()
with open("astronauts.txt", "w") as file_write:
    json.dump(response.text, file_write)
    
# json.load() method is used to load the json data from a file
with open("astronauts.txt", "r") as f:
    data = json.load(f)

pprint(data)
