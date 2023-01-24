#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    total_nums = len(arr)
    results = {'positive': 0, 'negative': 0, 'zero': 0}

    for num in arr:
        if num > 0:
            results['positive'] += 1
        elif num < 0:
            results['negative'] += 1
        else:
            results['zero'] += 1

    for name, num in results.items():
        if num > 0:
            results[name] = round(num/total_nums, 6)

    print(results['positive'])
    print(results['negative'])
    print(results['zero'])


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
