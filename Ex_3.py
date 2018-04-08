# Rochelle Fritch
# Week 3, 11/02/2018

def collatz(x):

    if x % 2 == 0:
        print(x // 2)
        return x // 2

    elif x % 2 == 1:
        r = 3 * x + 1
        print(r)
        return r

n = input("Pick a number: ")
while n != 1:
    n = collatz(int(n))
