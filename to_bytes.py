# Write a code that takes a given number, converts it to a bytes object and outputs the sum of its bytes.
# A little spoiler: the test numbers are going to be greater than 255, so you're going to need at least 2 bytes to encode them.

x = (int(input())).to_bytes(2, byteorder='little')
print(x[0] + x[1])
