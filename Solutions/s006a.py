# Solution to Project Euler problem 6 "Sum square difference"
#
# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...10^2=385 The
# square of the sum of the first ten natural numbers is, (1+2+...10)^2=55^2=3025 Hence
# the difference between the sum of the squares of the first ten natural numbers and the
# square of the sum is 3025-385=2640. Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.

# I have left two solutions to this problem, as I wanted to explore this problem in a
# more general way for other boundaries than just 100. In this solution (s006a) i will
# compute the answer using brute-force computation. For a more mathematical solution see
# s006b.

n = 100


def sumOfSquares():  # Computing the sum of all squares between 0 and n
    sum = 0
    for i in range(n + 1):
        sum = sum + i * i

    return sum


def squareOfSum():  # Computing the square of the sum of all numbers between 0 and n
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    sum = sum * sum

    return sum


def compute():  # Computing the difference between the two sums and thus the answer
    sumSquareDiff = squareOfSum() - sumOfSquares()
    return sumSquareDiff


print(compute())
