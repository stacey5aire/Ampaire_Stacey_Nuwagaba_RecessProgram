# Inheritance and method overriding
"""summary
--description
Inheritance and method overriding allows a class(child class) to inherit attributes and methods
from another class (parent class).

Key concepts
Base class (parent class): Class whose properties are inherited by another class.
Derived class (child class): Class that inherits attributes and properties from another base class.

    """
    
# Example 1: Syntax Create a class where a dog inherits from animal and overrides with a speak method

class Animal:
    def speak(self):
        return 'Mwe Mwe Mwe Mwe Mwe'
    
class Dog(Animal):
    def speak(self):
        return 'Barks'
    
# Implementatiion of inherited classes

animal = Animal()
dog = Dog()

print(animal.speak()) 
print(dog.speak())  

# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Method resolution Order (MRO). is order in which python looks for a method in hierarchy classes.

# Example 2: How polymorphismworks in python

class Animal:
    def speak(self):
        return "Croock"

class Dog(Animal):
    def speak(self):
        return "Barks"
    
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(Dog())
make_animal_speak(Cat())    


#Exercise 1: Create a simple application to manage different types of vehicles.
#Implement derived class to demonstrate inheritance and polymorphism
"""
Requirements
1.Base class to vehicle 
Attributes: make mode and year
Methods: display_info()

2. Derived classes:
Car: inherit from vehicle
attributes: number of doors
Overrides: display_info()

Motorcycle: inhrit from vehicle
Attributes: type_of_bike (cruiser, sport, touring)
Overrides: display_info()

#Exercise 2:
Create a function that accepts a list of vehicle objects and call their display_info() method
to print details of each vehicle
"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model} with {self.number_of_doors} doors")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        print(f"Motorcycle Info: {self.year} {self.make} {self.model} which is a {self.type_of_bike} bike")

def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
# Creating instances of Car and Motorcycle
car1 = Car("Toyota", "Camry", 2020, 4)
car2 = Car("Honda", "Accord", 2018, 2)
motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")
motorcycle2 = Motorcycle("Yamaha", "YZF-R3", 2021, "Sport")

# List of vehicles
vehicles = [car1, car2, motorcycle1, motorcycle2]

# Displaying information of all vehicles
display_vehicle_info(vehicles)




import csv
import json

# Reading and Writing Files

"""summary
Working with text files
Handling CSV files
JSON and XML file processing"""

# Working with text files,open,read,write,close
# NOTE: Python provides inbuilt functions to handle text files.
"""
Key concepts
Opening a file: open() function with file mode (r,w,a,r+)
Reading a file: read() function
Writing to a file: write() function
Closing a file: close() function

"""

# Example 3: Write a file and read a file

# Writing to a text file
with open("sample.txt","w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This is a second line in the file.\n")

# reading from a text file
with open("sample.txt","r") as file:
    content = file.read()
    print(content)


# Handling CSV files
"""
CSV (Comma Separated Values) file widely for data exchange. 
Key Concepts
Reading a CSV file: csv.reader() function
Writing to a CSV file: csv.writer() function
DictReader and DictWriter : These classes allow you to read and write CSV files using dictionaries.
"""

# Example 4: Reading and writing CSV files
import csv
# Writing to a CSV file
with open("sample.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","City"])
    writer.writerow(["Alice",25,"New York"])
    writer.writerow(["Bob",30,"San Francisco"])

# Reading from a CSV file
with open("sample.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# JSON and XML file processing
"""
JSON (JavaScript Object Notation) and XML (Extensible Markup Language) are popular formats used to structure data.
Key concepts
Loading JSON data: json.load() function for reading JSON file
Dumping JSON data: json.dump() function for writing JSON file
Parsing JSON data: json.loads() function for handling JSON string
"""

# Example 5: Reading and writing JSON files
import json

# Writing to a JSON file
student_data = {
    'name':'Stacey',
    'course':'BSE',
    'year':'Year 3'
}

# Open the file in write mode
with open("student.json","w") as file:
    json.dump(student_data,file)

# Reading from a JSON file
with open("student.json","r") as file:
    data = json.load(file)
    print(data)



# Exercise 2: Write and read xml file
import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("vehicles")

# Create a child element (Car)
car = ET.SubElement(root, "car")
car.set("make", "Toyota")
car.set("model", "Camry")
car.set("year", "2020")
doors = ET.SubElement(car, "doors")
doors.text = "4"

# Create another child element (Motorcycle)
motorcycle = ET.SubElement(root, "motorcycle")
motorcycle.set("make", "Yamaha")
motorcycle.set("model", "YZF-R3")
motorcycle.set("year", "2021")
type_of_bike = ET.SubElement(motorcycle, "type_of_bike")
type_of_bike.text = "Sport"

# Convert the tree to a string and write it to a file
tree = ET.ElementTree(root)
with open("vehicles.xml", "wb") as file:
    tree.write(file)

print("XML file 'vehicles.xml' written successfully.")



# Exercise 3: Using abstraction calculate the area and perimeter of a rectangle
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def main():
    # Create a Rectangle object
    rectangle = Rectangle(4, 7)
    
    # Calculate and print the area and perimeter
    print(f"Rectangle width: {rectangle.width}")
    print(f"Rectangle height: {rectangle.height}")
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")

if __name__ == "__main__":
    main()
