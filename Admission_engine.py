def average(physics, chemistry, mathematics):
    sum = physics + chemistry + mathematics
    count = 3
    return sum / count

# This function calculates the average of three subjects: Physics, Chemistry, and Mathematics.
# It takes the marks obtained in each subject as input, sums them up, and divides by the number of subjects (3) to return the average.

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
    
    # This function determines the grade based on the average marks obtained. 
    # It uses a series of conditional statements to check the range of the average and returns the corresponding grade.
    # The grading system is as follows:
    # - A: 90 and above
    # - B: 80 to 89
    # - C: 70 to 79
    # - D: 60 to 69

    
    def countdown(n):
        if n == 0:
            print("Launch!")
        else:
            print(n)
            countdown(n - 1)

    # This function implements a countdown from a given number n to 0.
    # It uses recursion to print the current number and then calls itself with n decremented by
    # 1 until it reaches 0, at which point it prints "Launch!".

while True:
    try:
        physics = float(input("Enter the marks obtained in Physics: "))
        chemistry = float(input("Enter the marks obtained in Chemistry: "))
        mathematics = float(input("Enter the marks obtained in Mathematics: "))
        break
    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")

# This block of code prompts the user to input the marks obtained in Physics, Chemistry, and Mathematics.
# It uses a while loop to continuously ask for input until valid numeric values are entered.

avg = average(physics, chemistry, mathematics)
print(f"The average marks obtained in Physics, Chemistry, and Mathematics is: {avg}")
grade_obtained = grade(avg)
print(f"The grade obtained based on the average marks is: {grade_obtained}")   

# This part of the code calculates the average marks using the average function and then determines the grade using the grade function.

countdown(3)

# Finally, this line calls the countdown function with an initial value of 3, 
# which will print the countdown from 3 to 0 and then print "Launch!".