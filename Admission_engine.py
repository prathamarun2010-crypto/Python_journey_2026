def average(physics, chemistry, mathematics):
    sum = physics + chemistry + mathematics
    count = 3
    return sum / count

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
    
    def countdown(n):
        if n == 0:
            print("Launch!")
        else:
            print(n)
            countdown(n - 1)
    
while True:
    try:
        physics = float(input("Enter the marks obtained in Physics: "))
        chemistry = float(input("Enter the marks obtained in Chemistry: "))
        mathematics = float(input("Enter the marks obtained in Mathematics: "))
        break
    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")
avg = average(physics, chemistry, mathematics)
print(f"The average marks obtained in Physics, Chemistry, and Mathematics is: {avg}")
grade_obtained = grade(avg)
print(f"The grade obtained based on the average marks is: {grade_obtained}")   

countdown(3)