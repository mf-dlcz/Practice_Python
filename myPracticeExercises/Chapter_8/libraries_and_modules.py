'''
                        Libraries & Modules:
'''


'''             Module:
A module is a file that contains a collection of related functions and 
classes ready for use in Python programs so that developers can avoid 
writing code from scratch.
'''


'''             Libraries:
A library is a collection of related modules. Whenever you need to use a 
module, you import it from its library
'''


#       #######################################################                 WORKING WITH MODULES:

'''             Scripts:
Scripts are files that are meant to be run directly. When you copy and paste 
code into your example.py file, you run it and get some output. That is a script. 
In the world of professional programming, you will work with scripts that won't 
necessarily print anything, but are meant to do something. They might apply a 
series of functions to some data, create new objects, or send data to a new file.
'''


'''             Modules:
Modules are files that are intended to be imported into running scripts. They contain 
definitions and statements (like functions, classes, and variables) that a script can 
use. Running a module does not generally produce output. 

Think of the employee networking program you created while studying classes and objects. If you 
didn't include any test code at the end of that file, it would not produce output on its own 
and can be considered a module.

There are many modules included as part of Python's standard library. Modules and libraries 
are also available for install. Additionally, you can write your own modules for use in 
your scripts.
'''


#           Reviewing a sample module:

# Imported this way, you must reference the module by name when you use its variables, classes, or 
# functions. 
'''
                SYNTAX:

import file_name

#* calling method in file:
variable = file_name.method_name(1, 2, 5)
'''

##########################################################################

#           Import definitions & Statements:

# When you name a particular definition or statement to import from a module, it brings that name into 
# the namespace of the importing script. Then, you can reference the name directly, without also naming 
# the module it came from
'''
from file_name import method_name

variable = method_name(1, 2, 5)
'''

##########################################################################

#           Importing all definitions & Statements:
# imports all definitions & statements from a module.
'''
from file_name import *
'''

###########################################################################

#           Import and assign alias:
# You can also assign an alias to an object or an entire module during import. This can be especially 
# helpful if you need to overcome a naming conflict in your scripting program. Or, if you have a function 
# or module with a long name, you can save yourself some typing using an abbreviation

'''
import file_name as f_name

total = f_name.method_name(1, 2, 5)
f_name.method_name()
'''

#           Provide an alias for a function
'''
from file_name import function_name as func_name

total = method_name(1, 2, 5)
'''