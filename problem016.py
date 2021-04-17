"""

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

def sumDigits(num):
    digits = str(num)
    listOfDigits = []

    for i in digits:
        listOfDigits.append(int(i))

    print(sum(listOfDigits))

sumDigits(2**1000)

# [Finished in 0.3s]
