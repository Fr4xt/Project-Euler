# Solution to Project Euler problem 4 "Smallest multiple"
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder. What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

# For a number m to be divisible by all numbers from 1 to n, m most have all prime
# numbers p below n as factors. This may seem a bit abstract, but is actually rather
# intuitive and follows directly from the prime factorization theorem. An easy way to
# find a value for m would therefore be to compute n!, as this would surely be divisible
# by all numbers from 1 to n. n! is however not the smallest number divisible in all
# numbers 1 through n. To find this number, the exponents in n!'s prime factorization has
# to be lowered to the smallest possible value, such that the value of any prime
# evaluated at its exponent doesn't exceed the value of n. This can be done by finding
# all primes below n, and raising these to the power of logp(n) rounded down to the
# nearest integer. Multiplying all these together in a running product will yield the
# smallest number, that can be divided by each of the numbers from 1 to n. To solve the
# problem, n is then simply set to 20

import math  # Needed for logarithms

n = 20


def isPrime(p):  # Finds all prime numbers below n
    if p == 2:  # Needed since the for loop starts at 2
        return True

    for i in range(2, p):
        if p % i == 0:
            return False
    return True


def compute():  # Finds the value of m (see description)
    product = 1
    for p in range(2, n + 1):
        if isPrime(p):
            product = product * p ** math.trunc(math.log(n, p))
    return product


print(compute())
