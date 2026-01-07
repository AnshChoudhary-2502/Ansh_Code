class student:
    def __init__(self, name, marks):
        self.name = name.capitalize()
        self.marks = marks
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        return sum/len(self.marks)   

s1 = student("ansh", [98, 97, 99, 96, 95])
s1.average()
print(f"Name: {s1.name}, \nAverage Marks: {s1.average()}")


# static method:- it is used at class level and not an object level

class employee:

    def __init__(self, name, role, department, salary):
        self.name = name
        self.role = role
        self.department = department
        self.salary = salary
    

class Engineer(employee):

    def __init__(self, name, role, department, salary, age, project):
        self.age = age
        self.project = project
        super().__init__(name, role, department, salary)     # Inheriting the properties of parent class employee

    def showdetails(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Age:", self.age)
        print("Project:", self.project)

a1 = Engineer("Ansh", "Intern", "Model Building", 500, 22, "Training")
a1.showdetails()



class order:
    def __init__(self, item, price):
        self.item = item.capitalize()
        self.price = price

order1 = order("earbuds", 3000)
order2 = order("headphones", 3500)

if order1.price < order2.price:
    print(order1.item, "is cheaper than", order2.item)
else:
    print(order2.item, "is cheaper than", order1.item)