# Rochelle Fritch
# Week 3 - Collatz conjecture, 11/02/2018

# "The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
# start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous 
# term is even, the next term is one half the previous term. Otherwise, the next term is 3 times the previous term plus 1. 
# The conjecture is that no matter what value of n, the sequence will always reach 1."
# (https://en.wikipedia.org/wiki/Collatz_conjecture)


def collatz(x):                 # Define the Collatz conjecture function

    if x % 2 == 0:              # If x is even /2 (if divided by 2 and the remainder is 0), == is equals (= is used for defining an operator)
        print(x // 2)
        return x // 2

    elif x % 2 == 1:            # If x is odd *3 & +1 (if divided by 2 and remainder is 1)
        r = 3 * x + 1
        print(r)
        return r

n = input("Pick a number: ")    # Take any number n
while n != 1:                   # != does not equal
    n = collatz(int(n))
