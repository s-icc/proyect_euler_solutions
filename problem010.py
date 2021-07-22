"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from math import sqrt

def es_primo(n):
    for i in range(2, round(sqrt(n)) + 1):
        if (n % i == 0): return False
    return True

total = 0

for i in range(2, 2000000):
    if (es_primo(i)): total += i

print(total)

# [Finished in 84.5s] xd
