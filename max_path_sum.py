def maxPathSum(triangle):
    maxSum = 0

    for row in range(len(triangle)-1, 0, -1):
        for num in range(0, len(triangle[row])-1):
            triangle[row-1][num] += max(triangle[row][num], triangle[row][num+1])
            if triangle[row-1][num] > maxSum:
                maxSum = triangle[row-1][num]
    return maxSum
