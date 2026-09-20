from sys import argv
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [int(x) for x in argv[1:]]
primes = [num for num in numbers if isPrime(num)]
sums = sum(primes)
print("Prime numbers: ", primes)
print("Sum of prime numbers: ", sums)