# Write a code that reads a string from the input, adds 1 to the code point of every character and outputs the encrypted string. 
#
#  Sample Input 1:
#
# I love ord function!
#
# Sample Output 1:
#
# J!mpwf!pse!gvodujpo"

print("".join(chr(ord(letter) + 1) for letter in input()))

# inp = input()
# return_value = []

# for char in inp:
#     code_point = ord(char)
#     code_point += 1
#     char_cipher = chr(code_point)
#     return_value.append(char_cipher)
    
# print("".join(return_value))
