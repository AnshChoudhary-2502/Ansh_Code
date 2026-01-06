X = str(input("Enter a string: "))

for letter in X:
    if letter == 'A' or letter == 'a' or letter == 'h' or letter == ' ':
        continue
    print('Current Letter :', letter)

while len(X) > 0:
    print('Current String :', X)
    break