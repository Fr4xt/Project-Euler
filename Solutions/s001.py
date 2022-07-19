# Solution to Project Euler problem 1 "Multiples of 3 or 5"
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5,
# 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5
# below 1000.

# One could likely calculate this using some clever modification of the Gauss formula
# (n(n+1)/2), but seeing as a simple for loop can compute this sum in less than a
# second this approach will be utilized instead.

sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i

print(sum)
