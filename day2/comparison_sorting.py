def countingSort(arr):
    # Write your code here
    result_arr = [0] * 100
    for num in arr:
        result_arr[num] += 1

    return result_arr
