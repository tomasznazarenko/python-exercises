# Here we have a predefined function that receives some user input and removes, if found, 
# all extra spaces at the beginning and at the end of a line using the built-in function strip().
# 
# def from_input(inp):
#     string = inp.strip()
#     return string
# 
# Create the body of a @tagged decorator that will return the string wrapped in the <title></title> HTML tag. 
# For example, for the word Test it should output <title>Test</title>. 
# You don't need to take any input or call a function; just write the body of the decorator.
def tagged(func):
    def wrapper(inp):
        return f'<title>{func(inp)}</title>'
    return wrapper
