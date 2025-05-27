'''
Get user input for numbers continuously until 'quit'
Compute the average of these numbers.
Find the maximum and minimum numbers entered.
'''

min_val = None
max_val = 0
total_sum = 0
count = 0
average = 0
user_input = None

while user_input !='quit':
    user_input = input("Enter a number:")
    
    #validation
    if user_input.isnumeric():
        user_input = int(user_input)
        count = count + 1
        total_sum = total_sum + user_input
        
        #make sure to update the min val to be an integer for comparison in next iteration of while loop
        if count==1:
            min_val = user_input
        
        if min_val > user_input:
            min_val = user_input
        
        if max_val < user_input:
            max_val = user_input
        
average = total_sum/count
print(total_sum, count, average)
print(min_val, max_val)
