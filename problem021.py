"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

def d(n):
	sumdivisors = 0
	for i in range(1, int(n/2) + 1):
		if n % i == 0:
			sumdivisors += i
	return sumdivisors

amicable_nums = [220, 284]

for i in range(285, 10000):
	b = d(i)
	if i == d(b) and i != b:
		amicable_nums.append(i)

print(sum(amicable_nums))

# [Finished in 13.7s]