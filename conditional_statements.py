age = int(input("Your age is: "))
if age >0 and age <18:
    print("Minor")
elif age >=18 and age < 50:
    print("Eligible")
elif age >= 50:
    print("Not Eligible")
else:
    print("Invalid Age And Age cannot be Negative")