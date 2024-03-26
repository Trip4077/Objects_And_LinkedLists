'''
Compute the value f(n) for a number of input integeres, nums, where 
f() is an expensive time-consuming function

return the results of f(n) un an array

Cache the results of previous calls to keep from timing out

add f() before solution

input: integer array
'''
import time


def f(n):
    r = 1

    for _ in range(5000000):
        r = ((r + n) * n) % 9973

    return r


def solution(nums):
    start = time.time()

    results = []
    cache = {}

    for n in nums:
        if n not in cache:
            cache[n] = f(n)

        results.append(cache[n])

    end = time.time()
    time_to_run = end - start
    print("Time taken to run the function:", time_to_run, "seconds")
    print(results)
    return results


test_1 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
assertion_1 = [3528, 135, 4115, 3528, 135, 4115, 3528, 135, 4115]

test_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assertion_2 = [3528, 3528, 3528, 3528, 3528,
               3528, 3528, 3528, 3528, 3528, 3528]

tests = [test_1, test_2]
assertions = [assertion_1, assertion_2]

for i in range(len(tests)):
    print(
        solution(tests[i]) == assertions[i]
    )
