# Solution to Project Euler problem 9 "Special Pythagorean triplet"
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2+b^2=c^2. For example, 3^2+4^2=9+16=25=5^2. There exists exactly one
# Pythagorean triplet for which a+b+c=1000. Find the product abc.

# This problem could be solved efficiently by constructing a function in two variables
# using the two given equations. Since we are however only considering solutions to this
# function less than or equal to 1000 (n), it is far cleaner and far more convenient
# (though less efficient) to just check if every possible value for a and b in the given interval
# satisfies the inequality and the two equations using exhaustive computation.

n = 1000


def compute():
    for a in range(1, n + 1):  # Iterates through all valid values for a
        for b in range(1, n + 1):  # Iterates through all valid values for b
            c = (a**2 + b**2) ** 0.5  # Calculates corresponding value for c

            if c % 1 == 0 and a + b + c == n and a < b < c:  # The three conditions
                return a * b * c


print(compute())
