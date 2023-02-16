def sortedSquaredArray(array):
    # Write your code here.
    def squareNum(num):
        return num**2
    result = list(map(squareNum, array))
    result.sort()
    return result