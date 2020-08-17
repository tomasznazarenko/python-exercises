# Suppose we have a file test.txt that looks like this:
#
# This
# is
# a
# test
# file
#
# Regard \n as the newline escape sequence.
# We want to read 10 bytes from this file. What will be the output of this code?

file = open("test.txt", 'r')
print(file.read(10))
file.close()

# This
# is
# a
