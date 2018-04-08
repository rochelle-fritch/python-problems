
# Rochelle Fritch
# Exercise 5, 04/03/2018

# Opening data files in python, printing formatted data in python.

# Different ways to open files:
#   w = write
#   r = read (default)
#   a = append
#   r+ = read + write

# with - automatically closes a file after.
# Look @ Section 7.1 Fancier output

# 
# Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values 
# should have the decimal places aligned, with a space between the columns.


with open("data/iris.csv") as f:
    for line in f:                  # looping through each line in file
        x = line.split(',')         # splits lines into a list
        print(x[0],x[1],x[2],x[3])  # formats with correct blocking
   



