"""
                                                    '' if "__name__ == "__main__" in python ''

1) The if "__name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or
 being imported as a module into another script.

2) In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run
directly, the name variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to
the name of the module.

3) In this given example, the main function contains the code that should be run when the script is run directly. The if statement at the bottom check!
whether the _name_ variable is equal to _main_. If it is, the main function is called.

"""

# refer some tips or module from imports file or module alos imported from there.

from imports import *

vedant()
