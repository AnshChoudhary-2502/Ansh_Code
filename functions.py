n = int(input("Enter a number to compute its factorial: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(n))

### lambda function :- short and sweet
n = lambda x: "positive" if x > 0 else ("negative" if x < 0 else "zero")
print(n(int(input("Enter a number: "))))