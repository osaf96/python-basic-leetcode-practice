

## LOOPS
# Loops allow you to repeatedly execute a block of code. For example:
my_list = [1, 2, 3]
for item in my_list:
    print(item)
# The above code will print 1, 2, 3

# You can also use the range() function to generate a sequence of numbers. For example:
for num in range(3):
    print(num)
# The above code will print 0, 1, 2

# You can also use the range() function to generate a sequence of numbers with a starting point. For example:
for num in range(1, 3):
    print(num)
# The above code will print 1, 2


# You can also use the range() function to generate a sequence of numbers with a starting point and a step size. For example:
for num in range(1, 3, 2):
    print(num)
# The above code will print 1

# Loops and indexing
# You can also use loops and indexing to iterate over a sequence. For example:
word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
# The above code will print 0, a, 1, b, 2, c, 3, d, 4, e


for number in range(1,10):
    print(number)
    
while(number < 10):
    print(number + 1)
    number += 1
    
# The above code will print 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# while loops are used to repeatedly execute a block of code as long as a condition is true.
# for loops are used to iterate over a sequence of elements.
