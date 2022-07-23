# Solution to Project Euler problem 6 "Sum square difference"
#
# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...10^2=385 The
# square of the sum of the first ten natural numbers is, (1+2+...10)^2=55^2=3025 Hence
# the difference between the sum of the squares of the first ten natural numbers and the
# square of the sum is 3025-285=2640. Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.

# I have left two solutions to this problem, as I wanted to explore this problem in a
# more general way for other boundaries than just 100. In this solution (s006b) i will
# therefore compute the answer using a general formula for finding the difference
# between the sum of the squares and the square of the sum between 1 and any arbitrary
# natural number n. This formula is found by first considering the formula for summing
# up the numbers 1 through n (the Gauss formula): n(n+1)/2, and the formula for summing
# up n consecutive squares: n(n+1)(2n+1)/6. A general formula for all n can thus be
# found by squaring the Gauss formula and subtracting the consecutive square formula
# from it. This yields a lengthy expression, that when reduced gives the following:
# n(3n+2)(n+1)(n-1)/12. To solve the problem, n is then simply set to 100.

n = 100


def compute():
    sumSquareDiff = n * (3 * n + 2) * (n + 1) * (n - 1) / 12
    return sumSquareDiff


print(compute())
