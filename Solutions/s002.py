# Solution to Project Euler problem 2 "Even Fibonacci numbers"
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55,
# 89, ... By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# Much like problem 1 one could calculate this "elegantly" using the exact formula for
# the Fibonacci sequence ((Φ^n-(1-Φ)^n)/2). But once again seeing as a simple for loop
# can compute this sum in no time this approach will be utilized instead

n = 4000000


def compute():
    fibonacci = [0, 1]  # Defining the starting conditions for the fibonacci sequence
    sum = 0

    i = 0
    while fibonacci[-1] < n:  # fibonacci[-1] fetches most recent element
        fibonacci.append(fibonacci[i] + fibonacci[-1])

        if fibonacci[-1] % 2 == 0:  # fibonacci[-1] is now different due to append
            sum = sum + fibonacci[-1]

        i = i + 1

    return sum


print(compute())
