''' Develop a flashcard type game where:
Based on the number a user enters, user will get a question 
User has 3 attempts to guess the answer to that question.'''

#create a ditionary with fun questions as keys and answers as values
q_and_a = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal?": "Blue Whale",
    "What is the name of Harry Potter's owl?":"Hedwig",
    "How many sides does a hexagon have?" : "6",
    "In which country was the game of chess invented?" : "India"
}

q = {}
a = {}

# print(q_and_a['What is the capital of France?'])
# a[1] = "Paris"
# a[2] = "Mars"
# print(a)

#dictionary[key] = value adds new key:value pair to a dictionary
#manually adding key and value
# q[1] = 'What is the capital of France?'
# q[2] = 'Which planet is known as the Red Planet?'

for index, question in enumerate(q_and_a):
    # print(index+1, question)
    q[index+1] = question
    
for index, question in enumerate(q_and_a):
    # print(index+1, q_and_a[question])
    a[index+1] = q_and_a[question]

# print(q)
# print(a)

user_name = input("Enter your name: ")
print(f"Welcome to the game, {user_name}!")

user_choice = int(input("Enter a number 1 through 6: "))
print("Great! Here is your trivia question: ", end = ' >>>>> ')
print(q[user_choice])

#as long as the number of attempts < 3, user will get to try

num_attempts = 0
while num_attempts < 3:
    user_answer = input("Enter your answer here : ")
    num_attempts = num_attempts + 1
    
    if user_answer.lower() == a[user_choice].lower():
        print("Bingo! Right answer!")
        break
    else:
        print("Wrong answer!")
        
    if num_attempts == 3:
        print("Game over!")
    
