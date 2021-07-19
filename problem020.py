from math import factorial

fact_num = str(factorial(100))
digits_sum = 0

for n in fact_num:
	digits_sum += int(n)

print(digits_sum)

# [Finished in 373ms]