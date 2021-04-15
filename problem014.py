"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

terms = 1
longest_chain = 0

for i in range(999999,1,-1):
    starting_n = i
    node = i
    while node > 1:
        if node%2 == 0:
            node = node/2
        else:
            node = (node*3) + 1
        terms += 1

    if terms > longest_chain:
        longest_chain = terms
        w_starting_number = starting_n

    terms = 1

print(w_starting_number)

# [Finished in 164.8s]