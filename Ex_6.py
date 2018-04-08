# Rochelle Fritch
# Exercise 6 - Functions

# Write a Python script containing a function called factorial() 
# that takes a single input/argument which is a positive integer 
# and returns its factorial. The factorial of a number is that 
# number multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
# You should, in your script, test the function by calling it with 
# the values 5, 7, and 10.

# Functions - Section 4.6 in Python tutorial

#Sum5 = 0
#for i in range (1,6):
#    Sum5 = Sum5 + i
#print("The sum of the values from 1 to 5 inclusive is :", Sum5)

#def sumall(upto):
#    sumupto = 0
#    for i in range(1, upto + 1):
#        sumupto = sumupto + i
#    return sumupto
#print("The sum of the values from 1 to 50 inclusive is :", sumall(50))

#Following on from the example above, returning the factorial of that number

def factorial(x):
    fact = 1                # need to start with 1, as multiplying
    for i in range(1,x+1): 
        fact = fact * i
    return fact
print("The factorial of 5 is:", factorial(5))
print("The factorial of 7 is:", factorial(7))
print("The factorial of 10 is:", factorial(10))
