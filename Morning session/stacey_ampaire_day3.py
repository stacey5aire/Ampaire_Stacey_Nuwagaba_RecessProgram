#Python Best Practices
"""
1. Indentation
2. Maximum Line Length : Limit to 79 characters
3. Blank Lines
4. Use meaningful names
5. Use List Comprehensions
"""
#Example of good meaningfull name


def calculate_area(radius):
    pass


total_price = 10000

#Example of lazy student meaningful name


def calc(r):
    pass


tp = 10000

#Comprehensions (Lists, dictionaries)

#Python operators
"""_summary_
Name of operator              Example
Addition                       x + y
Subtraction                    x - y
Multiplication                 x * y
Division                       x / y
Modulus                        x % y
Exponentation                  x ** y
Floor Division                 x // y

Comparison Operators
Name                           Example
Equal                           =
Not Equal                       !=
Greater Than                    >
Less Than                       <
Greater Than Or Equal           >=
Less Than Or Equal              <=

#Example of Python Logical Operators

Name of operator                 Symbol with Example    
and                                and
or                                 or
not                                not  


#Example of Membership Operators
Name                              Symbol with example   
AND                                
OR
XOR
NOT

"""


#Comprehensions (list, dictionary comprehensions)
"""_summary_
Comprehensions provide a concise way to create lists and dictionaries
What is the symbol for
lists                        {} squarre brackets           
dictionaries                 [] curly brackets
"""


#Example 1: Basic List Comprehensions

#Create a list of squares in range of 10


list_squares=[x**2 for x in range(10)]
print(list_squares)

#Exercise 1

#create a list of even squares in the range of 20

# List comprehension to get even squares 


even_squares = [x**2 for x in range(20) if x**2 % 2 == 0]
print(even_squares)

#Example 2: Dictionary comprehension


favorite_cars = ['RangeRover', 'LandCruiser', 'Tesla', 'Lamborghini']
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths)


#Exercise 2: Create a list of tuple where each tuple contains a number and its cube for numbers

# Create a list of tuples where each tuple contains a number and its cube

# Dictionary comprehension to create a dictionary with numbers and their cubes


number_cubes = {x: x**3 for x in range(20)}

# Convert the dictionary to a list of tuples


number_cubes_tuples = list(number_cubes.items())

print(number_cubes_tuples)


