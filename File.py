file = open("file.txt", "r")
content = file.read()
file.close()
print(content)

# Using with statement to automatically close the file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
    
# Appending to a file
with open("file.txt", "a") as file:
    file.write("This is an appended line.\n")

# Reading the updated file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Reading a file line by line
with open("file.txt", "r") as file:
        for line in file:
            print(line, end='')  # end='' to avoid adding extra new line

file.close()

