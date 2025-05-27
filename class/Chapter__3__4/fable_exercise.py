# April 24

fable = '''
The Ant and the Grasshopper: In a field one summer's day, 
a grasshopper was hopping about, chirping and singing to 
its heart's content. An ant passed by, grunting as it 
struggled to roll a huge kernel of corn it had stored for 
the winter. "Why not come and chat with me," said the 
grasshopper, "instead of toiling and struggling like that 
in the heat?" "I am helping to store up food for the winter," 
said the ant, "and I recommend you do the same." The 
grasshopper laughed and sang till the cold weather came. 
When the biting frost had stripped the trees of their leaves, 
the grasshopper had no food and found itself dying of hunger, 
while the ant lived warmly and cozily through the winter on the 
food it had worked so hard to gather and store.
'''

# CLEAN THE TEXT
# to clean the text we need to:
# 1. replace all newlines with a space
# 2. remove whitespace from the beginning and end of the document
# 3. remove all punctuation
punctuation = ''':;"',.?!'''
# 4. force all words to lowercase to make counting easier
# 5. convert the document to a list of words


# COUNT THE WORDS
# 1. Create a dictionary to store the count
# 2. Iterate through the list of words for each word:
# 2a. if the word is in the list, add one to its value
# 2b. if the word is not in the list, add the word to the list with value 1



# PRINT THE CHART
#   for each word in the dictionary
#     get the count of words from the word count collection
#     print the word 
#     print a number of symbols equal to the word count for the word