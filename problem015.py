"""

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""

from math import factorial

def calculateNumsOfPaths(a,b):
    steps = a + b
    nStepsSouth = a
    numerator = 1

    for i in range(steps, steps-nStepsSouth, -1):
        numerator = numerator * i
        
    nRoutes = int(numerator / factorial(nStepsSouth))
    print('there are',nRoutes,'routes to the bottom right corner')

calculateNumsOfPaths(20,20)

# [Finished in 0.2s]
