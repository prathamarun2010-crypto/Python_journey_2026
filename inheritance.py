class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}."
    
class Child(Parent):

    def __init__(self, name, age):
        self.name= name
        self.age = age
        print(f"Child's name is {self.name} and age is {self.age}.")   


parent = Parent("Alice")
print(parent.greet())
child = Child("Bob", 10)
print(child.greet())    