def avg():    #function to calculate average of three numbers
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c=int(input("Enter the number: "))
    
    
    average = (a + b + c) / 3
    print(f"The average is: {average}")

avg()  #Call the avg function to execute the code and calculate the average of three numbers entered by the user.
       #this is used to call the function and execute the code inside it. When this line is executed, 
       # the program will prompt the user to enter three numbers, calculate their average, and print the result. 



def birth_date(name):  #function to print the birth date of a person
    day = int(input("Enter the day of your birth: "))
    month = int(input("Enter the month of your birth: "))
    year = int(input("Enter the year of your birth: "))
    
    print(f"{name}, Your birth date is: {day}/{month}/{year}") 
    return "wish you a happy birthday!"  #Return a birthday wish message after printing the birth date of the person.

a=birth_date("UDtree")  #Call the birth_date function with the argument "Udtree" to execute the code and print the birth date of the person.    
print(a)  #Print the returned birthday wish message.