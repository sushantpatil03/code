import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def measure_time(algorithm, input_size):
    arr = [random.randint(1, 1000) for _ in range(input_size)]
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time
    
input_sizes = [10, 100, 1000, 10000, 100000]  # Add more sizes as needed

for size in input_sizes:
    merge_sort_time = measure_time(merge_sort, size)
    quick_sort_time = measure_time(quick_sort, size)

    print(f"Input Size: {size}\nMerge Sort Time: {merge_sort_time:.6f} seconds\nQuick Sort Time: {quick_sort_time:.6f} seconds\n")
