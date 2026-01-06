f = open("ansh.txt", "r")
print("File name:", f.name)
print("File mode:", f.mode)
print("if closed:", f.closed)
content = f.read()
print("File content:\n", content)

f.close()
print("if closed:", f.closed)


with open("ansh.txt", "") as file:                # using with statement file will be closed automatically
    file.write("Vehicle No. : GJ09EA3303\n")
    file.write("Purchase Period : Dhanteras\n")

with open("ansh.txt", "r") as file:
    content = file.read()
    print("Updated File content:\n", content)

# file = open("filename", "x")  x= operation on file
# file.close()  to close file 
# f.name: Returns the name of the file that was opened (in this case, "geek.txt").
# f.mode: Tells us the mode in which the file was opened. Here, it’s 'r' which means read mode.
# f.closed: Returns a boolean value- False when file is currently open otherwise True.

try:
    with open("Ansh.txt", "r") as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist.")