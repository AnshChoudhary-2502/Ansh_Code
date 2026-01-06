# map() : modify all items in an iterable (list, tuple etc.) using a function and return a map object (an iterator)
# many input ---> many output
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  

# filter() : filter items in an iterable based on a function that returns True or False and return a filter object (an iterator)
# many input ---> some output
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))   

# reduce() : apply a function cumulatively to the items of an iterable, reducing it to a single value
# many input ---> single output
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  