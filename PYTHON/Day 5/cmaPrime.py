from ast import arg
from sys import argv
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = []
for i in range(1, 11):
    curr = int(argv[i])
    if isPrime(curr):
        lst.append(curr)
print("Prime numbers: ", lst)
print("Sum of prime numbers: ", sum(lst))