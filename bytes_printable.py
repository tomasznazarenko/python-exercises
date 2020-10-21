# Write a code that for the given integer code point checks whether this code point corresponds to a printable character (as opposed to a hexadecimal escape sequence), and if yes, outputs this character, otherwise outputs False.
# Printable range is from 32 to 126, including these numbers.

inp = int(input())

if inp in range(32, 127):
    print(chr(inp))
else:
    print("False")
