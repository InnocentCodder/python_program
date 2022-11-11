# 3.	Write a Python program to find the simple interest. Principal amount, rate and time inputted from keyboard.
p = int(input("Enter the Principal Amount --> "))
r = int(input("Enter the rate of Interest --> "))
t = int(input("Enter the period of Time --> "))

simple_interest = (p*r*t)/100

print("The Simple interest on the given amount is -->", simple_interest)