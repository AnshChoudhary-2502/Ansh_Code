# class : blueprint for creating objects
# object : instance of a class

class Dog:
    species = "Siberian Husky"  # class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return "Woof!"

d1 = Dog("Sky", 5)
d2 = Dog("Buddy", 3)
print(d1.species)

Dog.species = "Labrador"  # modifying class attribute
print(d2.species)

d1.name = "Max"  # modifying instance attribute
print(d1.name)  


# Inheritance : creating a new class from an existing class
# single inheritance (a-->b), multiple inheritance (a-->b, c-->b), multilevel inheritance (a-->b-->c), hierarchical inheritance (a-->b, a-->c)

# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()