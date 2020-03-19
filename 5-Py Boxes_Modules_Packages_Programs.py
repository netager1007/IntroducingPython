# Standalone Programs
# -------------------


# Command_Line Arguments
# ----------------------
# On your computer, create a file called test2.py that contains these two lines:
import sys
print('Program arguments:', sys.argv)

# $ python test2.py
# Program arguments: ['test2.py']
# $ python test2.py tra la la
# Program arguments: ['test2.py', 'tra', 'la', 'la']


# Modules and the import Statement
# --------------------------------
# We refer to code of other modules by using the import statement.
# This makes the code and variables in the imported module available to your program.

# Import a Module with Another Name
# ---------------------------------
# you can import using an alias.

# import report as wr
# description = wr.get_description()
# print("Today's weather:", description)

# Import Only What You Want from a Module
# ---------------------------------------
# With Python, you can import one or more parts of a module.
# Each part can keep its original name or you can give it an alias.
# First, let’s import get_description() from the report module with its original name:

# from report import get_description
# description = get_description()
# print("Today's weather:", description)

print('')
# Module Search Path
# ------------------
# Where does Python look for files to import? It uses a list of directory names
# and ZIP archive files stored in the standard sys module as the variable path.
# You can access and modify this list. Here’s the value of sys.path for Python 3.3 on my Mac:
import sys
for place in sys.path:
    print(place)

# Python looks in the current directory first when you try to import something:
# The first match will be used. This means that if you define a module named random and it’s in the search
# path before the standard library, you won’t be able to access the standard library’s random now.


# Packages
# --------
