def factorial(num_1):   # Recursive function to calculate factorial
    if num_1 == 0 or num_1 == 1:
        return 1
    else:
        return num_1 * factorial(num_1 - 1)   # Recursive call to calculate factorial of num_1 by multiplying num_1 with the factorial of (num_1-1). 
                                      #This continues until the base case is reached (when num_1 is 0 or 1), at which point it returns 1.

num_1 = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num_1} is: {factorial(num_1)}")    #Call the factorial function with the user input to calculate and print the factorial of the given number.


def sum(num_2):   # Recursive function to calculate the sum of first n natural numbers
    if num_2 == 0:
        return 0
    else:
        return num_2 + sum(num_2 - 1)   # Recursive call to calculate the sum of first n natural numbers by adding n to the sum of (n-1). 
                                  #This continues until the base case is reached (when n is 0), at which point it returns 0.

num_2 = int(input("Enter a number to calculate the sum of first n natural numbers: "))
print(f"The sum of first {num_2} natural numbers is: {sum(num_2)}")    #Call the sum function with the user input to calculate and print the sum of the first n natural numbers.    





