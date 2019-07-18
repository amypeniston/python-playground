def factorial(n):
    """Calculate the factorial of a number n
    """
    if n <= 0:
        return 1
    return n * factorial(n-1)

for i in range(0, 10):
    print("Factorial {} = {}".format(i, factorial(i)))



def fibonacci(n):
    """Calculate the nth term in the fibonacci sequence
    """
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(0, 10):
    print("Fibonnaci term {} = {}".format(i, fibonacci(i)))
