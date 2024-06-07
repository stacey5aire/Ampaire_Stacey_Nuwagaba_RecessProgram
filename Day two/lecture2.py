#Example 1
print("Example 1")
Age = 70

if Age < 18: 
    print('You are an adult')
elif Age > 65:
    print('you are senior citizen')
    
else:
    print('You are a Youth')
    
    
    
  # Example 2 
print("Example 2") 

grade = 50

if grade >=90:
    print('Excellent')
elif grade >= 80:
    print('very good')
elif grade >= 70:
    print('Good')

else: 
    print('Not good')

""" 
 Exercise:  Scenario: Write a python script to determine the price 
 of a movie based on age. Condition children under 13 get discount for price 
 =shs1000
 Teenagers between 13 and 18 get discount for price = shs 500
 Adults 18 and above pay full price = shs 2000
 Otherwise, senior citizens pay full price = shs 5000
   
    """

print("Exercise Solution____") 

def get_ticket_price(age):
    if age < 13:
        price = 2000 - 1000  
    elif 13 <= age < 18:
        price = 500  
    elif 18 <= age < 65:
        price = 2000 
    else:
        price = 5000  
    return price


try:
    age = int(input("Enter your age: "))
    ticket_price = get_ticket_price(age)
    print(f"The ticket price for age {age} is: {ticket_price}sh")
except ValueError:
    print("Please enter a valid age.")

#loops
#Exercise 2

"""_summary_
    
    Create your own list of favorite colors using for loop
    2.  Create a reverse of the input 12345 to be 54321 using while loop
    """
print()
print("Exercise 2 solution_______________________________________________________________")

count=1
while(count<=10):
   print("Count: ",count)
   count+=1

colors=["blue","red","yellow","green","purple"]
for color in colors:
    print(color)
reversed_list=colors[::-1]
for color in reversed_list:
    print(color)    

#number 2(while loop in reverse 54321)   
count=5
while(count>=1):
    print("Count: ",count) 
    count-=1 


    