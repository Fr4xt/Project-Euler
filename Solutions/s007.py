# Solution to Project Euler problem 7 "10001st prime"
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13. What is the 10001st prime number?

# This program is utterly stupid, and likely breaks every last one of Pythons
# coding-conventions. It however yields the correct result within a reasonable
# computation time, so I am going to let it stay as my definitive solution to problem 7
# for now. If i ever have the time and energy, I will be sure to revisit the solution
# and write it properly. The program simply finds any arbitrary number n of primes p
# using exhaustive computation. It does so be creating a running list of consecutive
# primes, and then finding the first number larger than any number in the list, that
# isn't divisible by any of the found primes. This number must be prime (by the prime
# factorization theorem) and is therefore appended to the list. This process is repeated
# until the length of the list is that of n. The problem is then solved by printing the
# most recent (and therefore largest) element in the list.

n = 10001


def isPrime(p, primes):  # Checks wether p is divisible by any prime in the list
    for i in range(len(primes)):
        if p % primes[i] == 0:
            return False

    return True


def compute():  # Computes the nth prime number
    p = 1  # Starts at 1 since the while-loop increments at start
    primes = []

    while len(primes) < n:  # Writes n number og primes to list using isPrime function
        p = p + 1

        if p == 2:  # Needed since prime list is initially empty
            primes.append(p)
            continue

        if isPrime(p, primes):
            primes.append(p)

    return primes[-1]  # primes[-1] fetches latest (and therefore largest) element


print(compute())
