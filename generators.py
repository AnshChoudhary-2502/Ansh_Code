# generators are special type of iterators that allow user to iterate through a sequence of values without storing them all in memory at once
# it is used cz its memory efficient

def my_generator():
    yield 1
    yield 2
    yield 3     

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3   