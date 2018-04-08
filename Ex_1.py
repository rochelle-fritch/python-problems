
# Rochelle Fritch
# Week 1

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 23
ans = fib(x)
print("Fibonacci number", x, "is", ans)


# Print out:
# My name is Rochelle, so the first and last letter of my name (R + E = 18 + 5) give the number  23. The 23rd Fibonacci number is 28,657.
