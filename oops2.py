# Polymorphism in Python
# 1. Compile-time Polymorphism (Method Overloading)
# 2. Run-time Polymorphism (Method Overriding, operator overloading)

# 1. method overloading: same method name with different parameters quantity or type

class calculator:
    def add(self, *args):
        return sum(args)
    
calc = calculator()
print(calc.add(2, 3))          # Output: 5
print(calc.add(2, 3, 4, 5))    # Output: 14 


# 2. method overriding: child class has a method with the same name as in parent class but different implementation`
class Animal:
    def sound(self):
        return "I am the king"

class dog(Animal):
    def sound(self):
        return "Woof! Woof!"
    
a = Animal()
d = dog()
print(a.sound())  # Output: I am the king
print(d.sound())  # Output: Woof! Woof!

# 3. operator overloading: same operator behaves differently based on the operands

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"         

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Uses the overloaded + operator
print(p3)      # Output: Point(6, 8)