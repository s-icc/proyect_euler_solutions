"""

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

from math import factorial

fact_num = str(factorial(100))
digits_sum = 0

for n in fact_num:
	digits_sum += int(n)

print(digits_sum)

# [Finished in 373ms]