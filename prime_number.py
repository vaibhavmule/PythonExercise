
def primes(till):
    for num in range(1, till + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


print(primes(100))
