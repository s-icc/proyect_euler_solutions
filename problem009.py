""" 

A Pythagorean traplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

from math import sqrt

for a in range(999):
    for b in range(999):
        c = sqrt(pow(a,2) + pow(b,2))
        if (c == int(c) and (a < b) and (b < c) and (a + b + c == 1000)):
            print(a*b*c)
            break

# [Finished in 3.9s]