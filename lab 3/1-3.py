import time
import random

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    
    return merge(left, right)

def merge_sort_iterative(arr):
    n = len(arr)
    size = 1
    while size < n:
        for i in range(0, n, 2 * size):
            left = arr[i:i + size]
            right = arr[i + size:i + 2 * size]
            arr[i:i + len(left) + len(right)] = merge(left, right)
        size *= 2
    return arr

def test_merge_sort():
    test_case = [random.randint(0, 999999) for _ in range(999999)]

    start_time = time.time()
    recursive_result = merge_sort_recursive(test_case)
    recursive_time = time.time() - start_time
    print(f"Time taken for Recursive Sort: {recursive_time:.6f} seconds")

    start_time = time.time()
    iterative_result = merge_sort_iterative(test_case)
    iterative_time = time.time() - start_time
    print(f"Time taken for Iterative Sort: {iterative_time:.6f} seconds")

    print('-' * 40)

test_merge_sort()



