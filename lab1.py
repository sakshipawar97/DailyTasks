#Calculate the multiplication and sum of two numbers

#Accepting input from the user
number1= float(input("Enter first number: "))
number2= float(input("Enter second number: "))

#Calculating multiplication and addition
multiplication= number1*number2
addition= number1+number2

#Printing the result
print(f"The multiplication of {number1} and {number2} is : {multiplication}")
print(f"The addition of {number1} and {number2} is : {addition}")


--------------------------------------------------------------------------------------------

#Declare two variables and print that which variable is largest using ternary operators

#Accepting input from the user
number1= float(input("Enter first number: "))
number2= float(input("Enter second number: "))

#Using ternary operator determine the largest number
largest= number1 if number1>number2 else number2

#Printing the result
print(f"The largest number between {number1} and {number2} is {largest}")
--------------------------------------------------------------------------------------------

# Python program to convert the temperature in degree centigrade to Fahrenheit
#Accepting the temperature from the user in °C 
celsius= float(input("Enter temperature in Celsius: "))

#Converting to Fahrenheit
fahrenheit= (9/5) * celsius + 32

#Printing the result
print(f"{celsius}°c is equal to {fahrenheit}°F")

--------------------------------------------------------------------------------------------

# Input the lengths of the sides of the triangle
#Taking the input of lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side : "))
side2 = float(input("Enter the length of the second side : "))
side3 = float(input("Enter the length of the third side : "))

# Calculating the semi-perimeter
semi_perimeter = (side1 + side2 + side3) / 2

# Calculating the area of the triangle
area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5

# Print the result
print(f"The area of the triangle with sides {side1}, {side2}, and {side3} is: {area:.2f}")


