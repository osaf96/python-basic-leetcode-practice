## STRINGS
# Strings are used in Python to record text information, such as name. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello" to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).
# Indexing
# Indexing starts at 0 in Python. So, the string "hello" has the following indices:
# h e l l o
# 0 1 2 3 4

# You can use square brackets to grab single characters. For example:
my_string = "hello"
print(my_string[1])
print(my_string[3])
# The above code will print "e" and "l" respectively

# You can also use negative indexing to go backwards. For example:
my_string = "hello"
print(my_string[-1])
# The above code will print "o"

# You can also use a colon to grab everything up to a designated point. For example:
my_string = "hello"
print(my_string[:3])
# The above code will print "hel"

# You can also use a colon to grab everything after a designated point. For example:
my_string = "hello"
print(my_string[3:])
# The above code will print "lo"

# You can also use a colon to grab everything. For example:
my_string = "hello"
print(my_string[:])
# The above code will print "hello"
# print(my_string[8]) # This will throw an error
# The above code will print "e"

# Slicing
# You can use a colon to perform slicing which grabs everything up to a designated point. For example:
my_string = "hello"
print(my_string[1:])
# The above code will print "ello"

# You can also use a negative index to go backwards. For example:
# my_string = "hello"
print(my_string[-1])
# The above code will print "o"

# You can also use a colon to perform slicing backwards. For example:
my_string = "hello"
print(my_string[:-1])
# The above code will print "hell"

# You can also use a step size in the slicing. For example:
my_string = "hello"
print(my_string[::2])
# The above code will print "hlo"

# String Properties
# Strings are immutable. This means that once a string is created, the elements within it can not be changed or replaced. For example:
my_string = "hello"
# my_string[0] = "a"
# The above code will throw an error

# You can concatenate strings using the "+" sign. For example:
my_string = "hello"
print(my_string + " world")
# The above code will print "hello world"

# You can also use the "*" sign to repeat a string. For example:
my_string = "hello"
print(my_string * 3)
# The above code will print "hellohellohello"

# Built-in String Methods
# Strings have built-in methods. For example:
my_string = "hello"
print(my_string.upper())
# The above code will print "HELLO"

print(my_string.lower())
# The above code will print "hello"

print(my_string.split())
# The above code will print ['hello']

print(my_string.split('e'))
# The above code will print ['h', 'llo']

print(my_string.find('e'))
# The above code will print 1

print(my_string.center(20, '*'))
# The above code will print "*******hello********"

print('hello\thi'.expandtabs())
# The above code will print "hello   hi"

print(my_string.isalnum())
# The above code will print 

print(my_string.isalpha())
# The above code will print True

print(my_string.islower())
# The above code will print True

print(my_string.isspace())
# The above code will print False

print(my_string.istitle())
# The above code will print False

print(my_string.isupper())
# The above code will print False

print(my_string.endswith('o'))
# The above code will print True

print(my_string.startswith('h'))
# The above code will print True

print(my_string.split('e'))
# The above code will print ['h', 'llo']

print(my_string.partition('e'))
# The above code will print ('h', 'e', 'llo')

print(my_string.count('l'))
# The above code will print 2

print(my_string.capitalize())
# The above code will print "Hello"

print(my_string.replace('l', 'a'))
# The above code will print "heaao"

print(my_string.join('abc'))
# The above code will print "ahellobhelloc"

print(my_string.zfill(10))
# The above code will print "00000hello"

print(my_string.rjust(10, '*'))
print(my_string.ljust(10, '*'))
# The above code will print "hello*****"    

print(my_string.rfind('e'))
# The above code will print 1

## LIST
# Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed! You can also mix object types in a list. For example:
# my_list = [1,2,3]
# my_list = ['A string',23,100.232,'o']
# Just like strings, the len() function will tell you how many items are in the sequence of the list. For example:
my_list = ['one', 'two', 'three']
print(len(my_list))
# The above code will print 3

# Indexing and Slicing
# Indexing and slicing work just like in strings. For example:
my_list = ['one', 'two', 'three']   
print(my_list[0])
# The above code will print "one"

print(my_list[1:])
# The above code will print ['two', 'three']

# Concatenating lists
# You can concatenate lists just like strings. For example:
my_list = ['one', 'two', 'three']
another_list = ['four', 'five']
print(my_list + another_list)
# The above code will print ['one', 'two', 'three', 'four', 'five']

## DICTIONARY
# Dictionaries are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead. This key-value pair allows users to quickly grab objects without needing to know an index location. For example:
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])
# The above code will print "value1"

# Dictionaries are very flexible in the data types they can hold. For example:
my_dict = {'key1':123, 'key2':[12,23,33], 'key3':['item0','item1','item2']}
print(my_dict['key2'])
# The above code will print [12, 23, 33]

# You can also use built-in methods to grab keys and values. For example:
my_dict = {'key1':123, 'key2':[12,23,33], 'key3':['item0','item1','item2']}
print(my_dict.keys())
# The above code will print dict_keys(['key1', 'key2', 'key3'])






## TUPLES
# In Python, tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar. For example:
my_tuple = (1,2,3)
print(my_tuple[0])
# The above code will print 1

# You can also use built-in methods to grab values. For example:
my_tuple = (1,2,3)
print(my_tuple.index(2))
# The above code will print 1

print(my_tuple.count(2))
# The above code will print 1

## SETS
# Sets are an unordered collection of unique elements. For example:
my_set = set()
my_set.add(1)
print(my_set)
# The above code will print {1}

my_set.add(2)
print(my_set)
# The above code will print {1, 2}

## BOOLEANS
# Booleans are operators that allow you to convey True or False statements. For example:
print(1 > 2)
# The above code will print False

print(1 == 1)
# The above code will print True

## TUPLE UNPACKING
# Tuple unpacking allows you to assign variables from a tuple. For example:
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)
print(b)
print(c)

## LIST COMPREHENSIONS
# List comprehensions allow you to build out lists using a different notation. For example:
my_list = [x for x in 'word']
print(my_list)
# The above code will print ['w', 'o', 'r', 'd']

my_list = [x**2 for x in range(0, 11)]
print(my_list)
# The above code will print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

my_list = [x for x in range(0, 11) if x % 2 == 0]
print(my_list)
# The above code will print [0, 2, 4, 6, 8, 10]





    