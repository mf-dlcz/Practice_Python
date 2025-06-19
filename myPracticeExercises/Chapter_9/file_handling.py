#       Exploring File handling:

'''
-   The open() function is used to open files. The file object allows you to perform
    operations on the file.
-   The open() function takes two arguments: 
        1. the name of the file you want to open
        2. the mode in which you want to open it
    NOTE: modes can be combined by passing multiple characters. 
            EXAMPLE:
                    'rb' -> 'read binary' mode
                    'wb' -> 'write binary' mode
                    'rt' -> 'read text' mode #* are default values and therefore aren't needed but
                                            #*  They will make your code more explicit for others.

                    MODES:
    METHOD:                 Description:
    Read 'r'                Default value. Use this method for reading the contents of an existing file.
                            If the file doesn't exist, you will receive an error.

    Append 'a'              Use this method to add data to an existing file. If the file doesn't exist,
                            a new file will be created.

    Write 'w'               Use this method to write data into a file. If the file exists it will be overwritten.
                            If the file doesn't exist a new file will be created.

    Create 'x'              Use this method to create a new file. If the file already exists, you will receive an
                            error.

#*  By default, Python uses 't' (text mode) for text-based file handling. You can use 'b' 
#* (binary mode) for handling binary files, such as images.
'''

########################################################################           CREATING & WRITING FILES:

'''
# Create a file and write a welcome message to it.
f = open('welcome.txt', 'w')
f.write('Hello! This is my first time writing on a file. Yay!')

# Open the file and reads its contents.
f = open('welcome.txt', 'r')
print(f.read())

# Closes the file
f.close()
'''

#####################################################################
#*          CHALLENGE: Add data to an existing file:

'''
Use the append mode to modify the welcome.txt file you just created. Add the text "Adding: Thank you." 
to it. Next, print the file contents to confirm the appended text is available.
'''

'''
# Opening the txt file and adding to it
f = open('welcome.txt', 'a')
# Add a line of text to the existing file
f.write('\nAdding: Thank you')
# Closing the file
f.close()


# Opening the file and reading from the file
f = open('welcome.txt', 'r')
print(f.read())
'''

##############################################################                  OPENING & READING FILES:
'''
-   If file lives in a different file path that must be included and passed to
    the open() function.

            EXAMPLE:
    f = open('D:\\appfiles\welcome.txt', 'r')

-   The read() method reads the entire content of the file you if don't specify
    with a size argument (reads a specific number of bytes from the file).

            EXAMPLE:
    # For most text files, 5 bytes is equivalent to the first five chars.
    print(f.read(5))
'''

###########################################################                     DELETING FILES:

'''
-   To delete a file the OS module must be imported.
# * REMOVES the file permanently - cannot be recovered!!

            EXAMPLE:
#*  import os
    os.remove('welcome.txt')

-   To check if the file exists before deleting use the os.path.exists() method.

            EXAMPLE:
    import os
    if os.path.exists('welcome.txt')
        os.remove('welcome.txt')
    else:
        print('The file doesn't exist')
'''

############################################################                    with open()

# with open()
# The with statement automatically closes the file without explictly using the .close(method)

'''
- Using the .close() method

file = open('data.txt', 'r')
print(f.read())
f.close()

- Here is the same code using with open()

#
with open('data.txt', 'r) as file_read:
    print(file_read.read())
'''

