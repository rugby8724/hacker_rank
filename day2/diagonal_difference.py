def diagonalDifference(arr):
    # Write your code here
    leftSum = 0
    rightSum = 0
    loop = 0
    for i in range(len(arr)):
        leftSum += arr[loop][loop]
        rightSum += arr[loop][len(arr) - 1 - loop]
        loop += 1

    return abs(leftSum - rightSum)
