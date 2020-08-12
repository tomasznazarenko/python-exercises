# Below, we have written a decorator price_string. The function takes another function with one parameter as its argument, 
# converts its output to string and adds the pound sign to this string to get the price of a product.
# 
# def price_string(func):
#     def wrapper(quantity):
#         return "£" + str(func(quantity))
# 
#     return wrapper
# 
# Write a function new_price that will take an argument and return the value with a 10% discount. 
# That is, if the given price was 100, the function new_price should return 90.0 (it will be a float value), 
# and the decorated function should return £90.0.
# 
# You needn't take any input; just write the body of the function and decorate it.

def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper  


@price_string
def new_price(price):
    return 0.9 * price
