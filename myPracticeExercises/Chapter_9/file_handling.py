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

# Create a file and write a welcome message to it.
# f = open('welcome.txt', 'w')
# f.write('Hello! This is my first time writing on a file. Yay!')

# Open the file and print its contents.
# f = open('welcome.txt', 'r')
# print(f.read())

# Closes the file
# f.close()

#####################################################################
#*          CHALLENGE: Add data to an existing file: