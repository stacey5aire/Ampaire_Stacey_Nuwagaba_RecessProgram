# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""summary
    
    Dictionaries in python are collections of keys and values
    -Unordered
    -mutable and
    -indexed by keys
    
"""
    
    # Example 1: Create a dictionary
    # Create a dictionary for a student pursuing software engineering
    # the key must be your name, age, technology interest and year of study. put
    # your own details
    
student_dict = {
        'name' : 'Ampaire Stacey',
        'age' : '30',
        'technology': 'AI and ML',
        'course': 'BSE',
        'Year': 'Year3'
    }

#Exercise 1: Change the value of a key in the dictionary
student_dict['age']=22
student_dict['technology']='IoT'
print(student_dict)


#Ex2: Remove the key and value from dictionary after adding an email and its value


student_dict['email']="staceyampaire3@gmail.com"

print(student_dict)

# Removing a key-value pair, for example, the 'email' key using del statement

del student_dict['email']


# Printing the dictionary after removing the 'email' key

print("After removing 'email':", student_dict)

#Common dictionary methods

"""
__summary__
get() //returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() //updates the dictionary with the elements from another dictionary

pop() //Removes the specified key and return the corresponding value




"""
#Example 3: Use the get method to get the value

print(student_dict.get('technology'))

#Exercise 3: Use the update method to change value in age

# Updating the value of the 'age' key

student_dict.update({'age': '27'})

# Printing the dictionary after updating the 'age' key

print("After updating 'age':", student_dict)

#Exercise 4: Use if to check if key 'age' is present in the dictionary
# Checking if 'age' key is present in the dictionary and returning its value

if 'age' in student_dict:

    age_value = student_dict['age']

    print(f"The key 'age' is present in the dictionary with value: {age_value}")

else:

    print("The key 'age' is not present in the dictionary.")

#keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())    

"""
summary 
keys() returns a view of objects that displays a list of keys
values() returns a view of objects that displays a list of values
items() returns a view of objects that displays a list of items


"""

#Exercise 5: Use the update method to change the course and add
#  a new key "whatsapp_number" to the dictionary

# Updating the value of the 'course' key and adding 'whatsapp_number'
student_dict.update({'course': 'Computer Science', 'whatsapp_number': '+256 704273240'})

# Printing the dictionary after updating the 'course' keys, and adding 'whatsapp_number'
print("Dictionary after changing course and adding whatsapp number:", student_dict)



