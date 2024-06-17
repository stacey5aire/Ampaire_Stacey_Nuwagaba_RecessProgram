#Error Handling
#Exceptions handling with try , except,else and finally
#Custom Exceptions

""" 
    NOTES
    Error Handling- Help handle unexpected situations and errors.

    1.Try: contains code that might throw an exception
    NB: If an exception occurs the rest of the code in the try block is skipped or ignored

    2. Except : Catches and handles exceptions.
     - You can specify different handlers for different actions
    
    3. Else: The code runs if no exception occurs
    if no exceptios raised in the try block it runs

    4. Finally: It runs whether an exception is raised / occured or not

    More :
    try/except
        atch and recover from exceptions raised by Python, or by you.
    try/finally
        Perform cleanup actions, whether exceptions occur or not.
    raise
        Trigger an exception manually in your code.
    assert
        Conditionally trigger an exception in your code.
    with/as
        Implement context managers in Python 2.6, 3.0, and later (optional in 2.5).

 """

#Example 1: Handle Exceptions with division by zero
try:
    number = int(input("Enter a number: "))
    result = 20/number

except ValueError:
    print("Ivalid Number! Please Enter a valid number")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed") 

else:
    print(f"Result is {result}")

finally:
    print("Execution completed successfully")

# Exercise 1: Write a function that converts a string to an integer and handle both ValueError
# if a the string cannot be converted to an integer and the TypeError if the input is not a string
# Use multiple except block to handle these exceptions.


try:
    string= (input("Enter a string: "))
    result1= int(string)
except ValueError:
    print(f"ValueError: '{string}' cannot be converted to an integer.")
     
except TypeError:
    print(f"TypeError: '{string}' is not a string.")
      
finally:
    print("Execution completed successfully") 

# Custom exception handling
# Example 2: Exception raised for error in the input, if funds are insufficient

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account"
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom exceptions handling
try:
    balance = 20000
    amount_to_withdraw = float(input("Enter the amount to withdraw: "))
    new_balance = withdraw(balance, amount_to_withdraw)

except InsufficientFundsError as e:
    print(f"Error: {e.message}")

except ValueError:
    print("Invalid input! Please enter a numeric value.")

else:
    print(f"Withdrawal Successful! New Balance is {new_balance}")

finally:
    print("Execution successful")





"""
#Raising a Custom Exception
This involves defining your own exception class (usually inheriting 
from the built-in Exception class) and then using the raise keyword 
to trigger it when a specific condition occurs.



"""

#Exercise 2: Create a custom exception InvalidAge and write a function that raises
#this exception if the given age is negative. Handle this custom exception when calling the function

class InvalidAge(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age: {self.age}. Age cannot be negative."
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAge(age)
    else:
        print(f"Age is valid: {age}")

# Custom exception handling
try:
    age = int(input("Enter your age: "))
    check_age(age)

except InvalidAge as e:
    print(f'Error: {e.message}')

finally:
    print("Age validation completed")

    
