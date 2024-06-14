#Defining Functions

#Function syntax and parameters
#Return values
#Lambda functions

#Functions in python are defined using the 'def function' key word followed by parathensis

#Example 1
def multiply1(a,b):
    return a * b

result=multiply1(2,3)
print(multiply1)



#Example 2
#multiply return values

def get_coordinates():
    return 10, 20

x, y =get_coordinates()
print(x,y)

#Exercise 1: Define a function greet with a parameter name set to "Guest"
#  and welcome message "I am a software programmer"

def greet(guest):
    print("Hello",guest, "I am software programmer")

greet("Stacey")    
        
#Example3 : Return multiple values of name and position
def get_name_and_position():
    name = "Ampaire"
    position = 1
    return name, position

# Call the function and unpack the return values
name, position = get_name_and_position()

print(f"Name: {name}, Position: {position}")


#Exercise2: Return multiple return values of your name and age
def get_name_and_age():
    name = "Stacey"
    age = 23  
    return name, age

# Call the function and unpack the return values
name, age = get_name_and_age()

print(f"Name: {name}, Age: {age}")

#Notes
"""_summary_

def: Keyword to define a function
function name: Name of function
parameters: optional, arguments passed to the function
Docstrings: Optional, describes the function purpose
return: returns a value from a function

"""

#Syntax for defining a function
#def function_name(parameters):
"""Docstring Optional
       Function Body
       Return value"""

#Lambda Functions
#defined using the lambda keyword
#Syntax; lambda arguments: expression
#lambda is the keyword to define a lambda function.
#arguments: are the parameters that the lambda function takes (can be zero or more).
#expression: is a single expression evaluated and returned by the lambda function.

#Example
# Lambda function to add two numbers
add = lambda x, y: x + y

# Call the lambda function with arguments
result = add(5, 3)

print(f"Result: {result}")

#Example 6: Use cases of lambda function for sorting
# List of coordinates
coordinates = [(1, 2), (3, 4), (0, -1), (-2, 3)]

# Sort by the x-values
#sorted_by_x = sorted(coordinates, key=lambda coord: coord[0])
coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)
#print("Sorted by x-values:", sorted_by_x)


#Map, Filter and Reduce
#Example 6: Get squares of 1 to 5 using map, filter and reduce

number_squares = [1,2,3,4,5]

square = list(map(lambda x: x**2, number_squares))

print(square)

#Exercise 4: Define a function to get user info that accepts arbitrary keyword arguments and prints
#each key value pair 
#Syntax
def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
get_user_info(name="Alice", age=30, email="alice@example.com", country="Wonderland")


