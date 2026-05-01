for i in range (5):
    print(i)
#The for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
#The range() function generates a sequence of numbers, 
# which is commonly used in for loops to specify the number of iterations.


i = 0

while i < 5:
    print(i)
    i += 1
#The while loop is used to execute a block of code as long as a specified condition is true.
#In this example, the loop will continue to execute as long as i is less than 5.
#The variable i is incremented by 1 in each iteration to eventually break the loop when i reaches 5.


for i in range(1, 11):
    print("udtree")
#This for loop will print the string "udtree" 10 times, as it iterates through the numbers from 1 to 10 (inclusive).


l=["udtree", "python", "programming"]
i=0
while i < len(l):
    print(l[i])
    i += 1
#This while loop will print each element of the list l.
#The loop continues as long as i is less than the length of the list (len(l)).


l=["udtree", "python", "programming"]
for i in l:
    print(i)
#This for loop will also print each element of the list l.
#In this case, the loop iterates directly over the elements of the list,
#so i takes on the value of each element in the list during each iteration.


for i in range(1, 11):
    print(i)
else:
    print("loop is over")
#In this example, the for loop iterates through the numbers from 1 to 10.
#After the loop finishes iterating, the else block is executed, printing "loop is over".
#this shows an else block can be used with a for loop to execute code after the loop has completed all iterations.


for i in range(1, 11):
    if i == 5:
        break
    print(i)
#In this example, the for loop iterates through the numbers from 1 to 10.
#When i equals 5, the break statement is executed, which immediately exits the loop.
#As a result, the numbers 1 to 4 will be printed, and the loop will terminate when it reaches 5.


for i in range(1, 11):
    if i == 5:
        continue
    print(i)
#In this example, the for loop iterates through the numbers from 1 to 10.
#When i equals 5, the continue statement is executed, which skips the rest of the code in the loop for that iteration and moves to the next iteration.
#As a result, the numbers 1 to 4 and 6 to 10 will be printed, while 5 will be skipped.
