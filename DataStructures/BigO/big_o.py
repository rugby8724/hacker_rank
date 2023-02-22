import time
arr = [1, 2, 3]

one_start = time.time()


def func_one(a):
    return 1+a[0]


func_one(arr)
one_stop = time.time()

two_start = time.time()


def func_two(arr):
    return sum(arr)


func_two(arr)

two_stop = time.time()


print(f'one: {one_stop-one_start}')
print(f'two: {two_stop-two_start}')
