

def fib(n):
    """
    every number after the first two is the sum of the two preceding ones
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(11):
    print(fib(i))
