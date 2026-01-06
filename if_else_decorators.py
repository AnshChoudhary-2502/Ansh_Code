age = int(input("Your age is: "))
user = str(input("Enter your name: "))
is_member = bool(int(input("Are you a member? (1 for Yes, 0 for No): ")))

if age >6 and age <22:
    if is_member:
        print("You get a 30% discount!")
    else:
        print("You get a 15% discount!")

elif age >=22 and age <65:
    if is_member:
        print("You get a 20% discount!")
    else:
        print("You get standard 5% discount!")

elif age >=65 and age < 100:
    if is_member:
        print("You get a 30% discount!")
    else:
        print("You get a 15% discount!")

elif age >= 100:
    if is_member:
        print("You get a 50% discount!")
    else:
        print("You get a 25% discount!")

else:
    print("Invalid age entered")
    

# decorators are the additional functions which are usedf in modifying the other function and how it should behave 
# there is a wrapper function which wraps the original function and madifies its behaviour
def my_decorator(name):
     def wrapper():
         print("Thanks for shopping.")
         name()
         print("Have a nice day!")
     return wrapper

@my_decorator
def name():
    print(user)
name()