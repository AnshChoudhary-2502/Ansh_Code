age = int(input("Your age is: "))

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