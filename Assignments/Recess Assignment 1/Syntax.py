#Executing python syntax
print("Hello World!")

#Python Indentation
if 10>5:
    print("10 is greater than 5")
else:
    print("5 is greater than 10")    

#Python Variables
a=10    #integer
b="Stacey"      #String
c=True     #Boolean
d=10.5     #Float
colors = ["blue", "yellow", "green"]   #list

# Print variables
print("a =", a)
print("b =", b)
print("d =", d)
print("c =", c)
print("colors =", colors)

# Conditional Statements
if 10>5:
    print("10 is greater than 5")
else:
    print("5 is greater than 10")   

#functions
def my_function():
  print("Hello i am a function")

my_function()

#Data Types
a=10    #integer
b="Stacey"      #String
c=True     #Boolean
d=10.5     #Float
colors = ["blue", "yellow", "green"]   #list
nums = (4, 5, 7)  #tuple
colors = {"blue", "yellow", "red"}  #set
student = {"name": "Sarah", "age": 27, "grade": "A"}  #dictionary

#Loops
#for loop
fruits = ["banana", "apple", "berries"]
for fruit in fruits:
    print(fruit)

#while loop
count = 0
while count < 5:
    print(count)
    count += 1  

#Python Classes  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

#Python Objects 
person1 = Person("Bob", 25)
person1.greet()  


