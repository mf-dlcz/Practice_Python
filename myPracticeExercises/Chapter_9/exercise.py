# Additional exerices to practice opening, reading, adding, and closing a txt file

message_in_a_bottle = '''
Day 160
Purpose is not a single act, it is a way of moving through the world that ensures
everything you touch is infused with a little more love than it was before. It is a way
of being that gives you softer eyes, the ability to see a little more potential, a little
more hope, a little more possibility that the rest. It is not any one thing you do, but
a way you become. A person you choose to be.
'''


# creates a file called data.txt (If it doesn't exist)
# & it'll write to the file
reading_file = open('', 'w')

# writing data to a file
reading_file.write(message_in_a_bottle)

# close file after writing to it
reading_file.close()

# open the file to read it
reading_file = open('', 'r')

# printing in the console all the content of the file
print(reading_file.read())

# close the file
reading_file.close()