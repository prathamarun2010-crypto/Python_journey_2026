class student:
    age = 17
    exam = "jee"


s1 = student()
s1.name = "UDtree"  #This code creates an instance of the student class and assigns the name attribute to that instance.
print(s1.name, s1.age, s1.exam)  #This code creates an instance of the student class and prints the age and exam attributes of that instance. 
                        #The output will be "17 jee".   

s2 = student()
s2.name = "Xtral"  #This code creates another instance of the student class and assigns the name attribute to that instance.
print(s2.name, s2.age, s2.exam)  #This code creates another instance of the student class and prints the age and exam attributes of that instance. 
                        #The output will also be "17 jee" since both instances share the same class attributes.        

# Name belongs to the object attribute, while age and exam belong to the class attribute.   

s3 = student()
s3.name = "Veronica"  #This code creates another instance of the student class and assigns the name attribute to that instance.
s3.age = 18  #This code assigns a new value to the age attribute of the s3 instance, which will override the class attribute for that instance. 
print(s3.name, s3.age, s3.exam)  #This code creates another instance of the student class and prints the age and exam attributes of that instance.

# the age change for s3 because instance attribute take over class attribute when accessed through that instance. 
# So, when we access s3.age, it will return the value of the instance attribute (18) instead of the class attribute (17). 