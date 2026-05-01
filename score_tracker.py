i = 0  #Initialize a variable i to 0, which will be used to store user input for marks and control the while loop.

count = 0  #Initialize a variable count to 0, which will be used to keep track of the number of valid marks entered by the user.
           #Each time a valid mark is entered, count will be incremented by 1.

total =   0  #Initialize a variable total to 0, which will be used to accumulate the sum of all valid marks entered by the user. 
             #Each time a valid mark is entered, it will be added to total.
while i != "exit"  :#The while loop will continue to execute as long as the variable i is not equal to the string "exit". 
                    #This allows the user to keep entering marks until they choose to exit the program by typing "exit".
    i = (input("Enter the marks (or type 'exit' to quit): "))
    if i == "exit":  #If the user inputs "exit", the program will print a message and break out of the loop, ending the score tracker.
        print("Exiting the score tracker.")
        break
    i = int(i)  #Convert the input string to an integer for numerical processing
    count += 1  #Increment the count variable by 1 to keep track of the number of valid marks entered by the user.
    total += i  #Add the entered mark (i) to the total variable to keep a running sum of all valid marks entered by the user.
    if i >= 250 and i <= 300:
        print("rank 1 Tier: excellent.")
    elif i > 150 and i < 250:
        print("rank 2 Tier: strong.")
    elif i > 300:
        print("invalid marks.")    
    else:
        print("Improvement needed for iit roorkee.")

print(f"Total marks entered: {total}")
print(f"Total number of entries: {count}")
