# Rochelle Fritch 
# Exercise 4, 24/02/2018

# Please complete the following exercise this week. It is problem 5 from Project Euler. 
# The problem is as follows. 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. 
# Add your answer to your GitHub repository.

# tell if a number is divisible by 1 to 20
def isDiv1to20(number):
    for i in range(2, 21):      # Always end with +1 over the number you want to end with.
        if number % i !=0:      # if the remainder does not equal 0
            return False
    return True        

# starting at 20, check if it's divisible by 1 to 20.
# to optimise we can check every 20, rather than 1-20.
number = 20
while True:
    if isDiv1to20(number):
        break
    number +=20  # increment number

# if we find this number then stop
print(number)
