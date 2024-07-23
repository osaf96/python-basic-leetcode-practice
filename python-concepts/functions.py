## FUNCTIONS    
# Functions allow you to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code. Functions will be one of most basic levels of reusing code in Python, and it will also allow us to start thinking of program design. For example:
def say_hello():
    print("hello")
say_hello()
# The above code will print "hello"
#let me type the function myslef so i can understand it better give me an example of a function so i can write it by myself
# ask me some function to write 
# i will write it and you will tell me if it is correct or not
# i will write a function that takes a string and returns the string in uppercase
# i will write a function that takes a string and returns the string in lowercase

def uppercase_string(string):
    return string.upper()

def lowercase_string(string):
    print(string.lower()) 

print(uppercase_string("some lowercase string"))
lowercase_string("SOME UPPERCASE STRING")

# The above code will print "SOME LOWERCASE STRING" and "some uppercase string" respectively

# You can also pass arguments into a function. For example:
def say_hello(name):
    print(f"hello {name}")
say_hello("Jose")
# The above code will print "hello Jose"

# You can also set default values for arguments. For example:
def say_hello(name="Jose"):
    print(f"hello {name}")
say_hello()
# The above code will print "hello Jose"

# You can also return values from a function. For example:
def add(a, b):
    return a + b
result = add(1, 2)
print(result)
# The above code will print 3

# You can also return multiple values from a function. For example:
def add_subtract(a, b):
    return a + b, a - b
result = add_subtract(1, 2)
print(result)
# The above code will print (3, -1)

# You can also unpack the returned values. For example:
def add_subtract(a, b):
    return a + b, a - b
add, subtract = add_subtract(1, 2)
print(add)
print(subtract)
# The above code will print 3 and -1 respectively

# You can also use the *args and **kwargs syntax. For example:
def myfunc(*args):
    return sum(args)
result = myfunc(1, 2, 3, 4, 5)
print(result)
# The above code will print 15


# functions can be used in classes as well
# classes are used to create objects
# objects are instances of classes
# classes have attributes and methods
# attributes are variables that belong to the class
# methods are functions that belong to the class