#importing module from another
import modules

modules.greeting("Ram")
a = modules.person1["age"]
print(a)


#There are several built-in modules in Python, which you can import whenever you like.
import platform
x = platform.system()
print(x)

#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

import platform
x = dir(platform)
print(x)
