# Solution to Project Euler problem 4 "Largest palindrome product"
#
# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from
# the product of two 3-digit numbers.

# The product of two 3-digit numbers can at most be 6 digits. This means, that we are
# looking for a 6-digit palindrome. If let a, b and c be base-10 digits, then such a
# palindrome will have the following symmetry: "abccba". Generalizing this to the
# base-10 system, the palindrome (n) must satisfy the following equation:
# n=a(10^5+10^0)+b(10^4+10^1)+c(10^3+10^2) or n=100001a+10010b+1100c for all natural
# values of a, b and c in the interval from 0 to 9. The palindromes will decrease in
# size as we let c then b and then a decrease in size systematically, allowing us to
# exhaustively find the largest 6-digit palindrome which is also the product of two
# 3-digit numbers using a loop.

def compute():
    a = 9
    b = 9
    c = 9

    while True:
        n = a * 100001 + b * 10010 + c * 1100  # Palindrome generator

        for i in range(100, 1000):
            if n % i == 0 and n / i < 1000:  # Checking for two 3-digit divisors
                return n

        if c > 0:  # Decreasing size of next palindrome systematically (see description)
            c = c - 1
        elif b > 0:
            c = 9
            b = b - 1
        elif a > 0:
            c = 9
            b = 9
            a = a - 1


print(compute())
