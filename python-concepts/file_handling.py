# File handling in python
# File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.
# Example:
#
# # Open a file
file = open("file.txt", "w")

# Write to a file
file.write("Hello, World!")

# Close the file
file.close()
# The above code will create a file named file.txt and write Hello, World! to it. The file will be closed after writing.
# You can also read from a file. For example:
# Open a file
file = open("file.txt", "r")

# Read from a file
print(file.read())
 