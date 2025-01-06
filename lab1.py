1)Calculate the multiplication and sum of two numbers

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

2)Declare two variables and print that which variable is largest using ternary operators

#Accepting input from the user
number1= float(input("Enter first number: "))
number2= float(input("Enter second number: "))

#Using ternary operator determine the largest number
largest= number1 if number1>number2 else number2

#Printing the result
print(f"The largest number between {number1} and {number2} is {largest}")
--------------------------------------------------------------------------------------------

3) Python program to convert the temperature in degree centigrade to Fahrenheit
#Accepting the temperature from the user in °C 
celsius= float(input("Enter temperature in Celsius: "))

#Converting to Fahrenheit
fahrenheit= (9/5) * celsius + 32

#Printing the result
print(f"{celsius}°c is equal to {fahrenheit}°F")

--------------------------------------------------------------------------------------------

4) Input the lengths of the sides of the triangle
a = float(input("Enter the length of the first side: "))
b= float(input("Enter the length of the second side: "))
c= float(input("Enter the length of the third side: "))

# Calculating the semi-perimeter
s = (a + b + c) / 2

# Calculating the area of triangle
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the result
print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area}")


